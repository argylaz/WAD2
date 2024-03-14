from django.urls import path
from soundSafariApp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'SoundSafari'

urlpatterns = [
    path('', views.index, name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)