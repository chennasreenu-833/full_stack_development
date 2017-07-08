# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
def mysql_for_get_producers():
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
def get_producers(request):
    records=mysql_for_get_producers()
    list={}
    for each_rec in records:
        supplier_id=each_rec[0]
        supplier_name=each_rec[1]
        supplier_address=each_rec[2]
        supplier_phone=each_rec[3]
        list[supplier_id]={"supplier_name":supplier_name,"supplier_address":supplier_address,"supplier_phone":supplier_phone}
    return HttpResponse(json.dumps(list), content_type="application/json")
def get_items_from_producer(request):
    foo=open("items_from_producer.html","r+")
    file_data=foo.read()
    id=request.GET.get('id','')
    supplier_name=request.GET.get('supplier_name','')
    print supplier_name
    file_data=file_data.replace("<<id_value>>",id)
    file_data=file_data.replace("<<supplier_name>>","'"+str(supplier_name)+"'")
    foo.close()
    return HttpResponse(file_data, content_type="text/html")
def get_producer_items(request):
    id=int(request.GET.get('id',''))
    records=mysql_for_get_producer_items(id)
    list={}
    for each_rec in records:
        item_id=each_rec[0]
        item_name=each_rec[1]
        item_price=each_rec[2]
        time_to_deliver=each_rec[3]
        list[item_id]={"item_name":item_name,"item_price":item_price,"time_to_deliver":time_to_deliver}
    return HttpResponse(json.dumps(list),content_type="application/json")
def mysql_for_get_producer_items(id):
    cursor=connection.cursor()
    sql="select item.item_id,item.item_name,producer_item_log.price,producer_item_log.time_to_deliver from producer_item_log inner join item on producer_item_log.item_id=item.item_id where producer_item_log.producer_id='%d' and item.app_type=1 order by producer_item_log.time_to_replenish;"%(int(id))
    cursor.execute(sql)
    list=cursor.fetchall()
    return list
