from django.http import HttpResponse
from django.http import JsonResponse
import json 
from django.views.decorators.csrf import csrf_exempt
from ..utils import generate_response
from .models import Article
from django.shortcuts import render
import tensorflow as tf
from transformers import GPT2Tokenizer, TFGPT2LMHeadModel




def home(request):
    return render(request, 'home.html')


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

def chatbot_view(request):
    return render(request, 'chatbot.html')


# Initialisation du tokenizer et du modèle
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = TFGPT2LMHeadModel.from_pretrained('gpt2')

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors='tf')
    outputs = model.generate(inputs['input_ids'], max_length=100, num_return_sequences=1)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text


@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_message = data['message']
        bot_response = generate_response(user_message)
        return JsonResponse({'response': bot_response})

    return JsonResponse({'error': 'Invalid request'})