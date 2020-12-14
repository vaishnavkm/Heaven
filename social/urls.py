from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .forms import *
from .views import *
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home-view'),
    path('profiles/', include('profiles.urls')),
    path('posts/', include('posts.urls')),
    path('register',views.register,name='register'),
    path('login',views.login_id,name='login'),
    path('logout',views.logout_id,name='logout'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
