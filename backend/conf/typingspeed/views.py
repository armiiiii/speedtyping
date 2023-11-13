import json
import random

from django.shortcuts import render

import requests


def view(request):
    url = "https://www.mit.edu/~ecprice/wordlist.10000"
    resp = requests.get(url)
    words = resp.content.splitlines()
    return json.loads(' '.join(random.choices(words)))
