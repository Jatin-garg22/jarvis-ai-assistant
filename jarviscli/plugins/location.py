import requests

from plugin import plugin, require


@require(network=True)
@plugin("location")
def location(jarvis, s):
    """It gives you your current location"""
    send_url = "https://ipapi.co/json/"

    try:
        geo_req = requests.get(send_url, timeout=10)
        geo_req.raise_for_status()
        geo_json = geo_req.json()
    except requests.RequestException:
        jarvis.say("Could not fetch your location right now. Please try again later.")
        return

    latitude = geo_json.get("latitude", "unknown")
    longitude = geo_json.get("longitude", "unknown")
    city = geo_json.get("city", "unknown")
    region = geo_json.get("region", "")
    country = geo_json.get("country_name", geo_json.get("country", "unknown"))
    postal = geo_json.get("postal", geo_json.get("zip", "unknown"))

    jarvis.say("Latitude: {}".format(latitude))
    jarvis.say("Longitude: {}".format(longitude))
    jarvis.say("City: {}".format(city))
    if region:
        jarvis.say("Region: {}".format(region))
    jarvis.say("Country: {}".format(country))
    if postal:
        jarvis.say("Postal code: {}".format(postal))
