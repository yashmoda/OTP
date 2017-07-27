from __future__ import unicode_literals

import requests
import random
from django.http import JsonResponse
from Reg.models import UserData
from Ver.models import OTP


def sotp(request):
    if request.method == 'POST':
        jsonresponse = {}
        try:

            #name = request.GET.get('name')
            contact = request.POST.get('contact')
            print contact
            otp = random.randint(100000, 999999)
            try:
                msg = "Your one time password is " + str(otp)
                authkey = '125195AnE7snTWFepK5925ea7c'
                url = 'https://control.msg91.com/api/sendhttp.php?authkey=' + authkey + '&mobiles='
                url += str(contact)
                url += '&message=' + msg
                url += '&sender=' + 'CodeNy' + '&route=4&country=91'
                print url
                print requests.request('GET', url)
                #urllib2.urlopen(url)
                #requests.get(url).read()
                #httplib2.Http().request(url)
                '''req = urllib2.Request(url)
                response = urllib2.urlopen(req)
                response.read()'''
                print msg
            except Exception as e:
                print e
            try:
                user = UserData.objects.get(phone=str(contact))
            except Exception as e:
                print e
                UserData.objects.create(phone=str(contact))
                user = UserData.objects.get(phone=str(contact))
            #setattr(user, 'name', name)
            #user.save()
            try:
                otp_obj = OTP.objects.get(phone=user)
                otp_obj.otp = otp
                otp_obj.save()
            except Exception as e:
                print e
                OTP.objects.create(phone=user, otp=otp)

            jsonresponse['success'] = True
            jsonresponse['Message'] = "OTP SENT"
            pass
        except Exception as e:
            print e
            jsonresponse['success'] = False
            jsonresponse['Message'] = "OTP NOT SENT"
        print (str(jsonresponse))
        return JsonResponse(jsonresponse)
    print 123


def votp(request):
    jsonresponse = {}
    try:
        contact = str(request.POST.get('contact'))
        otp = str(request.POST.get('otp'))
        user = UserData.objects.get(phone=str(contact))
        otpobj = OTP.objects.get(phone=user)
        if otpobj.otp == otp:
            setattr(otpobj, 'flag', True)
            jsonresponse['success'] = True
            jsonresponse['Message'] = "Successful"
        else:
            jsonresponse['success'] = False
            jsonresponse['Message'] = "Invalid OTP"
    except Exception as e:
        print e
        jsonresponse['success'] = False
        jsonresponse['Message'] = "Invalid Mobile Number"
    return JsonResponse(jsonresponse)
