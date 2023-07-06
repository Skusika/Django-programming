from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.

def glav(request):
    response = render_to_string('blog/index.html')
    # return HttpResponse("Главная страница")
    return HttpResponse(response)

def posts(request):
    # return HttpResponse("Все посты блога")
    return render(request, 'blog/list_detail.html')
def info_post_sign(request,name_post:str):
    return HttpResponse(f"Информация о посте {name_post}")

def post_info(request, number_post:int):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')

