import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'waxing.settings'
import django
django.setup()
from selenium import webdriver
import time
import datetime
from crawler.models import Post

def check(link):
	test=Post.objects.filter(link=link)
	if test:
		return True
	else:
		return False

print('왁싱 크롤링 시작')
#시간 만들기
now = datetime.datetime.now()
ts1 = str(now - datetime.timedelta(days=1))[0:10]
ts2 = str(now)
time_from = ts1[0:4] + ts1[5:7] + ts1[8:10] + '000000'
time_to = ts2[0:4] + ts2[5:7] + ts2[8:10] + '235959'
#url 만들기
first_url = 'https://search.naver.com/search.naver?where=article&ie=utf8&query=%EC%99%81%EC%8B%B1+%EB%AA%A8%EB%8D%B8&t=0&st=rel&date_option=1&date_from='
second_url = '&date_to='
third_url = '&srchby=text&dup_remove=1&cafe_url=&without_cafe_url=&board=&sm=tab_pge&nso=so:r,p:1w,a:all&start='
#시작
end = 0
page = 1
link_ref = ''
driver = webdriver.Firefox()
while True:
	driver.get(first_url+time_from+second_url+time_to+third_url+str(page))
	cafe_list=driver.find_elements_by_css_selector('.sh_cafe_top')
	check_link = cafe_list[0].find_element_by_css_selector('.sh_cafe_title').get_attribute('href')
	if(len(cafe_list)<10):
		end = 1
	if(link_ref==check_link):
		break
	#이 페이지 긁기
	for i, item in enumerate(cafe_list):
		title = item.find_element_by_css_selector('.sh_cafe_title')
		link = title.get_attribute('href')
		if(check(link)==True):
			print('존재함 패스')
			continue
		title = title.text
		content = item.find_element_by_css_selector('.sh_cafe_passage').text
		post = Post(title=title, link=link, content=content, pub_date=now, cafe_blog='cafe')
		post.save()
		if(i==0):
			link_ref=link
	if(end==1):
		break
	page=page+10
	#다 긁고 비교를 위해 첫 글 저장





