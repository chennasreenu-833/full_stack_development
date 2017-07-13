from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^get_items_list$',views.get_items_list,name='get_items_list'),
    url(r'^get_items$',views.get_items,name='get_items'),
    url(r'^get_suppliers$',views.get_suppliers,name='get_suppliers'),
    url(r'^get_supplier_status$',views.get_supplier_status,name='get_supplier_status'),
    url(r'^add_supplier_item$',views.add_supplier_item,name='add_supplier_item'),
    url(r'^supplier_login$',views.supplier_login,name='supplier_login'),
    url(r'^admin_login$',views.admin_login,name='admin_login'),
    url(r'^check_supplier_login$',views.check_supplier_login,name='supplier_login'),
    url(r'^check_admin_login$',views.check_admin_login,name='check_admin_login'),
    url(r'^get_css$',views.get_css,name='get_css'),
    url(r'^show_items_as_list$',views.show_items_as_list,name="show_items_as_list"),
    url(r'^get_supplier_for_items_list$',views.get_supplier_for_items_list,name="get_supplier_for_items_list"),
    url(r'^get_js$',views.get_js,name='get_js'),
    url(r'^save_state$',views.save_state,name='save_state'),
    url(r'^show_items$',views.show_items,name='show_items'),
    url(r'^get_image$',views.get_image,name="get_image"),
    url(r'^get_supplier_for_items_page$',views.get_supplier_for_items_page,name="get_supplier_for_items_page"),
    url(r'^get_hunger_admin_page$',views.get_hunger_admin_page,name='get_hunger_admin_page'),
    url(r'^get_items_from_supplier$', views.get_items_from_supplier, name="get_items_from_supplier"),
    url(r'^get_supplier_items$',views.get_supplier_items,name="get_supplier_items"),
    url(r'^get_supplier_add_item_page$',views.get_supplier_add_item_page,name='get_supplier_add_item_page'),
    url(r'^get_items_for_supplierid$',views.get_items_for_supplierid,name='get_items_for_supplierid'),
    url(r'^update_supplier_item_price$',views.update_supplier_item_price,name='update_supplier_item_price'),
    url(r'',views.home,name='home'),


]
