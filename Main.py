import cohere
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
co = cohere.Client(api_key=env_vars.get("CohereAPIKey"))

models = co.models.list()
print(models)