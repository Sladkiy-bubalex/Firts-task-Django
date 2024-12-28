from django.shortcuts import render

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


def view_ingridients(request):
    template = 'calculator/index.html'
    count = request.GET.get('servings')
    
    recipes = {
        '/omlet/': DATA['omlet'],
        '/pasta/': DATA['pasta'],
        '/buter/': DATA['buter']
    }
    recipe = recipes.get(request.path)
    context = {'recipe': recipe.copy()}

    if count is None:
        return render(request, template, context)
    
    elif count is not None:
        for key, item in context['recipe'].items():
            item *= int(count)
            context['recipe'][key] = round(item, 2)
        return render(request, template, context)