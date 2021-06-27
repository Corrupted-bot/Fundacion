from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .models import Solicitud, SolicitudFacade
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
            return render(request, "index.html", context=None)

class HomeSolicitudView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
            solicitudFacade = SolicitudFacade()
            return render(request, "solicitudes.html",{"solicitudes": solicitudFacade.buscarSolicitudes()})

class DetalleSolicitudView(LoginRequiredMixin,TemplateView):
    def get(self,request, **kwargs):
        id = int(kwargs["id"])
        solicitudFacade = SolicitudFacade()
        return render(request, "solicitud.html",{"solicitud": solicitudFacade.buscarSolicitud(id)})

class ActualizarSolicitudView(LoginRequiredMixin,TemplateView):
    def get(self,request, **kwargs):
        id = int(kwargs["id"])
        solicitudFacade = SolicitudFacade()
        p = solicitudFacade.buscarSolicitud(id)
        p.estado = True
        p.save()
        return redirect('solicitudes')


class SolicitudCreate(CreateView):
    model = Solicitud
    template_name = './solicitud_form.html'
    fields = ['nombre','rut','telefono','email','imagen']

class SolicitudUpdate(UpdateView):
    model = Solicitud
    template_name = './solicitud_form.html'
    fields = '__all__'


class SolicitudDelete(DeleteView):
    model = Solicitud
    template_name = './solicitud_confirm_delete.html'
    success_url = reverse_lazy('solicitudes')
    