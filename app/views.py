from django.shortcuts import render
from django.views.generic import ListView
from .models import User, Task


def task_list(request):
    # Get filter and sorting parameters from the request
    status = request.POST.get('status')
    sort_by = request.POST.get('sort_by')

    print("status", status)
    print("sort_by", sort_by)
    # Filter tasks by status if provided
    if status:
        tasks = Task.objects.filter(status=status)
    else:
        tasks = Task.objects.all()

    # Sort tasks by priority or due date if provided
    if sort_by == 'priority':
        tasks = tasks.order_by('priority')
    elif sort_by == 'due_date':
        tasks = tasks.order_by('due_date')

    status_options = Task.objects.values_list('status', flat=True).distinct()
    priority_options = Task.objects.values_list('priority', flat=True).distinct()
    print("status_options", status_options)
    print("priority_options", priority_options)
    

    context = {
        'tasks': tasks,
        'statuses': status_options,
        'priority_options': priority_options
    }

    return render(request, 'app/task_list.html', context={"tasks": tasks})


