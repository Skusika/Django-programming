from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
import random
# Create your views here.

peoples = [
    'Жукова Анна Константиновна',
    'Юлия Степановна Потапова',
    'Гущин Аполлинарий Тимурович',
    'Дорофей Ярославович Третьяков',
    'Селезнева Анна Тарасовна',
    'Федотов Симон Харлампьевич',
    'Красильникова Вера Борисовна',
    'Бажен Тихонович Костин',
    'Веселова Анжелика Тимофеевна',
    'Щербаков Самсон Феодосьевич'
]
people_detail = [
    {'name': 'Жанна Ивановна Бобылева', 'age': 28, 'phone': '+72609577301'},
    {'name': 'Спиридон Феликсович Алексеев', 'age': 48, 'phone': '8 445 133 42 50'},
    {'name': 'Лыткина Зоя Рубеновна', 'age': 34, 'phone': '84061070300'},
    {'name': 'Олимпиада Святославовна Петухова', 'age': 70, 'phone': '8 740 992 96 95'},
    {'name': 'Лазарева Нина Кирилловна', 'age': 67, 'phone': '89040731989'},
    {'name': 'Каллистрат Ильич Ширяев', 'age': 63, 'phone': '+7 418 298 8976'},
    {'name': 'Евсеев Любосмысл Чеславович', 'age': 47, 'phone': '83111461302'},
    {'name': 'Прохор Харламович Артемьев', 'age': 47, 'phone': '+77827445919'},
    {'name': 'Кондрат Игнатьевич Ершов', 'age': 35, 'phone': '+7 419 594 39 00'},
    {'name': 'Ипат Власович Ильин', 'age': 47, 'phone': '88004779773'}
]

events = [
    {
        'title': 'Отдых',
        'description': 'Хорошо посидели',
        'date': '28 авг 2021',
        'content': 'Сегодня день рождения моего папы. Мы от всей души его поздравляем!'
    },
    {
        'title': 'Париж',
        'description': 'Незабываемое путешествие',
        'date': '5 сент 2020',
        'content': '''Мы с мужем наконец то посетили Париж. 
                Париж это город любви, не правда ли?'''
    },
    {
        'title': 'Финал лиги чемпионов',
        'description': 'Реал опять выиграл ЛЧ',
        'date': '28 мая 2022',
        'content': 'Как долго мы ждали этот матч. Ура!'
    },
    {
        'title': 'Охота на уток',
        'description': 'Ни одна утка не пострадала',
        'date': '7 дек 2019',
        'content': 'Ездили в лес, охотиться на уток. На болоте так необычно, с нами была еще и собака'
    },
    {
        'title': 'Фестиваль огурца',
        'description': 'Суздаль ждет тебя',
        'date': '12 июль 2021',
        'content': 'Фестиваль огурца это очень интересный праздник, и одно из самых значительных событий лета!'
    },
    {
        'title': 'Нашествие',
        'description': 'Даешь рок, но в следующем году',
        'date': '29 июль 2021',
        'content': 'Фестиваль может быть и ничего, но мы туда не ходим. это совершенно нам не интересно'
    },
    {
        'title': 'Новый год',
        'description': 'Эх, еще один год пролетел',
        'date': '31 дек 2022',
        'content': 'Много чего было в уходящем году, и плохого, и хорошего. Надеюсь, в наступающем году будет еще лучше'
    },
]
context = {
    'peoples': peoples,
    'detail': people_detail,
}

def glav(request):
    # response = render_to_string('base.html')
    # return HttpResponse("Главная страница")
    random.shuffle(events)
    events_end = {
        'events': events[0:3]
    }
    return render(request, 'blog/index.html', context=events_end)
    # return HttpResponse(response)

def posts(request):
    # return HttpResponse("Все посты блога")
    return render(request, 'blog/list_detail.html')
def info_post_sign(request,name_post:str):
    return HttpResponse(f"Информация о посте {name_post}")

def post_info(request, number_post:int):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')

def people_name(request):
    return render(request, 'blog/peoples.html', context=context)

def people_info(request):
    return render(request, 'blog/people_detail.html', context=context)


