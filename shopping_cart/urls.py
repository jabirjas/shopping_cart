
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls import include,url
from accounts import views as accounts
from shopping import views as shopping

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(("accounts.urls","accounts"))),
    url(r'^logout/$', accounts.user_logout, name='logout'),
    path('', shopping.homepage, name='homepage'),
    path('shopping/', include(("shopping.urls","shopping"))),

    re_path('media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path('static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_FILE_ROOT}),
]
