from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^get_items_list$',views.get_items_list,name='get_items_list'),
    url(r'^get_items$',views.get_items,name='get_items'),
    url(r'^get_suppliers$',views.get_suppliers,name='get_suppliers'),
    url(r'^get_supplier_status$',views.get_supplier_status,name='get_supplier_status'),
    url(r'^add_supplier_item$',views.add_supplier_item,name='add_supplier_item'),
    url(r'^supplier_login$',views.supplier_login,name='supplier_login'),
    url(r'^check_supplier_login$',views.check_supplier_login,name='supplier_login'),
    url(r'^get_css$',views.get_css,name='get_css'),
    url(r'^get_js$',views.get_js,name='get_js'),
    url(r'^get_image$',views.get_image,name="get_image"),
    url(r'^get_items_from_supplier$', views.get_items_from_supplier, name="get_items_from_supplier"),
    url(r'^get_supplier_items$',views.get_supplier_items,name="get_supplier_items"),
    url(r'',views.home,name='home'),


]
