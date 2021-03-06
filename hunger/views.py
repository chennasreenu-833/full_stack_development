# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import json
import datetime

def mysql_for_get_supplier_for_items_list(item_id):
    cursor=connection.cursor()
    current_time = datetime.datetime.now().hour
    current_time += 5
    sql="SELECT supplier.supplier_id,supplier.supplier_name,item.item_name,supplier_item_log.price,supplier_item_log.time_to_deliver from supplier_item_log inner join supplier on supplier_item_log.supplier_id=supplier.supplier_id inner join item on supplier_item_log.item_id=item.item_id where item.app_type=0 and item.item_id='%d' and supplier_item_log.available_from<='%d' and supplier_item_log.available_to>'%d';"%(int(item_id),current_time,current_time)
    cursor.execute(sql)
    list=cursor.fetchall()
    return list

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
    current_time= datetime.datetime.now().hour
    current_time+=5
    sql="select item.item_id,item.item_name,supplier_item_log.price,supplier_item_log.time_to_deliver from supplier_item_log inner join item on supplier_item_log.item_id=item.item_id where item.app_type=0 and supplier_item_log.supplier_id='%d' and supplier_item_log.available_from<='%d' and supplier_item_log.available_to>'%d' ;" %(id,current_time,current_time)
    cursor.execute(sql)
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
    sql="select supplier.supplier_id,supplier.supplier_name,supplier.supplier_address,supplier.supplier_phone from supplier inner join supplier_status on supplier.supplier_id=supplier_status.supplier_id where supplier.app_type=0 and supplier_status.supplier_state=1"
    cursor.execute(sql)
    list=cursor.fetchall()
    return list
def mysql_for_get_supplier_status():
    cursor=connection.cursor()
    sql="select supplier_status.supplier_id,supplier.supplier_name,supplier_status.supplier_state from supplier_status inner join supplier on supplier.supplier_id=supplier_status.supplier_id where supplier.app_type=0;"
    cursor.execute(sql)
    list=cursor.fetchall()
    return list
# def mysql_for_get_supplier_items(id):
#     cursor=connection.cursor()
#     sql="select item.item_id,item.item_name,supplier_item_log.price,supplier_item_log.time_to_deliver from supplier_item_log inner join item on supplier_item_log.item_id=item.item_id where supplier_item_log.supplier_id='%d' and item.app_type=0;"%(int(id))
#     cursor.execute(sql)
#     list=cursor.fetchall()
#     return list

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

def mysql_for_check_admin_login(username,password):
    cursor=connection.cursor()
    sql="select admin_password,admin_id from admin where admin_username = '%s';" %(username)
    cursor.execute(sql)
    list=cursor.fetchall()
    if(list):
        if(list[0][0]==str(password)):
            admin_id=list[0][1]
            return admin_id
        else:
            return "failed"
    else:
        return "invalid"

def home(request):
    foo = open("hunger_home.html", "r+")
    file_date = foo.read()
    foo.close()
    return HttpResponse(file_date, content_type="text/html")
def show_items_as_list(request):
    foo=open("show_items_as_list.html","r+")
    file_data=foo.read()
    foo.close()
    return HttpResponse(file_data,content_type="text/html")

def get_supplier_for_items_page(request):
    item_id=request.GET.get('id','')
    foo=open("get_supplier_for_items_page.html");
    file_data=foo.read()
    file_data = file_data.replace("<<id_value>>", item_id)
    foo.close()
    return HttpResponse(file_data,content_type="text/html")


def get_supplier_for_items_list(request):
    item_id=request.GET.get('id','')
    records=mysql_for_get_supplier_for_items_list(item_id)
    list={}
    list[item_id]=[];
    for each_rec in records:
        supplier_id=each_rec[0];
        supplier_name=each_rec[1];
        item_name=each_rec[2];
        price=each_rec[3];
        time_to_deliver=each_rec[4];
        list[item_id]+=[{"supplier_id":supplier_id,"supplier_name":supplier_name,"item_name":item_name,"price":price,"time_to_deliver":time_to_deliver}]
    return HttpResponse(json.dumps(list),content_type="application/json")



