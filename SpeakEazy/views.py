from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def SpeakEazy(request):
    return render(request,'home.html')


def voice_to_text(request):
    context = {'include_link': True} 
    return render(request,'VoiceToText.html',context)

def text_to_voice(request):
    context = {'include_link': True} 
    return render(request,'Text to voice.html',context)

def gesture_to_text(request):
    context = {'include_link': False} 
    return render(request,'Gesture to Text.html',context)

def gesture_to_voice(request):
    context = {'include_link': True} 
    return render(request,'GestureToVoice.html',context)

