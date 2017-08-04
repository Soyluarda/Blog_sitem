# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse

def home_view(request):
    if request.user.is_authenticated():
        context ={
            'isim':'Barış',
    }
    else:
        context={
            'isim':'Misafir',
    }
    return render(request, 'home.html', context)
