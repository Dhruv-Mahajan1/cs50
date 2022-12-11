from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("addlisting", views.addlisting, name="addlisting"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("addcomment/<int:id>", views.addcomment, name="addcomment"),
    path("addbid/<int:id>", views.addbid, name="addbid"),
    path("addtowishlist/<int:id>", views.addtowishlist, name="addtowishlist"),
    path("viewwishlist", views.viewwishlist, name="viewwishlist"),
    path("detelewishlistitem/<int:id>", views.detelewishlistitem, name="detelewishlistitem"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category>", views.particularcategory, name="particularcategory"),
    path("closebid/<int:id>", views.closebid, name="closebid"),
    path("yourlistings", views.yourlistings, name="yourlistings"),
    path("boughtitems", views.boughtitems, name="boughtitems"),
    

    
]

