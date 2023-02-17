
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index),
    path('form_data',views.form_data,name='form'),
    path('login_form',views.login_form),
    path('login',views.login,name='login'),
    # path('table',views.table,name='table'),
    path('del',views.delete,name='delete'),
    path('update/<int:uid>/',views.update,name='update'),
    path('form_update/',views.form_update),
    path('table/',views.table)
    
    
]
