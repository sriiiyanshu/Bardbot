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
current_tone = {"tone": "shakespeare"}  # can be 'shakespeare' or 'normal'

def should_use_shakespeare(latest_user_input):
    modern_cues = ["talk normally", "normal language", "stop speaking like shakespeare", "modern english"]
    shakespeare_cues = [
    "talk like shakespeare",
    "speak like shakespeare",
    "switch to shakespearean",
    "speak old english",
    "bard style",
    "use shakespearean language"
]


    lowered = latest_user_input.lower()
    for phrase in modern_cues:
        if phrase in lowered:
            return "normal"
    for phrase in shakespeare_cues:
        if phrase in lowered:
            return "shakespeare"
    return None

def generate_response(user_input):
    tone_change = should_use_shakespeare(user_input)
    if tone_change:
        current_tone["tone"] = tone_change

    if current_tone["tone"] == "shakespeare":
        prompt = f"Respond in the style of William Shakespeare:\n{user_input}"
    else:
        prompt = f"Respond in modern English:\n{user_input}"

    messages = []
    for turn in conversation_history:
        messages.append({"role": "user", "parts": [turn["user"]]})
        messages.append({"role": "model", "parts": [turn["model"]]})
    messages.append({"role": "user", "parts": [prompt]})

    chat = model.start_chat(history=messages[:-1]) if messages else model
    response = chat.send_message(prompt) if hasattr(chat, 'send_message') else model.generate_content(prompt)

    return response.text

def chat_page(request):
    return render(request, 'chat.html')

@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_input = data.get("message")
        try:
            response = generate_response(user_input)
            conversation_history.append({"user": user_input, "model": response})
            return JsonResponse({"response": response})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
