from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'cv_app/cv.html')
    #return render(request,'index.html')
