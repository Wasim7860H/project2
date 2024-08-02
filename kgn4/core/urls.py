from django. urls import path
from . import views

urlpatterns = [
    path('stulist/', views.stu_list),
    
    
]
