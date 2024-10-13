# Imports
from uagents import Model, Agent, Context

# searchLocation's address
searchLocationAddress = "agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80"


# Create an agent
agent = Agent(
    name = "sendToLocator",
    seed = "kjbgfsipzwvgpifdsfncoerubcgbjbgfj",
    port = 8001,
    endpoint = ["http://127.0.0.1:8001/submit"]
)


class Request(Model):
    message: str


@agent.on_message(model=Request)
async def handle_message(ctx: Context, sender: str, msg: Request):
    "Log the received message"
    ctx.logger.info("We have received a list of locations!")
    ctx.logger.info(msg.message)


@agent.on_event("startup")
async def send_message(ctx: Context):
    "Send a message to searchLocations agent by specifying its address"
    userLocation = ('Nebraska')
    ctx.logger.info(userLocation)
    await ctx.send(searchLocationAddress, Request(message=userLocation))
    ctx.logger.info(f"Message has been sent to searchLocations agent")


if __name__ == "__main__":
    agent.run()
