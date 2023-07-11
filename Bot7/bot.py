import openai
import requests
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API")


def generate(text):
    result = openai.Image.create(prompt=text, n=1, size="512x512")
    return result["data"][0]["url"]


def main():
    text = "ai in future"
    url = generate(text)

    response = requests.get(url=url)
    Image.open(response.raw)


main()
