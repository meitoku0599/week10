from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # articleのurls.pyを読み込み
    path('', include('article.urls')),
    # markdownxを読み込み
    path('markdownx/', include('markdownx.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)