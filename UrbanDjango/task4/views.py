from django.shortcuts import render


# Create your views here.
def platform(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'platform.html', context)


def games(request):
    title = 'Игры'
    list_of_games = ['Atomic Heart', "Cyberpunk 2077", "Pay Day2"]
    context = {
        'list_of_games': list_of_games,
        'title': title
    }
    return render(request, 'games.html', context)


def cart(request):
    title = 'Корзина'
    context = {
        'title': title,
    }
    return render(request, 'cart.html', context)







