"""INM_proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from Expedientes import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.gestionExpedientes, name="gestionExp"),
    path('registrarExtranjero/', views.registrarExtranjero),
    path('eliminacionExpediente/<numNue>', views.eliminarExpediente, name="eliminar"),
    path('listadoExpedientes/', views.listadoExpedientes, name="listaexp"),
    path('edicionExpedientes/<numNue>', views.edicionExpedientes, name="edicion"),
    path('editarExpediente', views.editarExpediente, name="editar"),
    path('expedientePDF/<numNue>', views.upload_file, name="expedientePDF"),
    path('confirmacionEliminar/<numNue>',views.confirmacionEliminar, name="confirmacionEliminar"),
    path('accounts/', include('django.contrib.auth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
