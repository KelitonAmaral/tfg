from django.conf.urls import url

from .views import UserListView, UserCreateView
from .views import UserUpdateView, UserDeleteView
from .views import UserRegisterView, UserRegisterSuccessView, UserRegisterActivateView

urlpatterns = [
	url(r'list/$', UserListView.as_view(), name='users_list'),
	url(r'registration/$', UserCreateView.as_view(), name='users_create'),
	url(r'(?P<pk>\d+)/$', UserUpdateView.as_view(), name='users_update'),
	url(r'(?P<pk>\d+)/delete/$', UserDeleteView.as_view(), name='users_delete'),
	url(r'register/success/',UserRegisterSuccessView.as_view(),name='users_register_success'),
	url(r'register/(?P<slug>[-\w\d]+)/activate/', UserRegisterActivateView.as_view(), name='users_register_activate'),
	url(r'register', UserRegisterView.as_view(), name='users_register'),
]
