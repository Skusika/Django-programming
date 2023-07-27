from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from dataclasses import dataclass


zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',

}

elements = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}

zodiac_dates = {
    1: {'capricorn': (1, 20), 'aquarius': (21, 31)},
    2: {'aquarius': (1, 19), 'pisces': (20, 29)},
    3: {'pisces': (1, 20), 'aries': (21, 31)},
    4: {'aries': (1, 20), 'taurus': (21, 30)},
    5: {'taurus': (1, 21), 'gemini': (22, 31)},
    6: {'gemini': (1, 21), 'cancer': (22, 30)},
    7: {'cancer': (1, 22), 'leo': (23, 31)},
    8: {'leo': (1, 21), 'virgo': (22, 31)},
    9: {'virgo': (1, 22), 'libra': (23, 30)},
    10: {'libra': (1, 23), 'scorpio': (24, 31)},
    11: {'scorpio': (1, 22), 'sagittarius': (23, 30)},
    12: {'sagittarius': (1, 22), 'capricorn': (23, 31)}
}


# Create your views here.

def index(request):
    zodiacs = list(zodiac_dict)
   # f'<li> <a href="{redirect_path}"> {sign.title()} </a> </li>'
    context = {
        'zodiacs': zodiacs,
        'zodiac_dict': zodiac_dict
    }
    return render(request, 'horoscope/index.html', context=context)
    # li_elements = ''
    # for sign in zodiacs:
    #     redirect_path = reverse('horoscope_name', args=[sign])
    #     li_elements += f'<li> <a href="{redirect_path}"> {sign.title()} </a> </li>'
    # response = f"""
    # <ol>
    #     {li_elements}
    # </ol>
    # """
    # return HttpResponse(response)

@dataclass
class Person:
    name: str
    age: int

    def __str__(self):
        return f'This is {self.name}'


def get_info_about_sign_zodiac(request, sign_zodiac):
    description = zodiac_dict.get(sign_zodiac)
    zodiacs = list(zodiac_dict)
    data = {
        'description': description,
        'sign': sign_zodiac.title(),
        'zodiacs': zodiacs
    }
    # response = render_to_string('horoscope/info_zodiac.html')
    return render(request, 'horoscope/info_zodiac.html', context=data)

def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Неправильный порядковый номер знака зодиака - {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac-1]
    redirect_url = reverse('horoscope_name', args=(name_zodiac, ))
    return HttpResponseRedirect(redirect_url)


def get_info_by_date(request, month: int, day: int):
    if (month == 3 and day in list(range(21, 32))) or (month == 4 and day in list(range(1, 21))):
        return HttpResponseRedirect(reverse('horoscope_name', args=['aries']))
    elif (month == 4 and day in list(range(22, 31))) or (month == 5 and day in list(range(1, 22))):
        return HttpResponseRedirect(reverse('horoscope_name', args=['taurus']))
    elif (month == 5 and day in list(range(21, 32))) or (month == 6 and day in list(range(1, 22))):
        return HttpResponseRedirect(reverse('horoscope_name', args=['gemini']))
    elif (month == 6 and day in list(range(22, 31))) or (month == 7 and day in list(range(1, 23))):
        return HttpResponseRedirect(reverse('horoscope_name', args=['cancer']))
    elif (month == 7 and day in list(range(23, 32))) or (month == 8 and day in list(range(1, 22))):
        return HttpResponseRedirect(reverse('horoscope_name', args=['leo']))
    elif (month == 8 and day in list(range(22, 32))) or (month == 9 and day in list(range(1, 23))):
        return HttpResponseRedirect(reverse('horoscope_name', args=['virgo']))
    elif (month == 9 and day in list(range(24, 31))) or (month == 10 and day in list(range(1, 24))):
        return HttpResponseRedirect(reverse('horoscope_name', args=['libra']))
    elif (month == 10 and day in list(range(24, 32))) or (month == 11 and day in list(range(1, 23))):
        return HttpResponseRedirect(reverse('horoscope_name', args=['scorpio']))
    elif (month == 11 and day in list(range(23, 31))) or (month == 12 and day in list(range(1, 23))):
        return HttpResponseRedirect(reverse('horoscope_name', args=['sagittarius']))
    elif (month == 12 and day in list(range(23, 32))) or (month == 1 and day in list(range(1, 21))):
        return HttpResponseRedirect(reverse('horoscope_name', args=['capricorn']))
    elif (month == 1 and day in list(range(21, 32))) or (month == 2 and day in list(range(1, 20))):
        return HttpResponseRedirect(reverse('horoscope_name', args=['aquarius']))
    elif (month == 2 and day in list(range(20, 29))) or (month == 3 and day in list(range(1, 21))):
        return HttpResponseRedirect(reverse('horoscope_name', args=['pisces']))
    else:
        return HttpResponseNotFound(f'Неизвестное значение {month}, {day} введите другое значение')

def type(request, type_name):
    li_elements = ''
    for sign in elements[type_name]:
        redirect_path = reverse('horoscope_name', args=[sign])
        li_elements += f"<li> <a href='{redirect_path}'>{sign.title()} </a> </li>"
    response = f'<ol> {li_elements} </ol>'
    return HttpResponse(response)


def get_znak(request):
    li_elements = ''
    for type in elements:
        li_elements += f'<li> <a href="{type}/"> {type.title()} </a> </li>'
    response = f'<ul> {li_elements} </ul> '
    return HttpResponse(response)

