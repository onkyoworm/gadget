#coding:utf-8
import requests
import re
from bs4 import BeautifulSoup
import urllib2
import xlwt
import xlrd
import sys
import json


url1 = 'http://www.xicidaili.com/'																#西刺
url2_1 = 'http://www.kuaidaili.com/free/inha/'													#快代理   1--高匿
url2_2 = 'http://www.kuaidaili.com/free/intr/'													#快代理   2--普通
url3 = 'http://www.httpdaili.com/mfdl/'															#httpdaili
url4 = 'http://www.66ip.cn/'																	#66ip
url5 = 'http://www.xdaili.cn/ipagent//freeip/getFreeIps?page=1&rows=10'							#讯代理
url6_1 = 'http://www.data5u.com/free/index.shtml'
url6_2 = 'http://www.data5u.com/free/gngn/index.shtml'
url6_3 = 'http://www.data5u.com/free/gnpt/index.shtml'
url6_4 = 'http://www.data5u.com/free/gwgn/index.shtml'
url6_5 = 'http://www.data5u.com/free/gwpt/index.shtml'
#simple of each website headers
header_xici = {
	'Host': 'www.xicidaili.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'zh,zh-CN;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding': 'gzip, deflate',
	'Cookie':'_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWEzMjM4ZTBhOWRjNzMwM2YwOTY4NjU4MjAwMDFjZmJmBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWxxU0psR21ZWFF4emNBWDg5ZDdxVkoxTnNjZXgyaGFUNjBiTDJiNklUZGs9BjsARg%3D%3D--4bde4ddec2e94c160ce16d183d6ab1d722b0d2bb; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1509696149; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1509696149',
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1',
	'If-None-Match': 'W/"cb19fedc96a8d69fbd9a357a170afba0"',
	'Cache-Control': 'max-age=0'}

header_kuaidaili = {}

header_httpdaili = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'zh,zh-CN;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding': 'gzip, deflate',
	'Cookie': 'UM_distinctid=15f7c0cae40449-0f196bd5a175638-4c322f7c-1fa400-15f7c0cae415b0; CNZZDATA4146503=cnzz_eid%3D1168875105-1509614725-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1509698760',
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1',
	'If-Modified-Since': 'Mon, 23 Oct 2017 01:13:45 GMT',
	'If-None-Match': "4a3d552c9c4bd31:a048",
	'Cache-Control': 'max-age=0'}

header_ip66 = {}

header_xdaili = {
	'Host': 'www.xdaili.cn',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'zh,zh-CN;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding': 'gzip, deflate',
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1',
	'Cache-Control': 'max-age=0'
}

header_data5u = {
	'Host': 'www.data5u.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'zh,zh-CN;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding': 'gzip, deflate',
	'Connection': 'keep-alive'
}

#some global variable
status_code_dict = dict()
page_dirt = dict()
xici_text_list = list()
kuaidaili_text_list = list()
httpdaili_text_list = list()
ip66_text_list = list()
xdaili_text_list = list()
data5u_text_list = list()

