from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import TaskManager, Category, Priority, Completed
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .forms import TaskForm, UserRegisterForm, UserLoginForm, FinishForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.contrib.auth import login, logout
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.db.models import Q


# @login_required
# def favourite_list(request):
#     new = TaskManager.objects.filter(favourites=request.user)
#     context = {
#         'new': new,
#     }
#     return render(request, 'taskmanager/favourites.html', context)
#
#
# @login_required
# def favourite_add(request, task_id):
#     post = get_object_or_404(TaskManager, pk=task_id)
#     if post.favourites.filter(pk=request.user.id).exists():
#         post.favourites.remove(request.user)
#     else:
#         post.favourites.add(request.user)
#     return redirect('home')


class FavouriteTask(TaskManager, ListView):
    def get(self, request, task_id):
        task = TaskManager.objects.get(pk=task_id)
        bound_form = TaskForm(instance=task)
        context = {
            'form': bound_form,
            'task': task
        }
        return render(request, 'taskmanager/favourite_no.html', context)

    def post(self, request, task_id):
        task = TaskManager.objects.get(pk=task_id)
        bound_form = TaskForm(request.POST, instance=task)
        context = {
            'form': bound_form,
            'task': task
        }
        if bound_form.is_valid():
            new_task = bound_form.save()
            return redirect(new_task)
        return render(request, 'taskmanager/favourite_no.html', context)

class TaskUpdate(TaskManager, ListView):
    def get(self, request, task_id):
        task = TaskManager.objects.get(pk=task_id)
        bound_form = TaskForm(instance=task)
        context = {
            'form': bound_form,
            'task': task
        }
        return render(request, 'taskmanager/update.html', context)

    def post(self, request, task_id):
        task = TaskManager.objects.get(pk=task_id)
        bound_form = TaskForm(request.POST, instance=task)
        context = {
            'form': bound_form,
            'task': task
        }
        if bound_form.is_valid():
            new_task = bound_form.save()
            return redirect(new_task)
        return render(request, 'taskmanager/update.html', context)




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешна')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')

    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'taskmanager/register.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'taskmanager/login.html', context)


class TagDelete(TaskManager, ListView):
    def get(self, request, task_id):
        task = TaskManager.objects.get(pk=task_id)
        return render(request, 'taskmanager/tag_delete.html', context={'task': task})

    def post(self, request, task_id):
        task = TaskManager.objects.get(pk=task_id)
        task.delete()
        return redirect(reverse('home'))



# @require_http_methods(['POST'])
# def delete(request, todo_id):

#     # return redirect('home')
#     # form = TaskForm()
#     # context = {
#     #     # 'form': form
#     #     'todo_delete': todo_delete
#     # }
#     return redirect('home')

    # return render(request, 'taskmanager/tag_delete.html', context)

# def update(request, taskmanager_id):
#     update_task = TaskManager.objects.get(id=taskmanager_id)
#     update_task.completed = not update_task.completed
#     update_task.save()
#     return redirect('index')

# def search(request):
#     search_query = request.GET.get('search', '')
#     if search_query:
#         task_manager = TaskManager.objects.filter(title__icontains=search_query)
#     else:
#         task_manager = TaskManager.objects.all()
#
#     context = {
#         'taskmanager': task_manager,
#     }
#     return render(request, 'taskmanager/index.html', context)

class HomeTaskManager(ListView):
    model = TaskManager
    template_name = 'taskmanager/index.html'
    context_object_name = 'taskmanager'
    extra_context = {'title': "Менеджер задач"}
    paginate_by = 2

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Менеджер задач'

        # context['title'] = self.get_upper('Список новостей')
        return context


def search(request):
    search_query = request.GET.get('search', '')
    if search_query:
        task_manager = TaskManager.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
    else:
        task_manager = TaskManager.objects.all()

    context = {
        'taskmanager': task_manager,
    }
    return render(request, 'taskmanager/search.html', context)

def get_category(request, category_id):
    task_manager = TaskManager.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)

    context = {
        'taskmanager': task_manager,
        'category': category,

    }
    return render(request, 'taskmanager/category.html', context)

def get_favourite(request, favourite_id):
    task_manager = TaskManager.objects.filter(favourite_id=favourite_id)
    favourite = Category.objects.get(pk=favourite_id)

    context = {
        'taskmanager': task_manager,
        'favourite': favourite,

    }
    return render(request, 'taskmanager/favourite.html', context)
def get_priority(request, priority_id):
    task_manager = TaskManager.objects.filter(priority_id=priority_id)
    priority = Priority.objects.get(pk=priority_id)


    context = {
        'taskmanager': task_manager,
        'priority': priority,


    }
    return render(request, 'taskmanager/priority.html', context)

def completed(request, completed_id):
    task_manager = TaskManager.objects.filter(completed_id=completed_id)
    completed = Completed.objects.get(pk=completed_id)


    context = {
        'taskmanager': task_manager,
        'completed': completed,


    }
    return render(request, 'taskmanager/completed.html', context)


def view_task(request, task_id):
    task_item = TaskManager.objects.get(pk=task_id)
    context = {
        'task_item': task_item
    }
    return render(request, 'taskmanager/view_task.html', context)

# @require_http_methods(['POST'])
# def add(request):
#     title = request.POST['title']
#     tasks = TaskManager(title=title,)
#     tasks.save()
#     return redirect('index')
#
# def update(request, tasks_id):
#     tasks = TaskManager.objects.get(id=tasks_id)
#     tasks.completed_at = not tasks.completed_at
#     tasks.save()
#     return redirect('index')
#
#
# def delete(request, tasks_id):
#     tasks = TaskManager.objects.get(id=tasks_id)
#     tasks.delete()
#     return redirect('index')

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # tasks = TaskManager.objects.create(**form.cleaned_data)
            tasks = form.save(commit=False)
            tasks.user = request.user
            tasks = form.save()
            # tasks = form.save(commit=False)


            return redirect(tasks)
    else:
        form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'taskmanager/add_task.html', context)

# def finish(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             tasks = form.save()
#             # tasks = form.save()
#             return redirect(tasks)
#     else:
#         form = TaskForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'taskmanager/add_task.html', context)

class FinishTask(TaskManager, ListView):
    def get(self, request, task_id):
        task = TaskManager.objects.get(pk=task_id)
        bound_form = FinishForm(instance=task)
        context = {
            'form': bound_form,
            'task': task
        }
        return render(request, 'taskmanager/finish_task.html', context)

    def post(self, request, task_id):
        task = TaskManager.objects.get(pk=task_id)
        bound_form = FinishForm(request.POST, instance=task)
        context = {
            'form': bound_form,
            'task': task
        }
        if bound_form.is_valid():
            new_task = bound_form.save()
            return redirect(new_task)
        return render(request, 'taskmanager/finish_task.html', context)