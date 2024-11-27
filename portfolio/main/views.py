import os
import json
from datetime import datetime

import requests
from django.conf import settings
from django.shortcuts import render


def main(request):
    file_path = os.path.join(settings.BASE_DIR, 'data', 'portfolio.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        portfolio_data = json.load(file)

    url = "https://api.github.com/users/githubstevemas/repos?per_page=100"
    response = requests.get(url)
    repos = response.json()

    for repo in repos:
        repo['updated_at'] = datetime.strptime(repo['updated_at'],
                                               "%Y-%m-%dT%H:%M:%SZ")

    return render(request, 'main.html',
                  {'portfolio_data': portfolio_data,
                   'repos': repos})
