import requests
from .models import Country

def get_or_create_country_from_api(code):
    try:
        return Country.objects.get(code=code)
    except Country.DoesNotExist:
        pass

    url = f"https://restcountries.com/v3.1/alpha/{code}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data for country code {code}")
    
    country_data = response.json()[0]

    return Country.objects.create(
        code = code,
        name = country_data.get('name', {}).get('common'),
        independent = country_data.get('independent'),
        google_maps = country_data.get('maps', {}).get('googleMaps'),
        open_street_map = country_data.get('maps', {}).get('openStreetMaps'),
        capital_name = country_data.get('capital', [None])[0],
        capital_lat = country_data.get('capitalInfo', {}).get('latlng', [None])[0],
        capital_lng = country_data.get('capitalInfo', {}).get('latlng', [None])[1] if len(country_data.get('capitalInfo', {}).get('latlng', [])) > 1 else None,
        region = country_data.get('region'),
        flag_png = country_data.get('flags', {}).get('png'),
        flag_svg = country_data.get('flags', {}).get('svg'),
        flag_alt = country_data.get('flags', {}).get('alt'),
        coat_of_arms_png = country_data.get('coatOfArms', {}).get('png'),
        coat_of_arms_svg = country_data.get('coatOfArms', {}).get('svg'),
        borders_with = ', '.join(country_data.get('borders', [])) if country_data.get('borders') else None
    )
