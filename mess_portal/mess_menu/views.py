from django.shortcuts import render,  get_object_or_404

from django.http import HttpResponse
from django.utils import timezone
from .models import Day, Food

def index(request):
    day_list = Day.objects.all()
    context = {'day_list': day_list}
    return render(request, 'mess_menu/index.html', context)

def detail(request, day_id):
    day = get_object_or_404(Day,pk = day_id)
    return render(request,'mess_menu/detail.html',{'day':day})

def today(request):
    day_list = Day.objects.all()
    date = timezone.now()
    today_name = date.today().strftime("%A")
    context = {
        
        'day_list': day_list,
        'today_name': today_name,
    }
    return render(request, 'mess_menu/today.html', context)
    

    
