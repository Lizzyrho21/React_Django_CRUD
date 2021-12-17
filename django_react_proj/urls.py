from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/students/', include('students.urls'))

]

#   re_path(r'^api/students/$', views.students_list),
#     re_path(r'^api/students/([0-9])$', views.students_detail),