import os
from dotenv import load_dotenv
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import google.generativeai as genai
import json

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash')

# Store in-memory conversation (non-persistent)
conversation_history = []

def generate_shakespearean_response(user_input):
    prompt = f"New Context. Respond to the following in the style of William Shakespeare:\n{user_input}"

    if conversation_history:
        messages = []
        for turn in conversation_history:
            messages.append({"role": "user", "parts": [turn["user"]]})
            messages.append({"role": "model", "parts": [turn["model"]]})
        messages.append({"role": "user", "parts": [prompt]})
        chat = model.start_chat(history=messages[:-1])
        response = chat.send_message(prompt)
    else:
        response = model.generate_content(prompt)

    return response.text

def chat_page(request):
    return render(request, 'chat.html')

@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_input = data.get("message")
        try:
            response = generate_shakespearean_response(user_input)
            conversation_history.append({"user": user_input, "model": response})
            return JsonResponse({"response": response})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
