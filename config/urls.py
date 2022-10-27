"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from music import views
from music.views import Cover


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', views.index, name="home",),
    path('album/new', views.create_album, name="create_album"),
    path('album/<int:pk>/', views.album_detail, name="album_detail"),
    path('album/<int:pk>/edit/', views.edit_album, name='edit_album'),
    path('album/delete/<int:pk>', views.delete_album, name='delete_album'),
    path('', Cover.as_view()),
    path('favorites/new/<int:alb_pk>', views.add_favorite, name='favorite'),
    path('favorites/', views.favorite, name='favorite_page')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)