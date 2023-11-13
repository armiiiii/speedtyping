import os
import json
import random

import requests
from django.http.response import JsonResponse

def view(request):
    url = "https://www.mit.edu/~ecprice/wordlist.10000" 
    resp = requests.get(url)
    words = resp.content.decode().splitlines()
    return JsonResponse(' '.join(random.choices(words, k=60)), safe=False)
