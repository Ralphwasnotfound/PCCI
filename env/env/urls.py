
from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("",include ('pccweb.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
