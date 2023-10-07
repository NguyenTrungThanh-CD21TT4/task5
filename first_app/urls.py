from django.urls import path,re_path
from first_app import views

urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^form',views.form_name_view,name='form'),
]
