"""
This agent is capable of receiving messages and reply to the sender.
"""

from uagents import Agent, Context, Model
import requests

agent = Agent()

class Request(Model):
    message: str

def get_attr(city_name, api):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        'query': city_name,
        'key': api,
        'type': 'tourist_attraction',
    }
    response = requests.get(url, params)
    data = response.json()
    li = []
    # print(data)
    # if 'results' in data:
    for place in data['results']:
        name = place.get('name')
        rating = place.get('rating')
        addy = place.get('formatted_address')
        li.append(f"{name}: {rating} stars\n{addy}\n")
    # else:
    #     return ("No results found.")
    str2 = ''.join(li)
    return str2



@agent.on_message(model=Request)
async def handle_message(ctx: Context, sender: str, msg: Request):
    """Log the received message and reply to the sender"""
    city = msg.message
    api_key = 'AIzaSyBvo0dTu0VrP46PyTW8ORJuCllJxWxF3Wc'
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    ctx.logger.info(city)
    ctx.logger.info(get_attr(city, api_key))
    await ctx.send(sender, Request(message= get_attr(city, api_key)))
    ctx.logger.info(f"Message has been sent to User Agent")




if __name__ == "__main__":
    agent.run()
