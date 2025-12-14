from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Главная страница — тут будут посты")

def register(request):
    return HttpResponse("Регистрация")

def user_login(request):
    return HttpResponse("Вход")

def user_logout(request):
    return HttpResponse("Выход")

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