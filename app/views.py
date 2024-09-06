from django.shortcuts import render, redirect
from .models import User, Task
from .choices import STATUS
from django.contrib.auth import authenticate, login
from django.contrib import messages


def task_list(request):
    '''
        Displays the Task List from the Database
        according to the filters and sorting based 
        on statuses, priorities and due dates of tasks
        renders template
        - app/task_list.html

    '''
    tasks = Task.objects.all()

    if request.method == 'POST':

        get_status = request.POST.get('status')
        get_sort_by = request.POST.get('sort_by')

        # tasks = Task.objects.all()

        get_status = None if get_status in [None, "None", ""] else get_status
        get_sort_by = None if get_sort_by in [None, "None", ""] else get_sort_by

        if get_status is None and get_sort_by is None:
            return render(request, 'app/task_list.html', context={"tasks": tasks, "render_status": STATUS})
        
        if get_status:
            tasks = Task.objects.filter(status=get_status)
        
        if get_sort_by == 'priority':
            tasks = tasks.order_by('priority')
        
        if get_sort_by == 'due_date':
            tasks = tasks.order_by('due_date')

        return render(request, 'app/task_list.html', context={"tasks": tasks, "render_status": STATUS})
    
    return render(request, 'app/task_list.html', context={"tasks": tasks, "render_status": STATUS} )


def user_login(request):
    if request.method == 'POST':
        get_email = request.POST.get('email')
        get_password = request.POST.get('password')

        user = authenticate(request, username=get_email, password=get_password)

        if user is not None:
            login(request, user)
            return redirect('/task')

    messages.error(request, 'Invalid username or password.')
    return render(request, 'app/login.html')
