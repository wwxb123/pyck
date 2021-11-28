from django.urls import path
from projects import views

app_name = 'projects'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.projects_list, name='list'),
    path('create/', views.ProjectCreateView.as_view(), name='create'),
    path('update/<int:pk>/',views.ProjectUpadateView.as_view(),name='update'),
    # path('delete/<int:pk>/',views.ProjectDeleteView.as_view(),name='delete'),
    path('delete/<int:pk>/',views.project_deltete,name='delete'),

]
