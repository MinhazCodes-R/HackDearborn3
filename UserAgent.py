"""
This agent will send a message to agent Bob as soon as its starts.
"""
from uagents import Agent, Context, Model

agent = Agent()

class Request(Model):
    message: str

@agent.on_message(model=Request)
async def handle_message(ctx: Context, sender: str, msg: Request):
    """Log the received message along with its sender"""
    ctx.logger.info("we just got mail!")
    ctx.logger.info(msg.message)
    # ctx.logger.info(f"Received message from {sender}: {msg.message}")

ai_addy = 'agent1qf37w8hy4erz74k8nt8m9lf89aw6mcp7ym29txntd0x08qxh6wlxw7u5tdj'
@agent.on_event("startup")
async def send_message(ctx: Context):
    """Send a message to AI agent by specifying its address"""
    city = ('Chicago') # change to user input city
    ctx.logger.info(city)
    await ctx.send(ai_addy, Request(message=city))
    ctx.logger.info(f"Message has been sent to AI agent")

if __name__ == "__main__":
    agent.run()
