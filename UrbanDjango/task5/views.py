from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.

def sign_up_by_html(request):
    users = ['user1', 'user2', 'user3']
    info = {}

    if request.method == 'POST':
        user_have = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        is_user = username in users
        if password == repeat_password:
            if age >= 18:
                if is_user == False:
                    user_have = True
                else:
                    info['error'] = 'Пользователь уже существует'
            else:
                info['error'] = 'Вы должны быть старше 18'
        else:
            info['error'] = 'Пароли не совпадают'

        if user_have:
            message = (f'Приветствуем, {username}!')
            print(message)
        else:
            message = info['error']
        return HttpResponse(message)
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_django(request):
    users = ['user1', 'user2', 'user3']
    info = {}

    if request.method == 'POST':
        user_have = False
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            is_user = username in users
            if password == repeat_password:
                if age >= 18:
                    if is_user == False:
                        user_have = True
                    else:
                        info['error'] = 'Пользователь уже существует'
                else:
                    info['error'] = 'Вы должны быть старше 18'
            else:
                info['error'] = 'Пароли не совпадают'

            if user_have:
                message = (f'Приветствуем, {username}!')
                print(message)
            else:
                message = info['error']
        return HttpResponse(message)
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)
