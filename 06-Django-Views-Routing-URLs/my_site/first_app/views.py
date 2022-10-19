from django.shortcuts import render
from django.http.response import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def simple_view(request):
    return HttpResponse('SAMPLE VIEWS ~~~~') # template HTML > JINJA

articles = {
    'sports':'Sport page~',
    'finance':'Finance page~',
    'politics':'Politics page~',
    'sports1':'Sport1 page1~',
}    

def sports_view(request):
    return HttpResponse(articles['sports'])

def finance_view(request):
    return HttpResponse(articles['finance'])

def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        # result = 'No page for that topic~'
        # return HttpResponseNotFound(result)
        raise Http404('404 generic ERROR') # 404.html 만들어서 처리 예정임,

def add_view(request, num1, num2):
    # domain.com/first_app/num1/num2 --> num1+num2
    result = f'{num1} + {num2} = {num1+num2}'
    return HttpResponse(str(result))

# domain.com/first_app/0 --> domain.com/first_app/finance
def num_page_view(request, num_page):
    try:
        print(f'')
        topics_list = list(articles.keys()) # ['sports','finance','politics']
        topic = topics_list[num_page]
        webpage = reverse('topic-page', args=[topic])
        print(f'{topics_list}  {num_page}  {topic}  {webpage}')
        return HttpResponseRedirect(webpage)
    except:
        raise Http404('404 generic ERROR') # 404.html 만들어서 처리 예정임,
