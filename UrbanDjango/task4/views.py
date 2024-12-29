from django.shortcuts import render

# Create your views here.
games_dict = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay2"]}


def func_platform(request):
    return render(request, 'fourth_task/platform.html')


def func_games(request):
    context = {'games_dict': games_dict}
    return render(request, 'fourth_task/games.html', context)


def func_cart(request):
    return render(request, 'fourth_task/cart.html')
