from django.urls import path
from todoapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('finished/<todo_id>', views.finished, name='finished'),
    path('delcomp', views.delcomp, name='delcomp'),
    path('delall', views.delall, name='delall'),
]