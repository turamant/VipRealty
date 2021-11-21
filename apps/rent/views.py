from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from apps.orders.forms import OrderModelForm
from apps.rent.forms import PropertyFilterForm
from apps.rent.models import Property, Lease


def main_rent(request):
    return render(request, 'rent/main_rent_page.html')

def listview_property(request):
    _property = Property.objects.all()
    form = PropertyFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['min_rent']:
            _property = _property.filter(rent__gte=form.cleaned_data['min_rent'])
        if form.cleaned_data['max_rent']:
            _property = _property.filter(rent__lte=form.cleaned_data['max_rent'])
        if form.cleaned_data['min_rooms']:
            _property = _property.filter(rooms__gte=form.cleaned_data['min_rooms'])
        if form.cleaned_data['max_rooms']:
            _property = _property.filter(rooms__lte=form.cleaned_data['max_rooms'])

        if form.cleaned_data['ordering']:
            _property = _property.order_by(form.cleaned_data['ordering'])

    context = {'property': _property, 'form': form}
    return render(request, 'rent/list_property.html', context)

def listview_leases(request):
    leases = Lease.objects.all()
    context = {'leases': leases}
    return render(request, 'rent/list_leases.html', context)

def detail_property(request, id):
    real = get_object_or_404(Property, id=id)
    form = OrderModelForm(request.POST or None, initial={
        '_property': real
    })
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("{}?sended=True".format(reverse('rent:detail_property',
                                                            kwargs={"id": real.id})))
    context = {'real': real,
               'form': form,
               'sended': request.GET.get("sended", False)}
    return render(request, 'rent/detail_property.html', context)

def detail_lease(request, pk):
    lease = Lease.objects.get(pk=pk)
    context = {'lease': lease}
    return render(request, 'rent/detail_lease.html', context)
