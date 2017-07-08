# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
def mysql_for_get_suppliers():
    cursor=connection.cursor()
    sql="select supplier_id,supplier_name,supplier_address,supplier_phone from supplier where supplier.app_type=1"
    cursor.execute(sql)
    list=cursor.fetchall()
    return list

def market_home(request):
    foo = open("market_home.html", "r+")
    file_date = foo.read()
    foo.close()
    return HttpResponse(file_date, content_type="text/html")

def get_image(request):
    image_name=request.GET.get('image','')
    foo = open("images/"+image_name+".png", "rb+")
    file_data = foo.read()
    foo.close()
    return HttpResponse(file_data, content_type="image/png")

def get_css(request):
    file_name=request.GET.get('file','')
    foo=open(file_name+".css","r+")
    file_data=foo.read()
    foo.close()
    return HttpResponse(file_data,content_type="text/css")

def get_js(request):
    file_name=request.GET.get('file','')
    foo=open(file_name+".js","r")
    file_data=foo.read()
    return HttpResponse(file_data,content_type="application/javascript")
def get_suppliers(request):
    records=mysql_for_get_suppliers()
    list={}
    for each_rec in records:
        supplier_id=each_rec[0]
        supplier_name=each_rec[1]
        supplier_address=each_rec[2]
        supplier_phone=each_rec[3]
        list[supplier_id]={"supplier_name":supplier_name,"supplier_address":supplier_address,"supplier_phone":supplier_phone}
    return HttpResponse(json.dumps(list), content_type="application/json")