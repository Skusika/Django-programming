from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# def monday(request):
#     return HttpResponse("1. Поднять детей. 2 Покормить завтракомю 3 Пожрать самой.")
#
# def tuesday(request):
#     return HttpResponse("1.Встать с кровати 2. Изучить питон")

spisok_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_info_about_sign_days(request, sign_days):
    if sign_days == "monday":
        return HttpResponse("Это понедельник")
    elif sign_days == "tuesday":
        return HttpResponse("Это вторник")
    elif sign_days == "wednesday":
        return HttpResponse("Это среда")
    elif sign_days == "thursday":
        return HttpResponse("Это четверг")
    elif sign_days == "friday":
        return HttpResponse("Это пятница")
    elif sign_days == "saturday":
        return HttpResponse("Это суббота")
    elif sign_days == "sunday":
        return HttpResponse("Это воскресенье")
    else:
        # return HttpResponseNotFound(f"Неизвестный день недели - {sign_days}")
        return render(request, 'week_days/greeting.html')

# def get_number_days(request, sign_days):
#     if 1 <= sign_days <= 7:
#         return HttpResponse(f"Сегодня {sign_days} день недели")
#     else:
#         return HttpResponse(f'Неверный номер дня - {sign_days}')

def get_number_days(request, sign_days: int):
    if sign_days > len(spisok_days):
        return HttpResponseNotFound(f'Неверный день недели')
    name_of_the_day = spisok_days[sign_days - 1]
    redirect_url = reverse("test", args=[name_of_the_day])
    return HttpResponseRedirect(redirect_url)



