import os
import json

from django.conf import settings
from django.shortcuts import render


def main(request):

    file_path = os.path.join(settings.BASE_DIR, 'data', 'portfolio.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        portfolio_data = json.load(file)

    return render(request, 'main.html',
                  {'portfolio_data': portfolio_data})
