from django.urls import path
from . import views

app_name = 'basic_app'


urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('list/<int:pk>/',views.SchoolDetailView.as_view(),name='detail'),
    path('list/', views.SchoolListView.as_view(), name='list'),
    path('create/', views.SchoolCreateView.as_view(),name='create'),
    path('update/<int:pk>', views.SchoolUpdateView.as_view(),name='update'),
     path('delete/<int:pk>/',views.SchoolDeleteView.as_view(),name='delete')
]