#function of check & get the website
def pre_work():
	url1_check = requests.get(url1, headers= header_xici)
	url2_1_check = requests.get(url2_1, headers= header_kuaidaili)
	url2_2_check = requests.get(url2_2, headers= header_kuaidaili)
	url3_check = requests.get(url3, headers= header_httpdaili)
	url4_check = requests.get(url4, headers= header_ip66)
	url5_check = requests.get(url5, headers= header_xdaili)
	url6_1_check = requests.get(url6_1, headers = header_data5u)
	url6_2_check = requests.get(url6_2, headers = header_data5u)
	url6_3_check = requests.get(url6_3, headers = header_data5u)
	url6_4_check = requests.get(url6_4, headers = header_data5u)
	url6_5_check = requests.get(url6_5, headers = header_data5u)

	#dict for store the status_code
	status_code_dict['url1'] = url1_check.status_code
	status_code_dict['url2_1'] = url2_1_check.status_code
	status_code_dict['url2_2'] = url2_2_check.status_code
	status_code_dict['url3'] = url3_check.status_code
	status_code_dict['url4'] = url4_check.status_code
	status_code_dict['url5'] = url5_check.status_code
	status_code_dict['url6_1'] = url6_1_check.status_code
	status_code_dict['url6_2'] = url6_2_check.status_code
	status_code_dict['url6_3'] = url6_3_check.status_code
	status_code_dict['url6_4'] = url6_4_check.status_code
	status_code_dict['url6_5'] = url6_5_check.status_code

	for key, value in status_code_dict.items():
		print key + str(value)
		if str(value) != '200':
			print({0} + "'s status_code is not 200, please check").format(str(key))

	#dirt for store the page
	page_dirt['url1'] = url1_check.content
	page_dirt['url2_1'] = url2_1_check.content
	page_dirt['url2_2'] = url2_2_check.content
	page_dirt['url3'] = url3_check.content
	page_dirt['url4'] = url4_check.content
	page_dirt['url5'] = url5_check.content
	page_dirt['url6_1'] = url6_1_check.content
	page_dirt['url6_2'] = url6_2_check.content
	page_dirt['url6_3'] = url6_3_check.content
	page_dirt['url6_4'] = url6_4_check.content
	page_dirt['url6_5'] = url6_5_check.content

	#localize the page
	with open('url1_page.html', 'w+') as f:
		f.writelines(url1_check.content)
	with open('url2_1_page.html', 'w+') as f:
		f.writelines(url2_1_check.content)
	with open('url2_2_page.html', 'w+') as f:
		f.writelines(url2_2_check.content)
	with open('url3_page.html', 'w+') as f:
		f.writelines(url3_check.content)
	with open('url4_page.html', 'w+') as f:
		f.writelines(url4_check.content)
	with open('url5_page.html', 'w+') as f:
		f.writelines(url5_check.content)
	with open('url6_1_page.html', 'w+') as f:
		f.writelines(url5_check.content)
	with open('url6_2_page.html', 'w+') as f:
		f.writelines(url5_check.content)
	with open('url6_3_page.html', 'w+') as f:
		f.writelines(url5_check.content)
	with open('url6_4_page.html', 'w+') as f:
		f.writelines(url5_check.content)
	with open('url6_5_page.html', 'w+') as f:
		f.writelines(url5_check.content)

#each website's crawler
def xici():

	ip_list = list()
	name = sys._getframe().f_code.co_name

	with open('url1_page.html', 'r') as f:
		soup = BeautifulSoup(f, 'lxml')
	infor = soup.find('table', attrs={'id': re.compile('ip_list')})
	for i in infor.children:
		i = re.sub('<img src="http://fs.xicidaili.com/images/flag/cn.png" alt="Cn">','',str(i))
		i = re.sub('<img alt="Cn" src="http://fs.xicidaili.com/images/flag/cn.png"/>','',str(i))
		i = re.sub('<td class="country"></td>', '',str(i))
		i = i.replace('</td>\n<td>', '</td>-<td>').replace('</td>\n<td class="country">', '</td>-<td class="country">')
		infor_soup = BeautifulSoup(str(i.strip()), 'lxml')
		ip_list.append(infor_soup)
	for i in ip_list:
		if str(i.get_text().encode('utf-8')).strip() != None:
			xici_text_list.append(str(i.get_text().encode('utf-8')).strip())

	#Finally xici_text_list store all the information
	with open(name + '.txt', 'w+') as f:
		for i in xici_text_list:
			f.writelines(i + '\n')

def kuaidaili():

	name = sys._getframe().f_code.co_name
	ip_list = list()
	with open('url2_1_page.html', 'r') as f1:
		soup1 = BeautifulSoup(f1, 'lxml')
	with open('url2_2_page.html', 'r') as f2:
		soup2 = BeautifulSoup(f2, 'lxml')
	infor_1 = soup1.find('table', attrs={'class': re.compile('table table-bordered table-striped')})
	infor_2 = soup2.find('table', attrs={'class': re.compile('table table-bordered table-striped')})

	for i in infor_1.children:
		infor_soup = BeautifulSoup(str(i), 'lxml')
		if len(infor_soup.get_text()) > 1:
			ii = BeautifulSoup(str(infor_soup).replace('</td>\n', '</td>-'), 'lxml')
			ip_list.append(ii)
	for i in infor_2.children:
		infor_soup = BeautifulSoup(str(i), 'lxml')
		if len(infor_soup.get_text()) > 1:
			ii = BeautifulSoup(str(infor_soup).replace('</td>\n', '</td>-'), 'lxml')
			ip_list.append(ii)
			#print ii.get_text()

	for i in ip_list:
		# if str(i.get_text().encode('utf-8')).strip() != None:
		# 	kuaidaili_text_list.append(str(i.get_text().encode('utf-8')).strip())
		# 	print(i.get_text().encode('utf-8')).strip()
		kuaidaili_text_list.append(str(i.get_text().encode('utf-8')))
	with open(name + '.txt', 'w+') as f:
		for i in kuaidaili_text_list:
			f.writelines(i + '\n')

