from django.urls import *
from admin import *
from django.views.generic import*
import json
# data=b"['''LangFrom:Python''']"
# with open('fi.cc','wb') as file:
#     fo=file.write(data)
#     print(fo)
def readOrder():
    with open("curent.json" ,'r')as JSonData:
        res=JSonData.read()

        return res




