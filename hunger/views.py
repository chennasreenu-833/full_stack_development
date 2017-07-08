# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import json
import datetime
def mysql_for_get_items_list():
    cursor=connection.cursor()
    sql="select supplier.supplier_id,supplier.supplier_name,item.item_id,item.item_name,supplier_item_log.price,supplier_item_log.time_to_deliver" \
        " from supplier_item_log" \
        " inner join item on item.item_id=supplier_item_log.item_id" \
        " inner join supplier on supplier.supplier_id=supplier_item_log.supplier_id" \
        " inner join supplier_status on supplier_status.supplier_id=supplier_item_log.supplier_id" \
        " where supplier_status.supplier_state=1 and supplier.app_type=0"
    cursor.execute(sql)
    list=cursor.fetchall()
    return list
def mysql_for_get_supplier_items(id):
    cursor=connection.cursor()
    sql="select item.item_name,supplier_item_log.price,supplier_item_log.time_to_deliver from supplier_item_log inner join item on supplier_item_log.item_id=item.item_id where item.app_type=0 and supplier_item_log.supplier_id='%d;" %(id)
    list=cursor.fetchall()
    return list
def mysql_for_get_items():
    cursor=connection.cursor()
    sql="select * from item"
    cursor.execute(sql)
    list=cursor.fetchall()
    return list

def mysql_for_get_suppliers():
    cursor=connection.cursor()
    sql="select supplier_id,supplier_name,supplier_address,supplier_phone from supplier where supplier.app_type=0"
    cursor.execute(sql)
    list=cursor.fetchall()
    return list
def mysql_for_get_supplier_status():
    cursor=connection.cursor()
    sql="select supplier_status.supplier_id,supplier.supplier_name,supplier_status.supplier_state from supplier_status inner join supplier on supplier.supplier_id=supplier_status.supplier_id where supplier.app_type=0;"
    cursor.execute(sql)
    list=cursor.fetchall()
    return list
def mysql_for_get_supplier_items(id):
    cursor=connection.cursor()
    sql="select item.item_id,item.item_name,supplier_item_log.price,supplier_item_log.time_to_deliver from supplier_item_log inner join item on supplier_item_log.item_id=item.item_id where supplier_item_log.supplier_id='%d' and item.app_type=0;"%(int(id))
    cursor.execute(sql)
    list=cursor.fetchall()
    return list

def mysql_for_add_supplier_item(supplier_id,item_id,available_from,available_to,price,time_to_deliver):
    cursor=connection.cursor()
    status=True
    sql="insert into supplier_item_log(supplier_id,item_id,available_from,available_to,price,time_to_deliver) values(%d,%d,%d,%d,%f,%d)" %(supplier_id,item_id,available_from,available_to,price,time_to_deliver)
    try:
        cursor.execute(sql)
        connection.commit()

    except:
        connection.rollback()
        status=False
    return status
def mysql_for_check_supplier_login(username,password):
    cursor=connection.cursor()
    sql="select supplier_password,supplier_id from supplier where supplier_username = '%s';" %(username)
    cursor.execute(sql)
    list=cursor.fetchall()
    if(list):
        if(list[0][0]==str(password)):
            supplier_id=list[0][1]
            return supplier_id
        else:
            return "failed"
    else:
        return "invalid"

def home(request):
    foo = open("hunger_home.html", "r+")
    file_date = foo.read()
    foo.close()
    return HttpResponse(file_date, content_type="text/html")
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
def supplier_login(request):
    foo=open("login.html","r+")
    file_date = foo.read()
    foo.close()
    return HttpResponse(file_date, content_type="text/html")

def get_items_from_supplier(request):
    foo=open("items_from_supplier.html","r+")
    file_data=foo.read()
    id=request.GET.get('id','')
    supplier_name=request.GET.get('supplier_name','')
    print supplier_name
    file_data=file_data.replace("<<id_value>>",id)
    file_data=file_data.replace("<<supplier_name>>","'"+str(supplier_name)+"'")
    foo.close()
    return HttpResponse(file_data, content_type="text/html")

def get_items_list(request):
    records=mysql_for_get_items_list()
    list={}
    for each_rec in records:
        supp_id=each_rec[0]
        supp_name=each_rec[1]
        item_id=each_rec[2]
        item_name=each_rec[3]
        item_price=each_rec[4]
        time_to_deliver=each_rec[5]
        if supp_id in list:
            list[supp_id]["all_items"]+=[{"item_id":item_id,"item_name":item_name,"item_price":item_price}]
        else:
            list[supp_id]={}
            list[supp_id]["supplier_name"]=supp_name
            list[supp_id]["all_items"]=[{"item_id":item_id,"item_name":item_name,"item_price":item_price}]
    return HttpResponse(json.dumps(list),content_type="application/json")
def get_items(request):
    records=mysql_for_get_items()
    list={}
    list["all_items"]=[]
    for each_rec in records:
        item_id=each_rec[0]
        item_name=each_rec[1]
        dict={"item_name":item_name,"item_id":item_id}
        list["all_items"].append(dict)
    return HttpResponse(json.dumps(list),content_type="application/json")
def get_suppliers(request):
    records=mysql_for_get_suppliers()
    list={}
    for each_rec in records:
        supplier_id=each_rec[0]
        supplier_name=each_rec[1]
        supplier_address=each_rec[2]
        supplier_phone=each_rec[3]
        list[supplier_id]={"supplier_name":supplier_name,"supplier_address":supplier_address,"supplier_phone":supplier_phone}

    return HttpResponse(json.dumps(list),content_type="application/json")
def get_supplier_status(request):
    records=mysql_for_get_supplier_status()
    list={}
    for each_rec in records:
        supplier_id=each_rec[0]
        supplier_name=each_rec[1]
        supplier_state=each_rec[2]
        list[supplier_id]={"supplier_name":supplier_name,"supplier_state":supplier_state}
    return HttpResponse(json.dumps(list),content_type="application/json")
def add_supplier_item(request):
    auth=str(request.POST.get('auth',''))
    supplier_id=int(request.POST.get('supplier_id',''))
    item_id=int(request.POST.get('item_id',''))
    available_from=int(request.POST.get("available_from",''))
    available_to=int(request.POST.get("available_to",''))
    price=float(request.POST.get("price",''))
    time_to_deliver=int(request.POST.get('time_to_deliver',''))
    if(auth=='TRUE'):
        result=mysql_for_add_supplier_item(supplier_id,item_id,available_from,available_to,price,time_to_deliver)
        if(result):
            return HttpResponse("SUCCESS")
        else:
            return HttpResponse("FAILED")
    else:
        return HttpResponse("invalid")

def check_supplier_login(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    result=mysql_for_check_supplier_login(username,password)
    return HttpResponse(result)

def get_image(request):
    image_name=request.GET.get('image','')
    foo = open("images/"+image_name+".png", "rb+")
    file_data = foo.read()
    foo.close()
    return HttpResponse(file_data, content_type="image/png")

def get_supplier_items(request):
    id=int(request.GET.get('id',''))
    records=mysql_for_get_supplier_items(id)
    list={}
    for each_rec in records:
        item_id=each_rec[0]
        item_name=each_rec[1]
        item_price=each_rec[2]
        time_to_deliver=each_rec[3]
        list[item_id]={"item_name":item_name,"item_price":item_price,"time_to_deliver":time_to_deliver}
    return HttpResponse(json.dumps(list),content_type="application/json")



# Create your views here.
