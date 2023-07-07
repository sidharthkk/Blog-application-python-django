from django.urls import path
from myapp import views

urlpatterns = [
    path('home', views.project_view, name='project_view'),
    path('newpost',views.newpost_view,name='project_view'),
    path('addpost/', views.addpost, name='addpost'),
    path('homeview',views.home_view,name='viewpost'),
    path('<int:pk>/', views.delete_project, name="delete"),
]