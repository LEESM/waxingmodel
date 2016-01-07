import os
import urllib.request
os.environ['DJANGO_SETTINGS_MODULE'] = 'waxing.settings'
import django
django.setup()
from selenium import webdriver
import time
from xinglala.models import Product
print('xingcrawler3 시작')
flag=0
base_url='http://www.xinglala.com/cn/?menuType=product&mode=view&prodCode='
items = Product.objects.all()[157:]
driver = webdriver.Firefox()
#driver.set_page_load_timeout(15)
flag=0
for i, item in enumerate(items):
	driver.get(base_url+item.xinglala_id)
	while True:
		try:
			mainimage=driver.find_element_by_css_selector('#selectImage')
			mainimage=mainimage.get_attribute('src')
			f=open('images/'+item.xinglala_id+'.jpg','wb')
			f.write(urllib.request.urlopen(mainimage).read())
			f.close()
			break
		except:
			if(flag==2):
				print('main 사진 없음')
				flag=0
				break
			else:
				print('메인사진 에러')
				flag=flag+1
				time.sleep(0.3)
	while True:
		try:
			detaildiv=driver.find_element_by_css_selector('.detailArea')
			details=detaildiv.find_elements_by_xpath("//center/img")
			for j, detail in enumerate(details):
				f=open('images/'+item.xinglala_id+'_'+str(j)+'.jpg','wb')
				f.write(urllib.request.urlopen(detail.get_attribute('src')).read())
				f.close()
				print(item.xinglala_id+'아이템 '+str(j)+'번 저장')
			print(str(item.id) + '번 완료 / 싱라라_아이디 : ' + item.xinglala_id)
			break
		except:
			if(flag==2):
				print('detail 사진 없음')
				flag=0
				break
			else:
				flag=flag+1
				time.sleep(0.3)
'''
f = open('00000001.jpg','wb')
f.write(urllib.urlopen('http://www.gunnerkrigg.com//comics/00000001.jpg').read())
f.close()
'''