import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from PIL import Image
import io
from django.http import HttpResponse
from .utils import textgen
import json

API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": f"Bearer {API_TOKEN}"}


class GenerateImageView(APIView):
    def get(self, request):
        payload1 = textgen()

        # Original text
        # text = '[{"generated_text": "A painting of establishment and the concept of the concept of the con"}]'

        # Convert text to list of dictionaries
        data = json.dumps(payload1)
        data = json.loads(data)

        # Extract the generated_text value
        generated_text = data[0]['generated_text']

        # Create the desired dictionary
        payload = {'inputs': generated_text}

        print(payload)

        response = self.query(payload)
        image_bytes = response.content

        image = Image.open(io.BytesIO(image_bytes))
        image_path = 'generatedimage.jpg'
        image.save(image_path)

        with open(image_path, 'rb') as f:
            image_data = f.read()

        response = HttpResponse(content_type='image/jpeg')
        response['Content-Disposition'] = 'attachment; filename="generatedimage.jpg"'
        response.write(image_data)

        return response

    def query(self, payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response


class GenerateView(APIView):
    def get(self, request):
        # message = request.query_params.get('message')
        # # message = request.get('message')
        # if message is not None:
        #     input_text = message
        # else:
        #     # Generate random text using utils.Textgen()
        input_text = "bird in a cage"
        payload = {"inputs": input_text}
        response = requests.post(
            API_URL, headers=headers, json=payload)
        image_bytes = response.content
        print('got image')
        print(image_bytes)
        # Create a PIL image object from the image bytes
        image = Image.open(io.BytesIO(image_bytes))

        # Create a BytesIO object to store the JPEG image data
        jpeg_bytes = io.BytesIO()

        # Save the image as JPEG to the BytesIO object
        image.save(jpeg_bytes, format='JPEG')

        # Set the appropriate response headers
        response = HttpResponse(content_type='image/jpeg')
        response['Content-Disposition'] = 'attachment; filename="generatedimage.jpg"'

        # Set the BytesIO object as the response content
        response.write(jpeg_bytes.getvalue())

        return response
