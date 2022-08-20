

from . import views
from django.conf.urls.static import static
from .views import SignUpView
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

# URLConf
urlpatterns = [
    path('main/', views.main, name="main"),
    path('addflower/', views.new_flower),
    path('updateflower/', views.update_flower),
    path('deleteflower/', views.delete_flower),
    path('login_user/', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name="logout"),
    path('signup/', SignUpView.as_view(), name='signup')
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
   # ('createuser/', views.createUser),
]