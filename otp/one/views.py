from django.shortcuts import render, HttpResponse
from .models import userDetail, OTPValidator
from random import randrange
import requests
# Create your views here.
def home(request):
    return render(request, 'signup.html')

def generate_otp(uid,ph):
    otp = randrange(111111, 999999)
    url = "https://api.textlocal.in/send/?apiKey=&sender=&numbers=&message="
    resp = requests.get(url)
    resp.json().get('status')
    if resp.json().get('status') == 'success':
        OTPValidator(otp=otp, uid=uid).save()
        return 1
    else:
        return 0

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        phoneno = request.POST['phoneno']

        user = userDetail(username=username, password= password, email= email, phoneno= phoneno)
        user.save()
        obj = userDetail.objects.get(username=username, password= password, email= email, phoneno= phoneno)
        gt = generate_otp(obj.id, phoneno)
        if not gt:
            return HttpResponse("Please enter valid phone number")
        else:
            return render(request, 'validate_otp.html', {'uid': obj.id})

def validate_otp(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        uid = request.POST['uid']
        try:
            obj = OTPValidator.objects.get(uid=uid, otp=otp)
            uobj = userDetail.objects.get(id=uid)
            uobj.ph_valid = 1
            uobj.save()
            obj.delete()
            return HttpResponse("Your phone validated. ")
        except:
            return HttpResponse("Invalid otp ")
