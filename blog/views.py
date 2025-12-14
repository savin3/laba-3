from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.core.paginator import Paginator
from .models import Post

def home(request):
    posts = Post.objects.select_related('author').order_by('-created_at')
    paginator = Paginator(posts, 10)  # Пока 10, потом можно 50
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/home.html', {'page_obj': page_obj})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} создан!')
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ошибка при регистрации.')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {username}!')
                return redirect('home')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, 'Вы вышли из аккаунта.')
    return redirect('home')


def profile_view(request, user_id):
    return HttpResponse(f"Профиль пользователя с ID {user_id}")

def profile_edit(request):
    return HttpResponse("Редактирование профиля")

def profile_delete(request):
    return HttpResponse("Удаление профиля")

def post_create(request):
    return HttpResponse("Создание поста")

def post_detail(request, post_id):
    return HttpResponse(f"Пост №{post_id}")

def post_edit(request, post_id):
    return HttpResponse(f"Редактирование поста №{post_id}")

def post_delete(request, post_id):
    return HttpResponse(f"Удаление поста №{post_id}")

def comment_edit(request, comment_id):
    return HttpResponse(f"Редактирование комментария №{comment_id}")

def comment_delete(request, comment_id):
    return HttpResponse(f"Удаление комментария №{comment_id}")

def like_post(request, post_id):
    return HttpResponse(f"Лайк поста №{post_id}")