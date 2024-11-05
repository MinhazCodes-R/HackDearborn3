# Imports
import time
from typing import Any, Dict
from uagents import Model, Agent, Context

# searchLocation's address
searchLocationAddress = "agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80"

# Create an agent
agent = Agent(
    name="sendToLocator",
    seed="kjbgfsipzwvgpifdsfncoerubcgbjbgfj",
    port=8001,
    endpoint=["http://127.0.0.1:8001/submit"]
)

# Define models for request and response data structures
class Request(Model):
    message: str

class Response(Model):
    timestamp: int
    text: str
    agent_address: str

# Receives list here
@agent.on_message(model=Request)
async def handle_message(ctx: Context, sender: str, msg: Request):
    "Log the received message"
    ctx.logger.info("We have received a list of locations!")
    ctx.logger.info(msg.message)

# Define a GET endpoint to check the agent's status
@agent.on_rest_get("/agent_status", Response)
async def get_status(ctx: Context) -> Dict[str, Any]:
    ctx.logger.info("Received GET request for agent status")
    return {
        "timestamp": int(time.time()),
        "text": "Agent is running and ready",
        "agent_address": ctx.agent.address,
    }

# Define a POST endpoint to receive data via HTTP and trigger message sending
@agent.on_rest_post("/submit_location", Request, Response)
async def submit_location(ctx: Context, req: Request) -> Response:
    ctx.logger.info(f"Received POST request with location: {req.message}")
    # Send the received location data to searchLocation agent
    await ctx.send(searchLocationAddress, Request(message=req.message))
    ctx.logger.info(f"Message with location '{req.message}' has been sent to searchLocation agent")
    
    return Response(
        text=f"Location '{req.message}' received and sent successfully",
        agent_address=ctx.agent.address,
        timestamp=int(time.time())
    )

if __name__ == "__main__":
    agent.run()
