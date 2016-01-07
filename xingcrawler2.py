import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'waxing.settings'
import django
django.setup()
from selenium import webdriver
import time
from xinglala.models import Product
print('xingcrawler2 시작')
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
            status_check = driver.find_element_by_css_selector('#naviWrap')
            try:
                total_check = driver.find_element_by_css_selector('.listTopSortWrap strong')
                brand_total = total_check.text[:-1]
                brand_total = int(brand_total)
            except:
                print('상품 없음 패스')
                break
            brand = driver.find_element_by_css_selector('#best_PB01')
            xinglala_ids = driver.find_elements_by_xpath("//a[@class='btnProdListImg']")
            raw_text=brand.text
            text_list=raw_text.split('\n')
            text_list.pop()
            item_count=int((len(text_list))/3)
            print('아이템 갯수:'+str(item_count))
            for inno in range(0,item_count):
                brand_no = no
                brand = text_list[3*inno]
                product = text_list[3*inno+1]
                price_xinglala = text_list[3*inno+2][1:]
                xinglala_id = xinglala_ids[inno].get_attribute('href')[23:36]
                images = ''
                q=Product(brand_no=brand_no, brand=brand, product=product, price_xinglala=price_xinglala, xinglala_id=xinglala_id, images=images)
                q.save()
                print('저장'+brand+"/"+product+"/"+price_xinglala)
            if(brand_total>40):
                while True:
                    try:
                        driver.get(base_url+str(no)+middle_url+'2'+last_url)
                        brand = driver.find_element_by_css_selector('#best_PB01')
                        xinglala_ids = driver.find_elements_by_xpath("//a[@class='btnProdListImg']")
                        raw_text=brand.text
                        text_list=raw_text.split('\n')
                        item_count=int((len(text_list))/3)
                        print('아이템 갯수:'+str(item_count))
                        for inno in range(0,item_count):
                            brand_no = no
                            brand = text_list[3*inno]
                            product = text_list[3*inno+1]
                            price_xinglala = text_list[3*inno+2][1:]
                            xinglala_id = xinglala_ids[inno].get_attribute('href')[23:36]
                            images = ''
                            q=Product(brand_no=brand_no, brand=brand, product=product, price_xinglala=price_xinglala, xinglala_id=xinglala_id, images=images)
                            q.save()
                            print('저장'+brand+"/"+product+"/"+price_xinglala)
                        break
                    except:
                        print('2페이지 에러')
                        time.sleep(0.5)
            break
        except:
            print('에러 난 카테고리 넘버 : '+str(no))
            flag=flag+1
            if(flag==3):
                flag=0
                break
            else:
                print('에러발생')
                time.sleep(0.5)