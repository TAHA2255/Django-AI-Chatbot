# Create your views here.



from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import os  # To access environment variables


DEEPINFRA_API_KEY = 'your api key'


def chatbot(request):
    return render(request, 'base.html')

@csrf_exempt
def get_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        if user_message:
            if not DEEPINFRA_API_KEY:
                return JsonResponse({'error': 'DeepInfra API key not configured'}, status=500)
            bot_response = generate_bot_response(user_message, DEEPINFRA_API_KEY)
            return JsonResponse({'response': bot_response})
        else:
            return JsonResponse({'error': 'No message received'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def generate_bot_response(user_message, api_key):
    api_url = "https://api.deepinfra.com/v1/openai/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/Meta-Llama-3-8B-Instruct",  
        "messages": [{"role": "user", "content": user_message}]
    }

    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        response_data = response.json()
        if response_data and 'choices' in response_data and len(response_data['choices']) > 0:
            return response_data['choices'][0]['message']['content']
        else:
            return "Sorry, I couldn't get a response from the AI."
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with DeepInfra API: {e}")
        return "There was an error communicating with the AI service."
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "An unexpected error occurred."