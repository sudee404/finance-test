from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/', views.signin, name='login'),
    path('register/', views.signup, name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('add/',views.add_income,name='add-income'),
    path('edit/',views.get_income,name='edit-income'),
    path('update/',views.update_income,name='update-income'),
    path('delete/',views.delete_income,name='delete-income'),
    path('plots/',views.get_plots,name='get-plots'),
]
