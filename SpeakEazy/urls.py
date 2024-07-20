from django.urls import path,include
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('speakeazy/',views.SpeakEazy,name='SpeakEazy'),
    path('', TemplateView.as_view(template_name="home.html"), name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('voice-to-text/', views.voice_to_text, name='voice-to-text'), 
    path('text-to-voice/', views.text_to_voice, name='text-to-voice'),
    path('gesture-to-text/', views.gesture_to_text, name='gesture-to-text'),
    path('gesture-to-voice/', views.gesture_to_voice, name='gesture-to-voice')
]