from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_image$',views.get_image,name='get_image'),
    url(r'^get_css$', views.get_css, name='get_css'),
    url(r'^get_js$',views.get_js,name='get_js'),
    url(r'^get_producers$',views.get_producers,name='get_suppliers'),
    url(r'^get_items_from_producer$',views.get_items_from_producer,name='get_items_from_producer'),
    url(r'^get_producer_items$',views.get_producer_items,name='get_producer_items'),
    url(r'^$', views.market_home, name='market_home'),
]