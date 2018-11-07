from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^clasificacion/nueva/$', views.clasificacion_nueva, name='clasificacion_nueva'),
    path('', views.clasificacion_lista, name='clasificacion_lista'),
    path('clasificacion/lista', views.clasificacion_lista, name='clasificacion_lista'),
    path('clasificacion/<int:pk>/editar/', views.clasificacion_editar, name='clasificacion_editar'),
    url(r'^clasificacion/(?P<pk>\d+)/remove/$', views.clasificacion_remove, name='clasificacion_remove'),
    path('clasificacion/<int:pk>/', views.clasificacion_detalle, name='clasificacion_detalle'),
    path('libro/lista', views.libro_lista, name='libro_lista'),
    url(r'^libro/nuevo/$', views.libro_nuevo, name='libro_nuevo'),
    path('libro/<int:pk>/editar/', views.libro_editar, name='libro_editar'),
    url(r'^libro/(?P<pk>\d+)/remove/$', views.libro_remove, name='libro_remove'),
    ]
