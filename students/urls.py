from django.urls import path
from . import views
urlpatterns = [
  path('', views.students_list, name='students_list'),
  path('<int:pk>/', views.students_detail, name="students_detail")
]


