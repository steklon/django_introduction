from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_list = Phone.objects.all()
    phones = phones_list
    get_sort = request.GET.get('sort', '')

    if get_sort == 'name':
        phones = phones_list.order_by('name')
    elif get_sort == 'min_price':
        phones = phones_list.order_by('price')
    elif get_sort == 'max_price':
        phones = phones_list.order_by('-price')

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
