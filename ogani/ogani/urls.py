from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from django.conf import settings
from django.conf.urls.static import static

from ogani import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexViews.as_view(), name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
