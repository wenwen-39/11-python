from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q

from mainsite.models import company, companyplace

def homepage(request):    
    test = companyplace.objects.all()

    return render(request,"index.html", locals())

def maps_mod(request,la,lo):
        MapLatitude = company.objects.filter(Q(latitude=la) | Q(longitude=lo))[0]
        return render(request,"maps.html", locals())

def homepage1(request, place=0):
        if place==1:
            data = company.objects.filter(place__contains="高雄市")
            return render(request,"place.html", locals())
        elif place==2:
            data = company.objects.filter(place__contains='基隆市')
            return render(request,"place.html", locals())
        elif place==3:
            data = company.objects.filter(place__contains='新北市')
            return render(request,"place.html", locals())
        elif place==4:
            data = company.objects.filter(place__contains='臺北市')
            return render(request,"place.html", locals())
        elif place==5:
            data = company.objects.filter(place__contains='新竹縣')
            return render(request,"place.html", locals())
        elif place==6:
            data = company.objects.filter(place__contains='桃園市')
            return render(request,"place.html", locals())
        elif place==7:
            data = company.objects.filter(place__contains='新竹市')
            return render(request,"place.html", locals())
        elif place==8:
            data = company.objects.filter(place__contains='苗栗市')
            return render(request,"place.html", locals())
        elif place==9:
            data = company.objects.filter(place__contains='苗栗縣')
            return render(request,"place.html", locals())
        elif place==10:
            data = company.objects.filter(place__contains='臺中市')
            return render(request,"place.html", locals())
        elif place==11:
            data = company.objects.filter(place__contains='彰化縣')
            return render(request,"place.html", locals())
        elif place==12:
            data = company.objects.filter(place__contains='彰化市')
            return render(request,"place.html", locals())
        elif place==13:
            data = company.objects.filter(place__contains='南投市')
            return render(request,"place.html", locals())
        elif place==14:
            data = company.objects.filter(place__contains='南投縣')
            return render(request,"place.html", locals())
        elif place==15:
            data = company.objects.filter(place__contains='雲林縣')
            return render(request,"place.html", locals())
        elif place==16:
            data = company.objects.filter(place__contains='嘉義縣')
            return render(request,"place.html", locals())
        elif place==17:
            data = company.objects.filter(place__contains='嘉義市')
            return render(request,"place.html", locals())
        elif place==18:
            data = company.objects.filter(place__contains='臺南市')
            return render(request,"place.html", locals())
        elif place==19:
            data = company.objects.filter(place__contains='屏東縣')
            return render(request,"place.html", locals())
        elif place==20:
            data = company.objects.filter(place__contains='屏東市')
            return render(request,"place.html", locals())
        elif place==21:
            data = company.objects.filter(place__contains='宜蘭縣')
            return render(request,"place.html", locals())
        elif place==22:
            data = company.objects.filter(place__contains='宜蘭市')
            return render(request,"place.html", locals())
        elif place==23:
            data = company.objects.filter(place__contains='花蓮縣')
            return render(request,"place.html", locals())
        elif place==24:
            data = company.objects.filter(place__contains='花蓮市')
            return render(request,"place.html", locals())
        elif place==25:
            data = company.objects.filter(place__contains='臺東市')
            return render(request,"place.html", locals())
        elif place==26:
            data = company.objects.filter(place__contains='臺東縣')
            return render(request,"place.html", locals())
        elif place==27:
            data = company.objects.filter(place__contains='澎湖縣')
            return render(request,"place.html", locals())
        elif place==30:
            data = company.objects.filter(place__contains='金門縣')
            return render(request,"place.html", locals())        
        elif place==32:
            data = company.objects.filter(place__contains='連江縣')
            return render(request,"place.html", locals())
        


