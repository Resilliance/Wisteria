from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
#import requests
import json
import base64

# Create your views here.
def index(request):
    """if request.method == "POST":
        user_input = request.POST.get('user_input', None)
        user_url = {'user_input' : user_input }
        if user_input is not None:
            detection(user_url)
        else:
            return redirect('index')"""
    return render(request, 'wisteria/index.html')

def detection(request):
    """input_base64 = requests.post(
                "https://3af31b1a-06af-46fb-8445-72f7347c17b2.syndic.ai",
                headers={"Content-Type": "application/json"},
                data= user_url)
    decoded_input = base64.decodestring(input_base64)
    image_result = open(decoded_input)
    print(decoded_input)"""
    
    return render(request,'wisteria/detection.html')
