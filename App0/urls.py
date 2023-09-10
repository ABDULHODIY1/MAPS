"""
        API AND MAP URLS
        FOR MAGA WEB SIT
"""
from .views import *
from django.urls import path
urlpatterns=[
    path("",Home.as_view(),name='Home'),
    path("Mapllowbddbdbgwgwsjh374826jhewnnbdb83y4bheuyghsbnvdsbv55bdg2647bgf", Mapd.as_view(), name='Map'),
    path("Map2sdbdsdsvjhsfbvsfhuehvhuyrhuirvhsbfehfr877878wu43uy34847yg487ry4rfy438r7g348743tg3ry34",Map2Real.as_view(),name='Map2'),
    path("api/locations/", LocationList.as_view(), name="location-list"),

]

