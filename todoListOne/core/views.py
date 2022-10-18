from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Task
from .forms import TaskForm, UpdateForm


# Create your views here.
def home(request):
    context = {}
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    tasks = Task.objects.all()

    context['form'] = form
    context['tasks'] = tasks
    return render(request, 'core/home.html', context)


def edit_task(request, id):
    context = {}
    task = get_object_or_404(Task, id=id)
    form = UpdateForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    context['form'] = form

    return render(request, 'core/edit_task.html', context)


def completed(request, id):
    task = get_object_or_404(Task, id=id)
    if not task.completed:
        task.completed = True
        task.save()

    return HttpResponseRedirect('/')


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return HttpResponseRedirect('/')


def filter_priority(request, choice):
    context = {}
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    tasks = Task.objects.filter(priority=choice)

    context['form'] = form
    context['tasks'] = tasks
    return render(request, 'core/home.html', context)


def filter_status(request, choice):
    context = {}
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    tasks = Task.objects.filter(completed=choice)

    context['form'] = form
    context['tasks'] = tasks
    return render(request, 'core/home.html', context)
