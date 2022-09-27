from email import charset
import string
from django.urls import reverse
from multiprocessing.sharedctypes import Value
from django.shortcuts import render, redirect
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator


from mainapp.models import teacher_extra
from . import views
from .models import admin_extra, answers, question, student_extra
from django.contrib.auth.models import Group, User
from django.http import HttpRequest, HttpResponse
from django.http import HttpResponseRedirect
from .forms import studentFORM, studentextraForm, teacherFORM, teacherextraForm, adminextraForm, adminFORM, quationForm, answerForm, profileForm, sprofileform
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.


def home(request):
    return redirect('login')


def student_signup(request):
    form = studentFORM()
    form1 = studentextraForm()
    mydict = {'form1': form1, 'form': form}
    if request.method == 'POST':
        form = studentFORM(request.POST)
        form1 = studentextraForm(request.POST, request.FILES)

        if form1.is_valid() and form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            f = form1.save(commit=False)
            f.user = user
            user2 = f.save()

            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
            print("user created")
            return HttpResponseRedirect('login')
    return render(request, 'student_signup.html', context=mydict)


def admin_signup(request):
    form = adminFORM()
    form1 = adminextraForm()
    mydict = {'form1': form1, 'form': form}
    if request.method == 'POST':
        form = adminFORM(request.POST)
        form1 = adminextraForm(request.POST, request.FILES)

        if form1.is_valid() and form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            f = form1.save(commit=False)
            f.user = user
            user2 = f.save()

            my_student_group = Group.objects.get_or_create(name='ADMIN')
            my_student_group[0].user_set.add(user)
            print("user created")
            return HttpResponseRedirect('login')
    return render(request, 'admin_signup.html', context=mydict)


def teacher_signup(request):
    form = teacherFORM()
    form1 = teacherextraForm()
    mydict = {'form1': form1, 'form': form}
    if request.method == 'POST':
        form = teacherFORM(request.POST)
        form1 = teacherextraForm(request.POST, request.FILES)

        if form1.is_valid() and form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            f = form1.save(commit=False)
            f.user = user
            user2 = f.save()

            my_student_group = Group.objects.get_or_create(name='TEACHER')
            my_student_group[0].user_set.add(user)
            print("user created")
            return HttpResponseRedirect('login')
    return render(request, 'teacher_signup.html', context=mydict)


def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()


def is_teacher(user):

    return user.groups.filter(name='TEACHER').exists()


def is_student(user):
    return user.groups.filter(name='STUDENT').exists()


def loginchecker(request):
    if is_admin(request.user):
        return redirect('admin_page')
    elif is_student(request.user):
        return redirect('studentpage')

    elif is_teacher(request.user):
        accountapproved = teacher_extra.objects.all().filter(
            user_id=request.user.id, active=True)
        if accountapproved:
            return redirect('teacher_page')
        else:
            return render(request, 'wait.html')
    else:
        return redirect('login')


@login_required(login_url='login')
@user_passes_test(is_student)
def student_page(request):
    form = quationForm()
    d = question.objects.all().annotate(ans_count=Count('answers'))
    p = student_extra.objects.all().filter(user_id=request.user.id)
    pag = Paginator(question.objects.all().order_by(
        '-date').annotate(ans_count=Count('answers')), 8)
    page = request.GET.get('page')
    quest = pag.get_page(page)

    mydict = {'form': form, 'd': d, 'p': p, 'questions': quest}
    if request.method == 'POST':
        form = quationForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            g = student_extra.objects.all().filter(user_id=request.user.id)
            for g in g:
                f.user = g
            quastion = f.save()

    return render(request, 'student_page.html', context=mydict)


def searched_page(request):
    if request.method == "POST":

        searched = request.POST['search']
        if searched:
            p = student_extra.objects.all().filter(user_id=request.user.id)

            questions = question.objects.all().order_by(
                '-date').filter(Title__contains=searched).annotate(ans_count=Count('answers'))
            mydict = {'searched': searched, 'questions': questions, 'p': p}
            return render(request, 'search.html', context=mydict)
        else:
            return redirect('studentpage')

    else:
        return redirect('studentpage')


@login_required(login_url='login')
@user_passes_test(is_student)
def profile(request):
    form = profileForm(instance=request.user)
    user = student_extra.objects.all().filter(user=request.user)
    for user in user:
        users = user
    form1 = sprofileform(instance=users)
    mydict = {'form1': form1, 'form': form, 'p': users}
    if request.method == 'POST':
        form = profileForm(request.POST, instance=request.user)
        form1 = sprofileform(request.POST, request.FILES,
                             instance=users)

        if form1.is_valid() and form.is_valid():
            form.save()

            form1.save()

    return render(request, 'profile.html', context=mydict)


def admin_page(request):
    return render(request, 'admin_page.html')


def teacher_page(request):
    return render(request, 'teacher_page.html')


def likes(request, id):

    post = answers.objects.all().filter(pk=id)

    for r in post:
        if r.likes.filter(id=request.user.id).exists():
            r.likes.remove(request.user)
            liked = True
        else:
            r.likes.add(request.user)
            print('notworks')
            liked = False
        questi = r.quation.id

    return redirect(reverse('detail', args=[str(questi)]))


@login_required(login_url='login')
@user_passes_test(is_student)
def detail(request, id):
    form = answerForm()

    p = student_extra.objects.all().filter(user_id=request.user.id)

    questio = question.objects.all().filter(pk=id)
    for r in questio:
        answe = answers.objects.all().filter(quation=r)
        an = answers.objects.filter(Q(likes__exact=request.user), quation=r)

    studen = student_extra.objects.all()
    teacher = teacher_extra.objects.all()
    admin = admin_extra.objects.all()

    if request.method == 'POST':
        form = answerForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            q = question.objects.all().filter(pk=id)
            for q in q:
                f.quation = q
            f.user = request.user
            quastion = f.save()

    mydict = {'d': answe, 'form': form, 'q': questio,
              'p': p, 's': studen, 'T': teacher, 'an': an, 'a': admin}
    return render(request, 'student_answer.html', context=mydict)


@login_required(login_url='login')
@user_passes_test(is_student)
def contact(request):
    p = student_extra.objects.all().filter(user_id=request.user.id)
    mydict = {
        'p': p}
    return render(request, template_name='contact-us.html', context=mydict)
