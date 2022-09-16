from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import Item
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView,FormView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskForm
from django.views.generic.detail import DetailView


class TaskList(ListView):
    model = Item
    context_object_name = 'tasks'
    template_name: str = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['tasks'] = context['tasks'].filter(user=self.request.user)
        # context['count'] = context['tasks'].filter(complete=False).count()
        if self.request.user.is_authenticated:
            context['tasks'] = context['tasks'].filter(user=self.request.user)
        

        # search_input = self.request.GET.get('search-area') or ''
        # if search_input:
        #     context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        # context['search_input'] = search_input
        return context

class RegisterPage(FormView):
    template_name: str = 'app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('list-view')


    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)
    
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('list-view')
        return super(RegisterPage,self).get(*args,**kwargs)


class LoginPage(LoginView):
    template_name: str = 'app/login.html'
    fields = ['username','password']
    redirect_authenticated_user: bool = True

    def get_success_url(self) -> str:
        return reverse_lazy('list-view')
    
def logoutPage(request):
    logout(request)
    return redirect('list-view')

class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Item
    context_object_name = 'task'
    success_url = reverse_lazy('list-view')

class CreateTask(LoginRequiredMixin,CreateView):
    model = Item
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('list-view')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask,self).form_valid(form)
    
   
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('list-view')


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Item
    context_object_name = 'task'
    template_name = 'base/task.html'