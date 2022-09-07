
from . import views
from django.conf.urls.static import static
from .views import SignUpView
from .views import DeleteView
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

# URLConf
urlpatterns = [
    path('main/', views.ListWithForm.as_view(), name="flower"),
    path('addflower/', views.new_flower),
    path('updateflower/', views.update_flower),
    #path('deleteflower/', views.delete_flower),
    path('flower-delete/<int:pk>/', DeleteView.as_view(), name="flower-delete"),
    path('login_user/', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name="logout"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    path('listflower/', views.flower_list),
]