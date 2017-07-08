from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_image$',views.get_image,name='get_image'),
    url(r'^$', views.market_home, name='market_home'),
]