import cohere
from rich import print
from dotenv import dotenv_values

# Load environment variables
env_vars = dotenv_values(".env")
CohereAPIKey = env_vars.get("CohereAPIKey")

# Initialize Cohere client
co = cohere.Client(api_key=CohereAPIKey)

# Define known function prefixes
funcs = [
    "exit", "general", "realtime", "open", "close", "play", "generate image",
    "system", "content", "google search", "youtube search", "reminder"
]

# Message history and preamble
messages = []

preamble = """
You are a very accurate Decision-Making Model, which decides what kind of a query is given to you.
You will decide whether a query is a 'general' query, a 'realtime' query, or is asking to perform any task or automation...
*** Do not answer any query, just decide what kind of query is given to you. ***
"""

# Convert ChatHistory to v2 format (assistant instead of Chatbot)
ChatHistory = [
    {"role": "user", "content": "how are you?"},
    {"role": "assistant", "content": "general how are you?"},
    {"role": "user", "content": "do you like pizza?"},
    {"role": "assistant", "content": "general do you like pizza?"},
    {"role": "user", "content": "open chrome and tell me about Mahatma Gandhi."},
    {"role": "assistant", "content": "open chrome, general tell me about Mahatma Gandhi."},
    {"role": "user", "content": "open chrome and Microsoft edge"},
    {"role": "assistant", "content": "open chrome, open edge."},
    {"role": "user", "content": "what is today's date and by the way remind me that I have a class on 5th August at 11:00 AM"},
    {"role": "assistant", "content": "general today's date , reminder set for class on 5th August at 11:00 AM."},
    {"role": "user", "content": "chat with me."},
    {"role": "assistant", "content": "general chat with me."}
]

def first_layer_DMM(prompt: str = "test") -> list[str]:
    messages.append({"role": "user", "content": prompt})

    # Build full conversation context
    convo = [{"role": "system", "content": preamble}] + ChatHistory + [{"role": "user", "content": prompt}]

    response = co.chat(
        model="command-a-reasoning-08-2025",
        messages=convo,
        temperature=0.7
    )

    # Extract text from response
    response_text = response.message.content[0].text

    # Clean and split response
    response_text = response_text.replace('\n', '')
    response_list = [i.strip() for i in response_text.split(';')]

    # Filter valid function-prefixed responses
    filtered = [task for task in response_list if any(task.startswith(func) for func in funcs)]

    # If no valid task detected, fallback to general
    return filtered if filtered else [f"general {prompt.strip()}"]

if __name__ == "__main__":
    while True:
        user_input = input(">>> ")
        result = first_layer_DMM(user_input)
        print(result)