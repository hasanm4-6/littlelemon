from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from .serializers import MenuSerializer, BookingSerializer, UserSerializer  
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from .models import Menu, Booking
from .forms import BookingForm
from datetime import datetime
import json

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    
    return render(request, 'bookings.html',{"bookings":booking_json})

def book(request):
    form = BookingForm()
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    
    return render(request, 'book.html', context)

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    
    return render(request, 'menu.html', {"menu": main_data})

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
        
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def bookings(request):
    if request.method == "POST":
        data = json.load(request)
        
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(reservation_slot=data['reservation_slot']).exists()

        if not exist:
            booking = Booking( first_name = data['first_name'], reservation_date = data['reservation_date'], reservation_slot = data['reservation_slot'] )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')

    date_str = request.GET.get('date')
    if date_str:
        query_date = date_str
    else:
        query_date = str(datetime.today().date())

    bookings = Booking.objects.filter(reservation_date=query_date)
    booking_json = json.loads(serializers.serialize('json', bookings))

    label = "Today" if query_date == str(datetime.today().date()) else query_date

    return JsonResponse({label: booking_json}, safe=False)