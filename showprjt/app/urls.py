from django.urls import path
from .import views

urlpatterns = [
    path('',views.e_shop_login),

    #----------------admin---------------
    path('shop_home',views.shop_home),
    path('logout',views.e_shop_logout),
    path('addproduct', views.addproduct),
    path('edit_product/<pid>',views.edit_product),
    path('delete_product/<pid>',views.delete_product),



    #-------------------user-----------------
    path('register',views.register),
    path('user_home',views.user_home),
    path('view_product/<pid>',views.view_product),
    path('add_to_cart/<pid>',views.add_to_cart),
    path('view_cart',views.view_cart),

]