from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.core.paginator import Paginator
from .models import Post
from .forms import ProfileForm

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
    user = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(author=user).order_by('-created_at')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/profile_view.html', {
        'profile_user': user,
        'page_obj': page_obj,
    })

@login_required
def profile_edit(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль обновлён!')
            return redirect('profile_view', user_id=request.user.id)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'blog/profile_edit.html', {'form': form})

@login_required
def profile_delete(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, 'Ваш профиль удалён.')
        return redirect('home')
    return render(request, 'blog/profile_delete.html')

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