def httpdaili():

	name = sys._getframe().f_code.co_name
	ip_list = list()

	with open('url3_page.html', 'r') as f:
		soup = BeautifulSoup(f, 'lxml')
	infor1 = soup.find('li', attrs={'style': re.compile('position: absolute; left: 10.5px; top: 0px;')})
	infor2 = soup.find('li', attrs={'style': re.compile('position: absolute; left: 410.5px; top: 0px;')})
	infor3 = soup.find('li', attrs={'style': re.compile('position: absolute; left: 810.5px; top: 0px;')})

	for i in infor1.children:
		infor_soup = BeautifulSoup(str(i).replace('</td>\n', '</td>-'), 'lxml')
		ip_list.append(infor_soup)
	for i in infor2.children:
		infor_soup = BeautifulSoup(str(i).replace('</td>\n', '</td>-'), 'lxml')
		ip_list.append(infor_soup)
	for i in infor3.children:
		infor_soup = BeautifulSoup(str(i).replace('</td>\n', '</td>-'), 'lxml')
		ip_list.append(infor_soup)

	for i in ip_list:
		if str(i.get_text().encode('utf-8')).strip() != None:
			httpdaili_text_list.append(str(i.get_text().encode('utf-8')).strip())
	with open(name + '.txt', 'w+') as f:
		f.writelines(httpdaili_text_list)

def ip66():

	ip_list = list()
	name = sys._getframe().f_code.co_name

	with open('url4_page.html', 'r') as f:
		soup = BeautifulSoup(f, 'lxml')
	infor = soup.find('table', attrs={'width': re.compile('100%')})
	for i in infor.children:
		b = str(i).replace('</td><td>', '-</td><td>')
		infor_soup = BeautifulSoup(b, 'lxml')
		ip_list.append(infor_soup)
	for i in ip_list:
		if str(i.get_text().encode('utf-8')).strip() != None:
			ip66_text_list.append(str(i.get_text().encode('utf-8')).strip())
	with open(name + '.txt', 'w+') as f:
		for i in ip66_text_list:
			f.writelines(i + '\n')

def xdaili():
	name = sys._getframe().f_code.co_name

	with open('url5_page.html', 'r') as f:
		raw_dict = json.loads(f.read())
	raw_list = raw_dict['RESULT']['rows']
	for i in raw_list:
		#'{0}-{1}-{2}-{3}-{4}-{5}-{6}'.format(i['ip'],i['port'],i['position'],i['anony'],i['responsetime'],i['validatetime'],i['type'])
		final_text = i['ip']+'-'+i['port']+'-'+i['position']+'-'+i['anony']+'-'+i['responsetime']+'-'+i['validatetime']+'-'+i['type']
		xdaili_text_list.append(final_text)
	with open(name + '.txt', 'w+') as f:
		for i in xdaili_text_list:
			f.writelines(i.encode('utf-8') + '\n')

def data5u():
	name = sys._getframe().f_code.co_name  

	for ii in range(1, 6):
		mesg_name = 'url6_' + str(ii) + '_page.html'
		with open(mesg_name, 'r') as f:
			raw_dict = json.loads(f.read())
			raw_list = raw_dict['RESULT']['rows']  
		for i in raw_list:
			#'{0}-{1}-{2}-{3}-{4}-{5}-{6}'.format(i['ip'],i['port'],i['position'],i['anony'],i['responsetime'],i['validatetime'],i['type'])
			final_text = i['ip']+'-'+i['port']+'-'+i['position']+'-'+i['anony']+'-'+i['responsetime']+'-'+i['validatetime']+'-'+i['type']+'-'+i['post']
			data5u_text_list.append(final_text)
	with open(name + '.txt', 'w+') as f:
		for i in data5u_text_list:
			f.writelines(i.encode('utf-8') + '\n')

#define the format of output
def output_format(target_list, current_function_name):
	workbook = xlwt.Workbook(encoding= 'utf-8')
	worksheet = workbook.add_sheet(current_function_name)
	for target in target_list:
		for i in range(len(target_list)):
			for j in range(len(target_list)):
				worksheet.write(i, j, target.get_text())
	workbook.save('12.xls')
			
if __name__ == '__main__':
	pre_work()
	xici()
	kuaidaili()
	httpdaili()
	ip66()
	xdaili()
	data5u()