from django.conf.urls import url

from fashion import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^exit/$',views.exit,name='exit'),
    url(r'^register/$', views.register, name='register'),
    url(r'^car/$', views.car, name='car'),
    url(r'^goods/$',views.goods, name='goods'),
    url(r'^list/$', views.list, name='list'),
]