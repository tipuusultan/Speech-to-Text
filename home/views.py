from django.shortcuts import render, HttpResponse
import speech_recognition as sr

# Create your views here.

def home(request):
    return render(request, 'index.html')




def result(request):
    if request.method == 'GET':
        try:
            r = sr.Recognizer()
            with sr.Microphone() as m:
                audio = r.listen(m)
                data = r.recognize_google(audio , language='eng-in')
                print(data)
        except:
            return HttpResponse("Something Went Wrong")
        context = {
            "data" : data
        }

    return render(request , 'index.html' , context )