from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('newflower/', views.new_flower)
]