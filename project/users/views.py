from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse

from django.views.generic import ListView, TemplateView, DetailView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from mail_templated import EmailMessage

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin

from .models import User
from .forms import UserRegisterForm


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/users_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     if self.request.GET:
    #         #quando ja tem dado filtrando
    #         context['form'] = SearchUserForm(data=self.request.GET)
    #     else:
    #         #quando acessa sem dado filtrando
    #         context['form'] = SearchUserForm()
    #     return context

    # def get_queryset(self):
    #     qs = User.objects.all()

    #     if self.request.GET:
    #         #quando ja tem dado filtrando
    #         form = SearchUserForm(data=self.request.GET)
    #     else:
    #         #quando acessa sem dado filtrando
    #         form = SearchUserForm()

    #     if form.is_valid():
    #         name = form.cleaned_data.get('name')
    #         type = form.cleaned_data.get('type')

    #         if name:
    #             qs = qs.filter(name__icontains=name)

    #         if type:
    #             qs = qs.filter(type=type)
    #     return qs
    
    
class UserCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = User
    fields = ['type', 'name', 'email', 'password', 'cpf', 'phone', 'birth_date', 'gender', 'is_active']
    success_url = 'users_list'
    
    def get_success_url(self):
        messages.success(self.request, 'User successfully registered on the platform!')
        return reverse(self.success_url)


class UserUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = User
    fields = ['type', 'name', 'email', 'cpf', 'phone', 'birth_date', 'gender', 'is_active']
    # template_name = 'users/user_form_update.html'
    success_url = 'users_list'
    
    def get_success_url(self):
        messages.success(self.request, 'User data successfully updated on the platform!')
        return reverse(self.success_url)


class UserDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = User
    success_url = 'users_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except Exception as e:
            messages.error(request, 'There are dependencies attached to this user, permission denied!')
        return redirect(self.success_url)


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/users_register_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(UserRegisterView, self).form_valid(form)
    
    def get_success_url(self):
        message = EmailMessage('users/email/validation_email.html', {'user': self.object},
                               settings.EMAIL_HOST_USER, to=[self.object.email])
        message.send()     
        return reverse('users_register_success')


class UserRegisterSuccessView(TemplateView):
    template_name= 'users/users_register_success.html'


class UserRegisterActivateView(RedirectView):
    models = User

    def get_redirect_url(self, *args, **kwargs):
        self.object = User.objects.get(slug=kwargs.get('slug'))
        self.object.is_active = True
        self.object.save()
        login(self.request, self.object)
        messages.success(self.request, 'Thank you for accessing the platform. This is your restricted area.')
        return reverse('home')