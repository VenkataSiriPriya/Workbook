from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TodoItem
from .forms import TodoItemForm

@login_required
def task_list(request):
    tasks = TodoItem.objects.filter(user=request.user)
    filter_status = request.GET.get('status')
    if filter_status == 'completed':
        tasks = tasks.filter(completed=True)
    elif filter_status == 'pending':
        tasks = tasks.filter(completed=False)

    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TodoItemForm()
    return render(request, 'add_task.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(TodoItem, id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')

@login_required
def mark_task(request, task_id):
    task = get_object_or_404(TodoItem, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
