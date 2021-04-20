from django.shortcuts import render
from authentication.models import Exam

import requests

# Create your views here.

def base(request):
    return render(request,"base.html")

def ExamOnlineView(request):

    url = "https://opentdb.com/api.php?amount=10"
    json_data = requests.get(url).json()   
    json=json_data["results"]
    context={
        "result":json
    }

    return render(request,"index.html",context)


