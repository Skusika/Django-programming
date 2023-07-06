from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import math
from django.urls import reverse


# Create your views here.

def get_rectangle_area(request, lengh:int, width:int):
    area = lengh * width
    # return HttpResponse(f'Площадь прямоугольника размером {lengh} x {width} равна {area}')
    return render(request, 'geometry/rectangle.html')

def get_square_area(request, d:int):
    a = d ** 2
    # return HttpResponse(f'Площадь квадрата размером {d} x {d} равна {a}')
    return render(request, 'geometry/square.html')

def get_circle_area(request, rad:int):
    s = math.pi * rad ** 2
    # return HttpResponse(f'Площадь круга радиуса {rad} равна {s:.2f}')
    return render(request, 'geometry/circle.html')


def rectangle(request, width: int, height: int):
    redirect_url = reverse('one', args=[width, height])
    return HttpResponseRedirect(redirect_url)

def square(request, width: int):
    redirect_url = reverse('two', args=[width])
    return HttpResponseRedirect(redirect_url)

def circle(request, radius: int):
    redirect_url = reverse('three', args=[radius])
    return HttpResponseRedirect(redirect_url)