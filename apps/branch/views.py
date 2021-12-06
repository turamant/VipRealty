from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify

from apps.branch.forms import RealtyForm
from apps.branch.models import Staff, Branch
from apps.rent.models import Realty
from apps.thesaurus.models import Street, City

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


#####################################   branch ################

def become_branch(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            branch = Branch.objects.create(name=user.username, created_by=user)

            return redirect('core:frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'branch/become_branch.html', {'form': form})

@login_required
def branch_admin(request):
    branch = request.user.branch
    realties = branch.realties.all()

    return render(request, 'branch/branch_admin.html',
                  {'branch': branch, 'realties': realties})


@login_required
def add_realty(request):
    if request.method == 'POST':
        form = RealtyForm(request.POST, request.FILES)
        if form.is_valid():
            realty = form.save(commit=False)
            realty.branch_number = request.user.branch
            realty.slug = slugify(realty.realty_number)
            realty.save()

            return redirect('branch:branch_admin')
    else:
        form = RealtyForm()

    return render(request, 'branch/add_realty.html',
                  {'form': form})

@login_required
def edit_realty(request, category_slug, slug):
    realty = Realty.objects.get(slug=slug)
    form = RealtyForm(instance=realty)
    if request.method == 'POST':
        form = RealtyForm(request.POST,  request.FILES, instance=realty)
        if form.is_valid():
            realty = form.save(commit=False)
            realty.branch_number = request.user.branch
            realty.slug = slugify(realty.realty_number)
            realty.save()
            return redirect('branch:branch_admin')
    return render(request, 'branch/edit_realty.html', {'form': form, 'realty': realty})

@login_required
def delete_realty(request, category_slug, slug):
    realty = Realty.objects.get(slug=slug)
    if request.method == 'POST':
        if "cancel" in request.POST:
            return redirect('branch:branch_admin')
        realty.delete()
        return redirect('branch:branch_admin')
    return render(request, 'branch/delete_realty.html', {'realty': realty})

def branch_list(request):
    branchs = Branch.objects.all()
    return render(request, 'branch/branch_list.html', {'branchs': branchs})

def branch_detail(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    realties = branch.realties.all()
    context = {'branch': branch, 'realties': realties}

    return render(request, 'core/index.html', context)
