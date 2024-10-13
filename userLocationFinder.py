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


class ChatGPTPrompt(Model):
    prompt: str


class ChatGPTResponse(Model):
    response: str


agent = Agent(
    name="user",
    endpoint="http://localhost:8000/submit",
    seed = 'poop',
    port=8000
)

AI_AGENT_ADDRESS = "agent1qwh8hhpc5cr2drsvd06n45wgt72fy7uj0tccrqzdnn3y0xyq4dn0z97zlvh"

address = "Kennedy Station, Scarborough"
user_start_date = "05/18/2025" # mm/dd/yy both
user_end_date = "06/15/2025"

def geocode_address(address: str):
    # URL for the Geocoding API request
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GOOGLE_API_KEY}"
    response = requests.get(geocode_url)
    if response.status_code == 200:
        result = response.json()
        if result['status'] == 'OK':
            location = result['results'][0]['geometry']['location']
            return location['lat'], location['lng']

@agent.on_event("startup")
async def send_message(ctx: Context):
    latitude, longitude = geocode_address(address)
    chatgpt_prompt = f"what's happening at latitude:{latitude}, longitude: {longitude} from {user_start_date} to {user_end_date}"
    await ctx.send(AI_AGENT_ADDRESS, GeolocationResponse(latitude=latitude, longitude=longitude))
    ctx.logger.info(f"Sent geolocation to Geolocation agent: {latitude}, {longitude}")
    await ctx.send(AI_AGENT_ADDRESS, ChatGPTPrompt(prompt=chatgpt_prompt))
    ctx.logger.info(f"Sent ChatGPT prompt to AI agent: {chatgpt_prompt}")


@agent.on_message(GeolocationResponse)
async def handle_geolocation_response(ctx: Context, sender: str, msg: GeolocationResponse):
    ctx.logger.info(f"Received geolocation response from {sender}:")
    ctx.logger.info(f"Latitude: {msg.latitude}, Longitude: {msg.longitude}")


@agent.on_message(ChatGPTResponse)
async def handle_chatgpt_response(ctx: Context, sender: str, msg: ChatGPTResponse):
    ctx.logger.info(f"Received ChatGPT response from {sender}: {msg.response}")


if __name__ == "__main__":
    agent.run()
