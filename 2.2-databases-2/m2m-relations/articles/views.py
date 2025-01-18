from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.prefetch_related().all()

    for article in object_list:
        print(article.title)
        for scope in article.scopes.all():
            print(scope.tag.name, scope.is_main)
    context = {
        'object_list': object_list
    }

    return render(request, template, context)
