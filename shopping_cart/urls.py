
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from accounts import views as accounts
from shopping import views as shopping

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(("accounts.urls","accounts"))),
    url(r'^logout/$', accounts.user_logout, name='logout'),
    path('', shopping.homepage, name='homepage'),
    path('shopping/', include(("shopping.urls","shopping"))),
]
