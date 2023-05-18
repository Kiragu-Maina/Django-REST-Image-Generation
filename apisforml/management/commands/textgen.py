
from django.core.management.base import BaseCommand
import requests


API_URL = "https://api-inference.huggingface.co/models/TurkuNLP/gpt3-finnish-small"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

class Command(BaseCommand):
    help = "Generates a sentence using the Starcoder model."

    def handle(self, *args, **options):
        payload = {
            "inputs": "A painting of ",
        }
        output = query(payload)
        print(output)


