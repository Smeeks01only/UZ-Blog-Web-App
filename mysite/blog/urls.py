from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='homepage'),
    path('fixtures', views.fixtures, name='fixturespage'),
    
    path('<slug:post>/', views.post_single, name='post_single')
    
    
]