# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def market_home(request):
    return HttpResponse("Hello, world. You're at the market.")

def get_image(request):
    image_name=request.GET.get('image','')
    foo = open("images/"+image_name+".png", "rb+")
    file_data = foo.read()
    foo.close()
    return HttpResponse(file_data, content_type="image/png")

