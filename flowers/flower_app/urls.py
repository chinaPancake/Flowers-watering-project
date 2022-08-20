from django.urls import path
from . import views
from django.conf.urls.static import static
from .views import SignUpView

# URLConf
urlpatterns = [
    path('main/', views.main, name="main"),
    path('addflower/', views.new_flower),
    path('updateflower/', views.update_flower),
    path('deleteflower/', views.delete_flower),
    path('login_user/', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name="logout"),
    path('signup/', SignUpView.as_view(), name='signup')
    #('createuser/', views.createUser),
]
