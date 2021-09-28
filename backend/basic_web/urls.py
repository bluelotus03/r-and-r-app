from django.contrib import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken'))
]
