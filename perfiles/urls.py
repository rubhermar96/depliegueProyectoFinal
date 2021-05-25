from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', views.BienvenidaView.as_view(), name='bienvenida'),
    url(r'^registrate/$', views.SignUpView.as_view(), name='sign_up'),
    url(r'^inicia-sesion/$', views.SignInView.as_view(), name='sign_in'),
    url(r'^cerrar-sesion/$', views.SignOutView.as_view(), name='sign_out'),
    path('ofertas/', login_required(views.listado_ofertas), name='listado_ofertas'),
    path('ofertas/new/', login_required(views.crear_oferta), name='crear_oferta'),
    path('ofertas/oferta/<int:pk>/', login_required(views.detalle_oferta),name='detalle_oferta'),
    path('ofertas/oferta/<int:pk>/edit/', login_required(views.editar_oferta),name='editar_oferta'),
    path('candidaturas/', login_required(views.mis_candidaturas), name='mis_candidaturas'),
    path('candidaturas/candidatura/<int:pk>/',login_required(views.detalle_candidatura), name='detalle_candidatura'),
    path('candidaturas/candidatura/<int:pk>/eliminar/',login_required(views.eliminar_candidatura),name='eliminar_candidatura'),
    path('ofertas/oferta/<int:pk>/new-candidatura/',login_required(views.crear_candidatura),name='crear_candidatura'),
    path('ofertas/oferta/<int:pk>/candidaturas/',login_required(views.listado_candidatos),name='listado_candidatos'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)