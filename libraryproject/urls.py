from django.contrib import admin
from django.urls import include, path
import apps.bookmodule.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include("apps.bookmodule.urls")),
    path('users/', include("apps.usermodule.urls")),
    path('books/', include('apps.bookmodule.urls')),
]
