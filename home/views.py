from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Breakfast
from django.utils import timezone
import datetime


def index(request):
    """
    home 출력
    """
    return render(request, 'home/index.html')


def breakfast_detail(request):
    """
    Breakfast 신청자 출력
    """
    x = datetime.datetime.now()
    y = datetime.datetime(x.year, x.month, x.day, 8, 30, 0)
    if x < y:
        today = datetime.date.today()
        today = today - datetime.timedelta(1)
    else:
        today = datetime.date.today()

    start_time = datetime.datetime(today.year, today.month, today.day, 8, 30, 0)
    breakfast_list = Breakfast.objects.filter(create_date__range=[start_time, timezone.now()]).order_by("-create_date")
    context = {'breakfast_list': breakfast_list}
    return render(request, 'home/breakfast_detail.html', context)


def breakfast_create(request):
    """
    Breakfast 신청
    """
    breakfast = Breakfast(group=request.POST.get('group'), name=request.POST.get('name'), create_date=timezone.now())
    breakfast.save()
    return redirect('home:index')


def breakfast_delete(request, breakfast_id):
    breakfast = get_object_or_404(Breakfast, pk=breakfast_id)
    breakfast.delete()
    return redirect('home:detail')
# Create your views here.
