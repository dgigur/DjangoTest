from django.shortcuts import render
from .forms import UserRegister


def sign_up_by_django(request):
    hello = ''
    if request.method == "POST":
        form = UserRegister(request.POST)
        users = ['first', 'second', "third", "fourth"]
        info = {}
        context = {
            'users': users,
            'info': info,
            'form': form,
            }
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username not in users and password == repeat_password and int(age) >= 18:
                error = ''
                hello = f"Приветствуем, {username}!"
            else:
                if password != repeat_password:
                    error = 'Пароли не совпадают'
                elif int(age) < 18:
                    error = 'Вы должны быть старше 18'
                elif username in users:
                    error = 'Пользователь уже существует'
            context.update({"username": username,
                            "password": password,
                            "repeat_password": repeat_password,
                            'age': age,
                            'error': error,
                            'hello': hello,
                            })
            return render(request, 'registration_page.html', context)
    form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})


def sign_up_by_html(request):
    hello = ''
    if request.method == "POST":
        users = ['first', 'second', "third", "fourth"]
        info = {}
        context = {
            'users': users,
            'info': info,
        }
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if username not in users and password == repeat_password and int(age) >= 18:
            error = ''
            hello = f"Приветствуем, {username}!"
        else:
            if password != repeat_password:
                error = 'Пароли не совпадают'
            elif int(age) < 18:
                error = 'Вы должны быть старше 18'
            elif username in users:
                error = 'Пользователь уже существует'
        context.update({"username": username,
                        "password": password,
                        "repeat_password": repeat_password,
                        'age': age,
                        'error': error,
                        'hello': hello,
                        })
        return render(request, 'registration_page.html', context)
    return render(request, 'registration_page.html')


def clear(request):
    return render(request, 'registration_page.html')