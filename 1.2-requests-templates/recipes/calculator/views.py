from django.shortcuts import render, reverse
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipes_handler(request):

    links = {
        'Омлет': reverse('omlet'),
        'Макароны': reverse('pasta'),
        'Бутерброд': reverse('buter')
    }

    return HttpResponse(
        "<br>".join(f"<a href='{link}'>{name}</a>" for name, link in links.items()))


def recipes(request):

    path = request.path[1:-1]
    recipe = DATA[path]

    servings = int(request.GET.get('servings', 1))

    recipe = {key: value * servings for key, value in recipe.items()}

    context = {
      'recipe': recipe
    }

    return render(request, 'calculator/index.html', context)
