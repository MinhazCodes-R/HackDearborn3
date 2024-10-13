# Imports
from uagents import Model, Agent, Context
import requests


# Create an agent
agent = Agent(
    name = "searchLocations",
    seed = "khavaioghgjabougrvbosubvisgvgjfkf",
    port = 8000,
    endpoint = ["http://127.0.0.1:8000/submit"]
)


class Request(Model):
    message: str


def get_attr(userLocationName, api):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        'query': userLocationName,
        'key': api,
        'type': 'tourist_attraction',
    }
    response = requests.get(url, params)
    data = response.json()
    locationList = []

    for place in data['results']:
        name = place.get('name')
        rating = place.get('rating')
        formAddress = place.get('formatted_address')
        locationList.append(f"{name}: {rating} stars\n{formAddress}\n")
    
    str2 = ''.join(locationList)
    return str2



@agent.on_message(model=Request)
async def handle_message(ctx: Context, sender: str, msg: Request):
    "Log the received message"
    city = msg.message
    api_key = 'AIzaSyBvo0dTu0VrP46PyTW8ORJuCllJxWxF3Wc'
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    ctx.logger.info(city)
    ctx.logger.info(get_attr(city, api_key))
    await ctx.send(sender, Request(message= get_attr(city, api_key)))
    # ctx.logger.info(f"Message has been sent to User sendToLocator")



    
if __name__ == "__main__":
    agent.run()
