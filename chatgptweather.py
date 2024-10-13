import requests
from uagents import Agent, Context, Model

# ChatGPT API key
API_KEY = "sk-UT_bubFHgd9RW9dAZ3Xk7fvksBKyYT0M0lJvUacUkFT3BlbkFJTB-unpyBMF6Rv5kti9ydHTsUbqbgIcJK9bBAcNkOoA"


class ChatGPTPrompt(Model):
    prompt: str


class ChatGPTResponse(Model):
    response: str


agent = Agent(
    name="chatgptweather",
    endpoint="http://localhost:8001/submit",
    seed="meowmeow",
    port=8001
)
print(agent.address)

def send_prompt(api_key, prompt):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,  # Controls the creativity of the response
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}, {response.text}"


@agent.on_message(ChatGPTPrompt)
async def handle_prompt(ctx: Context, sender: str, msg: ChatGPTPrompt):
    ctx.logger.info(f"Received ChatGPT prompt from {sender}: {msg.prompt}")

    chatgpt_response = send_prompt(API_KEY, msg.prompt)
    await ctx.send(sender, ChatGPTResponse(response=chatgpt_response))
    ctx.logger.info(f"Sent ChatGPT response to {sender}: {chatgpt_response}")


if __name__ == "__main__":
    agent.run()
