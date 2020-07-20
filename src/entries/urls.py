from . import views
from django.urls import path

app_name = 'entries'
urlpatterns = [
    path('', views.entry_view, name='entries'),
    
    path('create/', views.log_create_view, name='create'),
    path('<int:id>/', views.update_view, name='update'),
    path('<int:id>/delete/', views.delete_view, name='delete')
    
    
]