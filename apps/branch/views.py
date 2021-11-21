from django.db.models import Sum
from django.shortcuts import render, get_object_or_404

from apps.branch.models import Staff


def listview_staff(request):
    staff = Staff.objects.all()
    salary_all = Staff.objects.aggregate(Sum('salary'))
    context = {'staff': staff, 'salary_all': salary_all}
    return render(request, 'branch/list_staff.html', context)

def detail_staff(request, pk):
    person = get_object_or_404(Staff, pk=pk)
    context = {'person': person}
    return render(request, 'branch/detail_staff.html', context)