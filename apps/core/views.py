from django.shortcuts import render

from apps.rent.models import Realty


def frontpage(request):
    realties = Realty.objects.all()[0:8]
    return render(request, 'core/index.html', {'realties': realties})

def contact(request):
    return render(request, 'core/contact.html')