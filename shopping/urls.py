from django.urls import path,re_path
from django.conf.urls import include
from shopping import views 

urlpatterns = [
    path('create-product/',views.create_product,name="create_product"),
    path('',views.list_product,name="list_product"),
    re_path('product-details/(?P<pk>.*)/$',views.view_product,name="view_product"),
    re_path('update-product/(?P<pk>.*)/$',views.update_product,name="update_product"),
]