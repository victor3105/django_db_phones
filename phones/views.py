from django.urls import reverse
from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    phone_list = []
    for phone in phones:
        phone_info = {'Name': phone.name, 'Price': phone.price,
                      'Image': phone.image, 'URL': f'{reverse("catalog")}{phone.slug}'}
        phone_list.append(phone_info)
    context = {'phones': phone_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).get()
    phone_info = {'Name': phone.name, 'Price': phone.price,
                  'Image': phone.image, 'Date': phone.release_date,
                  'LTE': phone.lte_exists}
    context = {'phone': phone_info}
    return render(request, template, context)
