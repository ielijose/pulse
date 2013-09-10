from random import choice
frases = ['leonidas esta sentado', 'freddy se fue', 'christian esta arriba']
from django.core.cache import cache
def ejemplo(request):
    frase = cache.get('frase_cool')
    if frase is None:
        frase = choice(frases)
        cache.set('frase_cool', frase)
    return {'frase': frase}

from django.core.urlresolvers import reverse

def menu(request):
    menu = {'menu': [
        {'name': 'Home', 'url': reverse('home')},
        {'name': 'Add', 'url': reverse('add')},
        {'name': 'Acerca de', 'url': reverse('about')},
    ]}
    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu
