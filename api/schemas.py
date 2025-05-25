from drf_spectacular.utils import OpenApiParameter
from .serializers import NameCountryProbabilitySerializer

name_country_schema = {
    "parameters": [
        OpenApiParameter(
            name='name',
            description='Person name to analyze (e.g. "andrii")',
            required=True,
            type=str,
            location=OpenApiParameter.QUERY,
        ),
    ],
    "responses": {
        200: NameCountryProbabilitySerializer(many=True)
    }
}

popular_names_schema = {
    "parameters": [
        OpenApiParameter(
            name='country',
            description='Country code (e.g. "UA", "US")',
            required=True,
            type=str,
            location=OpenApiParameter.QUERY,
        ),
    ],
    "responses": {
        200: NameCountryProbabilitySerializer(many=True)
    }
}
