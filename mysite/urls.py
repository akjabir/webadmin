from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('history.urls')),
    path("/", include('history.urls')),
    path('single_post/<int:id>',single_post.single_post)', 
    path('', include('base.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

