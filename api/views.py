import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Name, Country, NameCountryProbability
from .serializers import NameCountryProbabilitySerializer
from django.utils.timezone import now
from .utils import get_or_create_country_from_api
from drf_spectacular.utils import extend_schema
from .schemas import name_country_schema, popular_names_schema



class NameCountryView(APIView):
    @extend_schema(
        parameters=name_country_schema["parameters"],
        responses=name_country_schema["responses"]
    )
    def get(self, request):
        name_param = request.query_params.get('name', None)
        if not name_param:
            return Response({"error": "Query param 'name' is required"}, status=400)

        response = requests.get(f"https://api.nationalize.io?name={name_param}")
        data = response.json()

        name_obj, _ = Name.objects.get_or_create(name=data['name'])
        name_obj.last_accessed = now()
        name_obj.request_count += 1
        name_obj.save(update_fields=["last_accessed", "request_count"])

        result = []
        for country_info in data.get('country', []):
            code = country_info['country_id']
            prob = country_info['probability']

            country_obj = get_or_create_country_from_api(code)

            NameCountryProbability.objects.update_or_create(
                name=name_obj,
                country=country_obj,
                defaults={'probability': prob}
            )
            result.append({
                "name": name_obj.name,
                "country": {"code": code, "name": country_obj.name},
                "probability": prob
            })

        print("DEBUG:", name_obj.last_accessed)
        return Response(result)


class PopularNamesView(APIView):
    @extend_schema(
        parameters=popular_names_schema["parameters"],
        responses=popular_names_schema["responses"]
    )
    def get(self, request):
        country_code = request.query_params.get('country', None)
        if not country_code:
            return Response({"error": "Query param 'country' is required"}, status=400)

        try:
            country = Country.objects.get(code=country_code)
        except Country.DoesNotExist:
            return Response({"error": f"Country with code '{country_code}' not found."}, status=404)

        qs = NameCountryProbability.objects.filter(country=country).order_by('-probability')[:5]
        serializer = NameCountryProbabilitySerializer(qs, many=True)
        return Response(serializer.data)


def process_name_request(name_str):
    name_obj, _ = Name.objects.get_or_create(name=name_str)
    name_obj.request_count += 1
    name_obj.last_accessed = now()
    name_obj.save(update_fields=["last_accessed"])
    name_obj.save()
    return name_obj

from .models import NameCountryProbability

def save_probability(name_obj, country_obj, prob):
    NameCountryProbability.objects.update_or_create(
        name=name_obj,
        country=country_obj,
        defaults={'probability': prob}
    )

class NationalityView(APIView):
    def get(self, request, name):
        name_obj, _ = Name.objects.get_or_create(name=name)
        name_obj.request_count += 1
        name_obj.last_accessed = now()
        name_obj.save()

        response = requests.get(f"https://api.nationalize.io/?name={name}")
        countries_data = response.json()['country']

        results = []

        for c in countries_data:
            country_obj = get_or_create_country_from_api(c['country_id'])
            save_probability(name_obj, country_obj, c['probability'])

            results.append({
                'country': country_obj.name,
                'probability': c['probability'],
                'flag': country_obj.flag_svg,
                'capital': country_obj.capital_name,
                'region': country_obj.region,
            })
        return Response({'name': name, 'results': results})
