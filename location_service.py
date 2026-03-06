# services/location_service.py


def get_nearby_hospitals(latitude: float, longitude: float):

    hospitals = [
        {
            "name": "Rural Health Clinic",
            "distance": "2 km",
            "location": "Village Center"
        },
        {
            "name": "Government Hospital",
            "distance": "4 km",
            "location": "Main Town"
        },
        {
            "name": "Community Medical Center",
            "distance": "6 km",
            "location": "District Road"
        }
    ]

    return {
        "user_location": {
            "latitude": latitude,
            "longitude": longitude
        },
        "hospitals": hospitals
    }