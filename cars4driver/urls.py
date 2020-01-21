from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls import handler404
from django.conf import settings
from apps import views
from dealer import views
from dashboard import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.urls',namespace="cars")),
    url(r'^dealer/', include('dealer.urls',namespace="dealers")),
    url(r'^dashboard/', include('dashboard.urls',namespace="dashboard"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
