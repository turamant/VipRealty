from django.db.models import Sum
from django.shortcuts import render, get_object_or_404

from apps.branch.models import Staff


LIMIT = 2


class ExceededLimit(BaseException):
    def __init__(self, LIMIT):
        self.LIMIT = LIMIT
    def __str__(self):
        return repr(self.LIMIT)


def listview_staff(request):
    staff = Staff.objects.all()[:(LIMIT + 1)]
    if len(staff) > LIMIT:
        try:
            raise ExceededLimit(LIMIT)
        except ExceededLimit as e:
            return render(request, 'branch/limit.html')
    if request.user.is_superuser:
        salary_all = Staff.objects.aggregate(Sum('salary'))
        salary_sum = salary_all['salary__sum']
        context = {'staff': staff, 'salary_sum': salary_sum}
    else:
        context = {'staff': staff}
    return render(request, 'branch/list_staff.html', context)

def listview_salary_staff(request):
    staff = Staff.objects.all().only('staff_number', 'first_name', 'last_name', 'salary')[:(LIMIT + 1)]
    if len(staff) > LIMIT:
        try:
            raise ExceededLimit(LIMIT)
        except ExceededLimit as e:
            return render(request, 'branch/limit.html')
    salary_all = Staff.objects.aggregate(Sum('salary'))
    salary_sum = salary_all['salary__sum']
    context = {'staff': staff, 'salary_sum': salary_sum}
    return render(request, 'branch/salary_staff.html', context)

def detail_staff(request, pk):
    person = get_object_or_404(Staff, pk=pk)
    context = {'person': person}
    return render(request, 'branch/detail_staff.html', context)