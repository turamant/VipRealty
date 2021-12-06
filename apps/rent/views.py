import random

from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from apps.orders.forms import OrderModelForm
from apps.rent.forms import RealtyFilterForm, LeaseCreateForm, ViewingCreateForm, ClientCreateForm
from apps.rent.models import Realty, Lease, Viewing, Client
from apps.thesaurus.models import Category


def search(request):
    query = request.GET.get('query', '')
    realties = Realty.objects.filter(Q(description__icontains=query))

    return render(request, 'rent/search.html', {'realties': realties, 'query': query})

def main_rent(request):
    ''' использую '''
    return render(request, 'rent/main_rent_page.html')


def category(request, category_slug):
    ''' использую '''
    category = get_object_or_404(Category, slug=category_slug)
    realties = category.realties.all()
    form = RealtyFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['type_realty']:
            realties = realties.filter(type_realty__name=form.cleaned_data['type_realty'])
        if form.cleaned_data['min_rent']:
            realties = realties.filter(rent__gte=form.cleaned_data['min_rent'])
        if form.cleaned_data['max_rent']:
            realties = realties.filter(rent__lte=form.cleaned_data['max_rent'])
        if form.cleaned_data['min_rooms']:
            realties = realties.filter(rooms__gte=form.cleaned_data['min_rooms'])
        if form.cleaned_data['max_rooms']:
            realties = realties.filter(rooms__lte=form.cleaned_data['max_rooms'])

        if form.cleaned_data['ordering']:
            realties = realties.order_by(form.cleaned_data['ordering'])

    context = {'category': category, 'realties': realties, 'form': form}
    return render(request, 'rent/category.html', context)


def realty(request, category_slug, realty_slug):
    ''' использую '''
    realty = get_object_or_404(Realty, category__slug=category_slug, slug=realty_slug)
    viewings = realty.viewings.all()

    if request.method == 'POST':
        viewings_form = ViewingCreateForm(request.POST)
        if viewings_form.is_valid():
            viewings_form.save()
            return redirect("{}?sended=True".format(reverse('rent:realty',
                                                            kwargs={"category_slug": category_slug,
                                                                    "realty_slug": realty.slug})))
    else:
        viewings_form = ViewingCreateForm()

    form = OrderModelForm(request.POST or None, initial={
        'realty': realty
    })
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("{}?sended=True".format(reverse('rent:realty',
                                                            kwargs={"category_slug": category_slug,
                                                                    "realty_slug": realty.slug})))

    similar_realties = list(realty.category.realties.exclude(id=realty.id))


    if len(similar_realties) >= 4:
        similar_realties = random.sample(similar_realties, 4)

    context = {'realty': realty,
               'viewings': viewings,
               'similar_realties': similar_realties,
               'form': form,
               'viewings_form': viewings_form,
               'sended': request.GET.get("sended", False)}
    return render(request, 'rent/detail_realty.html', context)

#######################################

def detail_realty(request, id):
    realty = get_object_or_404(Realty, id=id)
    viewings = realty.viewings.all()

    if request.method == 'POST':
        viewings_form = ViewingCreateForm(request.POST)
        if viewings_form.is_valid():
            viewings_form.save()
            return redirect("{}?sended=True".format(reverse('rent:detail_realty',
                                                            kwargs={"id": realty.id})))
    else:
        viewings_form = ViewingCreateForm()


    form = OrderModelForm(request.POST or None, initial={
        'realty': realty
    })
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("{}?sended=True".format(reverse('rent:detail_realty', kwargs={"id": realty.id})))

    similar_realties = list(realty.category.realties.exclude(id=realty.id))

    if len(similar_realties) >= 4:
        similar_realties = random.sample(similar_realties, 4)

    context = {'realty': realty,
               'similar_realties': similar_realties,
               'viewings': viewings,
               'form': form,
               'viewings_form': viewings_form,
               'sended': request.GET.get("sended", False)}
    return render(request, 'rent/detail_realty.html', context)
#############################################################################


def listview_realties(request):
    if request.user.is_superuser:
        realties = Realty.objects.all()
        num_realty_free = Realty.objects.filter(rent_status__exact='free').count()
    else:
        realties = Realty.objects.filter(rent_status__exact='free')
        num_realty_free = None
    form = RealtyFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['min_rent']:
            realties= realties.filter(rent__gte=form.cleaned_data['min_rent'])
        if form.cleaned_data['max_rent']:
            realties = realties.filter(rent__lte=form.cleaned_data['max_rent'])
        if form.cleaned_data['min_rooms']:
            realties = realties.filter(rooms__gte=form.cleaned_data['min_rooms'])
        if form.cleaned_data['max_rooms']:
            realties = realties.filter(rooms__lte=form.cleaned_data['max_rooms'])

        if form.cleaned_data['ordering']:
            realties = realties.order_by(form.cleaned_data['ordering'])

    context = {'realties': realties, 'form': form, 'num_realty_free': num_realty_free}
    return render(request, 'rent/list_realties.html', context)



def create_lease(request):
    leases = Lease.objects.all()
    if request.method == 'POST':
        form = LeaseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rent:list_leases')
    else:
        form = LeaseCreateForm()
    context = {'form': form, 'leases': leases}
    return render(request, 'rent/create_lease.html', context)

def listview_leases(request):
    leases = Lease.objects.all()[:100]
    context = {'leases': leases}
    return render(request, 'rent/list_leases.html', context)

def detail_lease(request, pk):
    lease = Lease.objects.get(pk=pk)
    context = {'lease': lease}
    return render(request, 'rent/detail_lease.html', context)


def list_clients(request):
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'rent/list_clients.html', context)

def detail_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    context = {'client': client}
    return render(request, 'rent/detail_client.html', context)

def create_client(request):
    clients = Client.objects.all()
    if request.method == 'POST':
        form = ClientCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rent:list_clients')
    else:
        form = ClientCreateForm()
    context = {'clients': clients, 'form': form}
    return render(request, 'rent/create_client.html', context)
