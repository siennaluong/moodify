from django.urls import path
from .views import HomeView, ActivityView, ActivityAdd
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('activities', ActivityView.as_view(), name='activity'),
    path('add', ActivityAdd.as_view(), name='add'),
    path('summary', views.summary,name='summary')
]