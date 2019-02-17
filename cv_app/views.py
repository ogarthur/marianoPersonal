from django.shortcuts import render
from cv_app import user_information
# Create your views here.
def index(request):
    print(user_information.test_user_data)
    data = user_information.test_user_data

    return render(request,'cv_app/cv.html',{'user_data':data})
