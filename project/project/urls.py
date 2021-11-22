from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('core.urls')),
    # url(r'appadministracao/', include('core.urls')),
    # url(r'appaexterno/', include('appexterno.urls')),
    # url(r'criterio_avaliacao/', include('criterio_avaliacao.urls')),
    # url(r'appaluno/', include('appaluno.urls')),
    # url(r'appprofessor/', include('appprofessor.urls')),
    # url(r'avaliacao/', include('avaliacao.urls')),
    # url(r'curso/', include('curso.urls')),
    # url(r'disciplina/', include('disciplina.urls')),
    # url(r'documento/', include('documento.urls')),
    # url(r'submissao/', include('submissao.urls')),
    # url(r'turma/', include('turma.urls')),
    url(r'users/', include('users.urls')),
   
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # url(r'', include('landpage.urls')),
]

#url para arquivos de media quando em desenvolvimento
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, 
    document_root = settings.STATIC_ROOT)    
  
