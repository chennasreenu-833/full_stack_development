from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_image$',views.get_image,name='get_image'),
    url(r'^get_css$', views.get_css, name='get_css'),
    url(r'^get_js$',views.get_js,name='get_js'),
    url(r'^get_suppliers$',views.get_suppliers,name='get_suppliers'),

    url(r'^$', views.market_home, name='market_home'),
]