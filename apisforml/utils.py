import requests
from django.http import HttpResponse
import json
import random





# API_URL = "https://api-inference.huggingface.co/models/TurkuNLP/gpt3-finnish-small"
API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer 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"}

def textgen():
    random_float = generate_random_float()
    random_description = generate_random_description()
    
    random_description = str(random_description)
    print(random_description)
    payload = {
        "inputs": random_description,
        "temperature": random_float
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def generate_random_float():
    return random.uniform(1.0, 100.0)

def generate_random_description():
    with open('description_starters.txt', 'r') as f:
        starters = f.read().splitlines()
        
    selected_starter = random.choice(starters)
    return selected_starter