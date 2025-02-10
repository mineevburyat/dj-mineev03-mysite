from django.contrib import admin
from django.urls import path, include
from filebrowser.sites import site
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('main.urls', namespace='main')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('library/', include('library.urls', namespace='library')),
    path('service/', include('service.urls', namespace='service')),
    path('project/', include('project.urls', namespace='project')),
    path('about/', include('about.urls', namespace='about')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]