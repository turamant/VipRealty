from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from apps.orders.forms import OrderModelForm
from apps.rent.forms import RealtyFilterForm, LeaseCreateForm
from apps.rent.models import Realty, Lease


def main_rent(request):
    return render(request, 'rent/main_rent_page.html')

def listview_realties(request):
    realties = Realty.objects.filter(rent_status__exact='free')
    num_realty_free = Realty.objects.filter(rent_status__exact='free').count()
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


def detail_realty(request, id):
    realty = get_object_or_404(Realty, id=id)
    form = OrderModelForm(request.POST or None, initial={
        'realty': realty
    })
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("{}?sended=True".format(reverse('rent:detail_realty',
                                                            kwargs={"id": realty.id})))
    context = {'realty': realty,
               'form': form,
               'sended': request.GET.get("sended", False)}
    return render(request, 'rent/detail_realty.html', context)


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
