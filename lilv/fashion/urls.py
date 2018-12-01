from django.conf.urls import url

from fashion import views

urlpatterns = [
    url(r'^$',views.index)
]