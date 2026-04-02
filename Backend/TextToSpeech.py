import cohere

co = cohere.Client("your-api-key")
response = co.chat(model="command-r", message="ping")
print(response.text)