import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'waxing.settings'
import django
django.setup()
from selenium import webdriver
import time
from xinglala.models import Product
print('크롤링 시작')
flag=0
base_url='http://www.xinglala.com/cn/?menuType=product&mode=brandList&lcate=&mcate=&scate=&fcate=&lcateShare=&searchField=&searchKey=&searchIcon6=&searchIcon7=&searchIcon8=&sort=&searchColor=&searchSize=&searchStartPrice=&searchEndPrice=&pr_no='
middle_url='&SearchBrand=&page='
last_url='&FCT='
simple_url='http://www.xinglala.com/cn/?menuType=product&mode=brandList&pr_no='
driver = webdriver.Firefox()
for no in range(1,270):
    while True:
        try:
            driver.get(simple_url+str(no))
            total_check = driver.find_element_by_css_selector('.listTopSortWrap strong')
            brand_total = total_check.text[:-1]
            brand_total = int(brand_total)
            brand = driver.find_element_by_css_selector('#best_PB01')
            raw_text=brand.text
            text_list=raw_text.split('\n')
            text_list.pop()
            item_count=int((len(text_list))/3)
            print(item_count)
            for inno in range(0,item_count):
                brand_no = no
                brand = text_list[3*inno]
                product = text_list[3*inno+1]
                price_xinglala = text_list[3*inno+2][1:]
                q=Product(brand_no=brand_no, brand=brand, product=product, price_xinglala=price_xinglala)
                q.save()
                print(brand+"/"+product+"/"+price_xinglala)
            if(brand_total>40):
                driver.get(base_url+str(no)+middle_url+'2'+last_url)
                brand = driver.find_element_by_css_selector('#best_PB01')
                raw_text=brand.text
                text_list=raw_text.split('\n')
                text_list.pop()
                item_count=int((len(text_list))/3)
                print(item_count)
                for inno in range(0,item_count):
                    brand_no = no
                    brand = text_list[3*inno]
                    product = text_list[3*inno+1]
                    price_xinglala = text_list[3*inno+2][1:]
                    q=Product(brand_no=brand_no, brand=brand, product=product, price_xinglala=price_xinglala)
                    q.save()
                    print(brand+"/"+product+"/"+price_xinglala)
            break
        except:
            print(str(no))
            flag=flag+1
            if(flag==3):
                flag=0
                break
            else:
                print('에러발생')
                time.sleep(0.5)