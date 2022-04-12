from django.urls import path

from . import views

app_name = 'elecciones'

urlpatterns=[
    # ex: /elecciones/
    path('',views.index, name='index'),
    path('<int:region_id>/', views.resultados, name='resultados'),


]