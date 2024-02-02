from django.urls import path
from . import views
urlpatterns =[
    path("",views.func),
    path("<int:month>",views.monthly_challanges_by_num),
    path("<str:month>",views.monthly_challanges,name="monthname")
              ]