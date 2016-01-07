import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'waxing.settings'
import django
django.setup()
from selenium import webdriver
import time
#from xinglala.models import Product
print('크롤링 시작')
flag=0