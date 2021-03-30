from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json

## test read data in file
###
	# f = open("a.txt", "r")
	# get_article(f.read())
	# ######
	# exit(0)
# file = open("a.txt","w")
		# file.write(driver.page_source)

url="https://ngs.ru"
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options
### primer https://gist.github.com/dzitkowskik/0fc641cf59af0dc3de62
### start elapsed time
####
def get_article(tbuf):
	soup = BeautifulSoup(tbuf, "html.parser")
	cnt = 0
	articles = dict()
	myarticles_dicts = list()
	for link in soup.find_all('article'):
		for st1 in link.find_all('a'):
			if st1.attrs['href'].find("/more/") != -1:
				if st1.attrs['title'].find("Подробнее") != -1:
					pass
				else:
					#debug print
					# print("info: https://ngs.ru" + st1.attrs['href'] + " рубрика: ", st1.attrs['title'])
					articles[st1.attrs['href']] = st1.attrs['title']
					cnt = cnt + 1
	articles_dict = dict(set(articles.items()))
	for a1 in articles_dict:
		try:
			if a1.split("/")[2].isdigit():
				id_articles = a1.split("/")[2]
		except Exception:
			id_articles = 0
		my_arr0 = {
			"article_id": int(id_articles),
			"url": a1,
			"title": articles_dict[a1],
			"full_text": "testing",
		}
		myarticles_dicts.append(my_arr0)
	if not myarticles_dicts:
		return "empty"
	app_json = json.dumps({"articles": myarticles_dicts}, sort_keys=True)
	return app_json


#####
def fullscreenshot(driver, filename):
	height = driver.execute_script("return document.body.scrollHeight")
	driver.set_window_size(1200, height)
	driver.save_screenshot(filename)

def get_status_res(url=url):
	r = requests.get(url)
	return r.status_code

def parse_city_ngs(test="no_test"):
	result1=""
	try:
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--disable-gpu')
		driver = webdriver.Remote(options=chrome_options,
		                          command_executor='http://172.17.0.1:4444/wd/hub',
		                        desired_capabilities={'javascriptEnabled': True})
		driver.implicitly_wait(100)
		driver.get(url)
		result1=get_article(driver.page_source)
		driver.close()
		if test=="test":
			if result1 != "empty":
		         result1="ok"
	except Exception as err:
		print("error: ",err)
	return result1
####
if __name__ == "__main__":
	a=parse_city_ngs()
	print(a)