import requests
from django.shortcuts import render
from django.core.paginator import Paginator


def fetch_news(last_news_id=None):
    api_url = "https://a24916-27c7.w.d-f.pw/api/news/last"
    api_key = "0203infinity2024"
    params = {
        'api': api_key,
        'count': 1000,
    }
    if last_news_id:
        params['last_news_id'] = last_news_id

    response = requests.get(api_url, params=params)
    response.raise_for_status()
    return response.json()


def index(request):
    news_list = fetch_news()
    paginator = Paginator(news_list, 30)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news/index.html', {'page_obj': page_obj})
