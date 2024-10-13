# ai agent
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
    return str(li)



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























# from uagents import Agent, Context, Model
# import requests
#
# class AttractionsRequest(Model):
#     city_name: str
#
# class AttractionsResponse(Model):
#     attractions: list
#
# agent = Agent(
#     name="ai_agent",
#     endpoint="http://localhost:8000/submit",
#     seed="i love poopee",
# )
# # print(agent.address)
#
# GOOGLE_API_KEY = "AIzaSyBvo0dTu0VrP46PyTW8ORJuCllJxWxF3Wc"
#
# @agent.on_message(AttractionsRequest)
# async def handle_request(ctx: Context, sender: str, msg: AttractionsRequest):
#     city_name = msg.city_name
#     attractions = get_attractions(city_name)
#     await ctx.send(sender, AttractionsResponse(attractions=attractions))
#     ctx.logger.info(f"Sent attractions for {city_name} to {sender[-10:]}")
#
# def get_attractions(city_name):
#     url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
#     params = {
#         'query': f'tourist attractions in {city_name}',
#         'key': GOOGLE_API_KEY,
#     }
#     response = requests.get(url, params=params)
#     data = response.json()
#     results = data.get('results', [])
#     attractions = [place['name'] for place in results]
#     return attractions
#
# if __name__ == "__main__":
#     # Print the AI agent's address
#     print(f"AI Agent Address: {agent.address}")
#     agent.run()
#
