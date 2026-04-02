import os  # Importing the Groq Library to use its API.
import json  # Importing functions to read and write JSON files.
from dotenv import load_dotenv  # Importing the read dotenv_values function.
from dotenv import dotenv_values  # Importing dotenv_values to read environment variables from files.

# Load environment variables from the .env file.
env_vars = dotenv_values(".env")

# Retrieve specific environment variables for username, assistant name, and API key.
username = env_vars.get("Username")
assistant_name = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")

# Initialize the Groq client using the provided API key.
client = Groq(api_key=GroqAPIKey)

# Initialize a list to store chat messages.
messages = []

# Define a system message that provides context to the AI
System= """"""
# A list of system instructions for the chatbot.
SystemChatBot = [{"role": "system", "content": System}]

# Attempt to load the chat log from a JSON file.
try:
    with open("Data\ChatLog.json", "r") as f:
        Messages = load(f) # Load existing messages from chat log.
except FileNotFoundError:
    with open("DataChatLog.json", "w") as f:
        dump([], f)

def RealtimeInformation():
    date_time = datetime.datetime.now()  # Get the current date and time.
    day = date_time.strftime("%A")  # Day of the week.
    date = date_time.strftime("%d")  # Current date.
    month = date_time.strftime("%B") #Day of the month.
    year= date_time.strftime("%Y") #month name.
    hour = date_time.strftime("%H")  # Current hour.
    minute = date_time.strftime("%M")  #  minute.
    second = date_time.strftime("%S") #second.
    data = f"please use this real-time information if needed,\n"
    data+= f"Day: {day}\nMonth: {month}\nDate: {date}\nYear: {year}\n"
    data+= f"Time: {hour} hr:{minute} min:{second} secs.\n"
    return data

    def AnswerModifier(Answer):
        lines = Answer.split("\n")
        non_empty_lines = [line for line in lines if line.strip()]
        modified_answer = "\n".join(non_empty_lines)