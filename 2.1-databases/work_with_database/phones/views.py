from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    catalog_sort = request.GET.get('sort')
    if catalog_sort == 'name':
        all_phones = Phone.objects.all().order_by('name')
    elif catalog_sort == 'min_price':
        all_phones = Phone.objects.all().order_by('price')
    elif catalog_sort == 'max_price':
        all_phones = Phone.objects.all().order_by('-price')
    else:
        all_phones = Phone.objects.all()
        
    context = {'phones': all_phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).first()
    context = {'phone': phone}
    return render(request, template, context)
