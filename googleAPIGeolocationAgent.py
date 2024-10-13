import os
import requests
from uagents import Agent, Context, Model

# Load the API key from environment variable
GOOGLE_API_KEY = "AIzaSyBvo0dTu0VrP46PyTW8ORJuCllJxWxF3Wc"

class GeolocationRequest(Model):
    address: str

class GeolocationResponse(Model):
    latitude: float
    longitude: float

agent = Agent(
    name="user",
    endpoint="http://localhost:8000/submit",
)

AI_AGENT_ADDRESS = "agent1qvnpu46exfw4jazkhwxdqpq48kcdg0u0ak3mz36yg93ej06xntklsxcwplc"

address = "Kings Cross Station, London"

def geocode_address(address: str):
    # URL for the Geocoding API request
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GOOGLE_API_KEY}"
    response = requests.get(geocode_url)
    if response.status_code == 200:
        result = response.json()
        if result['status'] == 'OK':
            location = result['results'][0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            raise ValueError(f"Geocoding API error: {result['status']}")
    else:
        raise ConnectionError(f"Failed to connect to Geocoding API: {response.status_code}")

@agent.on_event("startup")
async def send_message(ctx: Context):
    try:
        latitude, longitude = geocode_address(address)
        await ctx.send(AI_AGENT_ADDRESS, GeolocationResponse(latitude=latitude, longitude=longitude))
        ctx.logger.info(f"Sent geolocation to Geolocation agent: {latitude}, {longitude}")
    except Exception as e:
        ctx.logger.error(f"Error during geocoding: {e}")

@agent.on_message(GeolocationResponse)
async def handle_response(ctx: Context, sender: str, msg: GeolocationResponse):
    ctx.logger.info(f"Received response from {sender}:")
    ctx.logger.info(f"Latitude: {msg.latitude}, Longitude: {msg.longitude}")

if __name__ == "__main__":
    agent.run()