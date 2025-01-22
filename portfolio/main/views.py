import os
import json
import requests

from datetime import datetime
from django.conf import settings
from django.shortcuts import render
from dotenv import load_dotenv

load_dotenv()


def main(request):

    lang = request.GET.get('lang', 'en')
    file_path = os.path.join(settings.BASE_DIR, 'data', f'portfolio_{lang}.json')

    with open(file_path, 'r', encoding='utf-8') as file:
        portfolio_data = json.load(file)

    url = "https://api.github.com/users/githubstevemas/repos?per_page=100"
    token = os.getenv('TOKEN_GITHUB')

    headers = {
        "Authorization": f"token {token}"
    }

    response = requests.get(url, headers=headers)
    repos = response.json()

    for repo in repos:
        print(repo['updated_at'])
        repo['updated_at'] = datetime.strptime(repo['updated_at'],
                                               "%Y-%m-%dT%H:%M:%SZ")

    repos = sorted(repos, key=lambda repo: repo['updated_at'], reverse=True)

    return render(request, 'main.html',
                  {'portfolio_data': portfolio_data,
                   'range_five': list(range(5)),
                   'repos': repos})
