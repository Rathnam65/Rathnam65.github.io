import phonenumbers
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode

def get_location_coordinates(phone_number, api_key):
    # Parse phone number
    parsed_number = phonenumbers.parse(phone_number)
    
    # Get location description
    location = geocoder.description_for_number(parsed_number, "en")
    
    # Initialize OpenCage Geocoder with API key
    geocoder = OpenCageGeocode(api_key)
    
    # Query for location coordinates
    results = geocoder.geocode(location)
    
    if results and len(results) > 0:
        latitude = results[0]['geometry']['lat']
        longitude = results[0]['geometry']['lng']
        return latitude, longitude
    else:
        return None

# Example usage
api_key = 'e529812872ac453dbe2eb19fea6b7c1d'
phone_number = "+919346504868"  # Example phone number

coordinates = get_location_coordinates(phone_number, api_key)

if coordinates:
    print(f"The coordinates for the phone number {phone_number} are: Latitude = {coordinates[0]}, Longitude = {coordinates[1]}")
else:
    print(f"Coordinates for the phone number {phone_number} could not be found.")