def show_items(request):
    foo = open("show_items.html", "r+")
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

def admin_login(request):
    foo=open("admin_login.html","r+")
    file_date = foo.read()
    foo.close()
    return HttpResponse(file_date, content_type="text/html")
def get_supplier_add_item_page(request):
    auth=request.POST.get('auth','')
    username=str(request.POST.get('username',''))
    userid=request.POST.get('userid','')
    foo=open('hunger_add_item.html','r+')

    file_data=foo.read()
    file_data=file_data.replace('<<auth>>',str(auth).lower())
    file_data=file_data.replace('<<username>>',str(username))
    file_data = file_data.replace('<<userid>>', str(userid))
    foo.close()
    return HttpResponse(file_data,content_type='text/html')

def get_items_from_supplier(request):
    foo=open("items_from_supplier.html","r+")
    file_data=foo.read()
    id=request.GET.get('id','')
    supplier_name=request.GET.get('supplier_name','')
    file_data=file_data.replace("<<id_value>>",id)
    file_data=file_data.replace("<<supplier_name>>","'"+str(supplier_name)+"'")
    foo.close()
    return HttpResponse(file_data, content_type="text/html")
def get_hunger_admin_page(request):
    auth = request.POST.get('auth', '')
    username = str(request.POST.get('username', ''))
    userid = request.POST.get('userid', '')
    foo = open('hunger_admin.html', 'r+')

    file_data = foo.read()
    file_data = file_data.replace('<<auth>>', str(auth).lower())
    file_data = file_data.replace('<<username>>', str(username))
    file_data = file_data.replace('<<userid>>', str(userid))
    foo.close()
    return HttpResponse(file_data, content_type='text/html')

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

def check_admin_login(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    result=mysql_for_check_admin_login(username,password)
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
def mysql_for_get_items_for_supplierid(supplier_id):
    cursor=connection.cursor()
    sql="select item.item_name,item.item_id,supplier_item_log.price from supplier_item_log inner join item on item.item_id=supplier_item_log.item_id where supplier_item_log.supplier_id='%d' and item.app_type=0;"%(int(supplier_id))
    cursor.execute(sql)
    list=cursor.fetchall()
    return list
def get_items_for_supplierid(request):
    supplier_id=int(request.POST.get('id',''))
    records=mysql_for_get_items_for_supplierid(supplier_id)
    list={}
    for each_rec in records:
        item_name=each_rec[0]
        item_id=each_rec[1]
        price=each_rec[2]
        if item_id not in list:
            list[item_id]={"item_name":item_name,"price":price}
    return HttpResponse(json.dumps(list),content_type="application/json")
def mysql_for_update_supplier_item_price(supplier_id,item_id,price):
    cursor=connection.cursor()
    sql="update supplier_item_log set price='%s' where supplier_id='%d' and item_id='%d' ;"%(str(price),int(supplier_id),int(item_id))
    cursor.execute(sql)


def update_supplier_item_price(request):
    supplier_id=request.POST.get('supplier_id','')
    item_id=request.POST.get('item_id','')
    try:
        price=float(request.POST.get('price',''))
        mysql_for_update_supplier_item_price(supplier_id,item_id,price)
        return HttpResponse(json.dumps({"response": "true"}), content_type="application/json")
    except Exception as ex:
        return HttpResponse(json.dumps({"response":"false"}),content_type="application/json")
def mysql_for_save_state(id,state):
    cursor=connection.cursor()
    sql="update supplier_status set supplier_state='%d' where supplier_id='%d'" %(int(state),int(id))
    cursor.execute(sql)

def save_state(request):
    id_string=request.POST.get('id_state','')
    suppliers=str(id_string).split('_')
    for each_supplier in suppliers:
        if not each_supplier:
            continue
        a=str(each_supplier).split(':')
        id=a[0]
        state=a[1]
        try:
            result=mysql_for_save_state(id,state)
        except Exception as ex:
            pass
    return HttpResponse(json.dumps({"response":"true"}),content_type="application/json")


# Create your views here.
