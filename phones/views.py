from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    phone_list = []
    for phone in phones:
        phone_info = {'Name': phone.name, 'Price': phone.price,
                      'Image': phone.image, 'Slug': phone.slug}
        phone_list.append(phone_info)
    context = {'phones': phone_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
