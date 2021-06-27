from django.conf.urls import url, re_path
from django.urls import path, include, reverse
from beneficiario import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r"^$",views.HomePageView.as_view(), name="index"),
    url(r"solicitudes/",views.HomeSolicitudView.as_view(), name="solicitudes"),
    url(r"solicitud/(?P<id>\d+)/$",views.DetalleSolicitudView.as_view(),name="detalle"),
    url(r"^solicitud/create/$",views.SolicitudCreate.as_view(success_url="/solicitudes/"),name="solicitud_create"),
    url(r'^solicitud/(?P<pk>\d+)/update/$', views.SolicitudUpdate.as_view(success_url="/solicitudes/"),name="solicitud_update"),
    url(r'^solicitud/(?P<pk>\d+)/delete/$', views.SolicitudDelete.as_view(success_url="/solicitudes/"),name="solicitud_delete"),
    url(r'^solicitud/(?P<id>\d+)/estado/$', views.ActualizarSolicitudView.as_view(),name="solicitud_estado"),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)