from django.urls import path

from users import views
app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('reg/', views.reg, name='reg'),
    path('profile/', views.profile, name='profile'),
    
]