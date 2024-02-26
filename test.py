import llama_index
import os
from dotenv import load_dotenv

load_dotenv()

print(f"loading the api key")
print(f"OPENAI API KEY is : {os.environ['OPENAI_API_KEY']}")