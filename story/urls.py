from django.urls import path
from . import views

urlpatterns = [
    path('<int:number>/', views.chapter_detail, name='chapter_detail'),
]
