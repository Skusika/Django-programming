from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Book, Author, CustomUser
from django.views.generic import ListView, DetailView
from django.db.models import F, Sum, Max, Min, Count, Avg, Value


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'my_library/register.html', {'form': form})


# def profile(request):
#     return render(request, 'my_library/profile.html')

def home(request):
    return render(request, 'my_library/home.html')


@login_required
def profile(request):
    return render(request, 'users/profile.html')


class OneBook(DetailView):
    template_name = 'my_library/one_book.html'
    model = Book


def show_all_book(request):
    # movies = Movie.objects.order_by(F('year').asc(nulls_last=True), 'rating')
    books = Book.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_field=Value('Hello'),
        int_field=Value(123)
    )
    for book in books:
        book.save()
    return render(request, 'my_library/all_books.html', {
        'books': books
    }
                  )

def show_one_book(request):
    book = get_object_or_404(Book)
    return render(request, 'my_library/one_book.html', {
        'book': book
    })

def show_authors(request):
    authors = Author.objects.order_by('name')
    for author in authors:
        author.save()
    return render(request, 'my_library/authors.html', {
        'authors': authors
    })
