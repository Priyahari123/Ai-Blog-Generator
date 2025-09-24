import json
import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from ai.utills import generate_blog_article

@csrf_exempt  
def home(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        topic = data.get('topic', '')
       
        if topic:
            article = generate_blog_article(topic)
 
            return JsonResponse({'article': article})
        else:
            return JsonResponse({'error': 'No topic provided'}, status=400)
    else:
        return render(request,'chat.html')
