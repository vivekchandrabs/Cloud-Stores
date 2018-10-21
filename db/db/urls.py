"""db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dbapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('signin/',views.signin),
    path('signup/',views.signup),
    path('logout/', views.signout),
    path('<slug:user_name>/base/',views.Take_Text),
    path('<slug:owner>/owner/',views.owner),
    path('<slug:owner>/addstore/',views.addstore),
    path('<int:storeid>/additems/',views.additem),
    path('<int:storeid>/viewitems/',views.viewitem),
    path('<int:storeid>/<int:shopid>/orderitems/',views.orderitems),
    path('<int:storeid>/chooseshop/',views.chooseshop),
    path('<slug:owner>/orderitems/',views.choosestore),
    path('<int:storeid>/addshop/',views.addshop),
    path('sendemail/',views.sendemail),
    path('<slug:owner>/delete/',views.deleteshop),
    path('<int:storeid>/deletestores/',views.deletestores),
    path('delete/<int:store_id>/<int:item_id>/', views.delete_item_from_cart),
    path('checkout-customer/<int:storeid>/', views.checkoutcust),
    path('shop/<int:storeid>/checkout/',views.customer),
    
    

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
