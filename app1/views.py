
# from dbus import Bus
from .models import Register, Seat, BusDetail,Route
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import  datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
tme = datetime.now().time()

current_time = now.strftime("%H:%M:%S")

def home(request):
    if request.session.has_key('email'):  
        return redirect('buslist')
    elif request.session.has_key('driver_name'):
        return redirect('markedroute')
    else:
        return render(request,'bus-landing/index.html')
    

def nav(request):
    return render(request,'nav.html')

def register(request):
    if request.method == "POST":
        model=Register()
        model.first_name = request.POST['first_name']
        model.last_name = request.POST['last_name']
        model.email = request.POST['email']
        model.address = request.POST['address']
        model.password = request.POST['password']
        data=Register.objects.all().filter(email=request.POST['email'])
        if len(data)<=0:
            model.save()
            return redirect('login')
        else:
            return render(request, 'register.html',{'message':'alredy exist'})
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        try:
            data = Register.objects.get(email=request.POST['email'],password=request.POST['password'])
            if data:
                request.session['email'] = request.POST['email']
                return redirect('buslist')
            else:
                return render(request, 'login.html',{'message':'invalid id password'})
        except:
            return render(request, 'login.html',{'message':'invalid id password'})
    else:
        return render(request, 'login.html')

def buslist(request):
    if request.session.has_key('email'):
        model = BusDetail.objects.all()
        user = Register.objects.get(email = request.session['email'])
        return render(request, 'index.html', {'model': model,'user':user})
    else:
        return redirect('login')

def seat(request,id):
    if request.session.has_key('email'):
        bus = BusDetail.objects.get(id=id)
        model=Route.objects.filter(bus=bus)
        user = Register.objects.get(email = request.session['email'])
        return render(request, 'seat.html', {"model": model,'bus':bus,'user':user,'route':model})

def booking(request,id):
    if request.session.has_key('email'):
        bus = BusDetail.objects.get(id=id)
        user=Register.objects.get(email=request.session['email'])
        if request.method=='POST':
            seat=Seat()
            seat.bus=bus
            seat.nos=request.POST.get('nos')
            seat.booked_by_user=str(user)
            seat.timing=now
            x=request.POST.get('nos')
            seat.save()
            if  int(seat.nos)<=bus.rem and int(seat.nos)>0:
                bus.rem=int(bus.rem)-int(seat.nos)
                bus.save()
                return redirect('buslist')
            else:
                return render(request, 'book seat.html', {'bus':bus,'user':user,'message':'type valid seat number'})
        return render(request, 'book seat.html', {'bus':bus,'user':user})
    else:
        return redirect('login')


def logout(request):
    if request.session.has_key('email'):
        del request.session['email']
        return redirect('login')

def driverlogin(request):
    if request.method == 'POST':
        try:
            data = BusDetail.objects.get(driver_name=request.POST['driver_name'],password=request.POST['password'])
            if data:
                request.session['driver_name'] = request.POST['driver_name']
                print(request.session['driver_name'])
                return redirect('markedroute')
            else:
                return render(request, 'driverlogin.html',{'message':'invalid id password'})
        except:
            return render(request, 'driverlogin.html',{'message':'invalid id password'})
    else:
        return render(request, 'driverlogin.html')

def getbusroute(request,id):
    if request.session.has_key('email'):
        bus = BusDetail.objects.get(id=id)
        print(tme)
        if bus.dest_time<tme:
            bus.rem=0
            bus.save()
        route=Route.objects.filter(bus=bus)
        print(bus)
        return render(request, 'seat.html',{'route':route,'bus':bus})

def saetdetail(request):
    if request.session.has_key('email'):
        user=Register.objects.get(email=request.session['email'])
        bus = Seat.objects.filter(booked_by_user = user.email)
        return render(request,'seatdetail.html',{'bus':bus,'user':user})
    else:
        return redirect('login')

def markedroute(request):
    if request.session.has_key('driver_name'):
        model=BusDetail.objects.get(driver_name=request.session['driver_name'])
        # driver=BusDetail.objects.get(driver_name=request.session['driver_name'])
        print(model,'drivetrrr')
        bus=Route.objects.filter(bus=model)
        print(bus)
        if request.POST:
            print(request.POST.get('id'))
            m=Route.objects.get(id=request.POST.get('id'))
            print(m)
            m.marked=True
            m.marked_time=current_time  
            m.save()
            return render(request,'marked.html',{'bus':bus,'driver':model})
        return render(request,'marked.html',{'bus':bus,'driver':model})
    else:
        return redirect('driverlogin')


def driverlogout(request):
    if request.session.has_key('driver_name'):
        del request.session['driver_name']
        return redirect('driverlogin')
    else:
        return redirect('driverlogin')