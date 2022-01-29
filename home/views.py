from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Breakfast
from django.utils import timezone


def index(request):
    """
    home 출력
    """
    return render(request, 'home/index.html')


def breakfast_detail(request):
    """
    Breakfast 신청자 출력
    """
    breakfast_list = Breakfast.objects.order_by('-create_date')
    context = {'breakfast_list': breakfast_list}
    return render(request, 'home/breakfast_detail.html', context)


def breakfast_create(request):
    """
    Breakfast 신청
    """
    breakfast = Breakfast(group=request.POST.get('group'), name=request.POST.get('name'), create_date=timezone.now())
    breakfast.save()
    return redirect('home:index')

# Create your views here.
