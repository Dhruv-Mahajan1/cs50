from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.gettitle,name='gettitle'),
    path("random",views.randomtitle,name='random'),
    path("search",views.search,name='search'),
    path("createnewpage",views.createnewpage,name='createnewpage'),
    path("edit/<str:title>",views.editentry,name='editentry'),
    path("saveedit/<str:title>",views.saveedit,name='saveedit'),
]
