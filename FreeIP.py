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
url7 = 'http://www.goubanjia.com/'
url8 = 'http://www.ip181.com/'
url9 = 'http://www.proxy360.cn/Proxy'
url10 = 'http://www.ip3366.net/'
url11 = 'http://ip.baizhongsou.com/'
url12 = 'http://www.pcdaili.com/index.php?m=daili&a=free&type=1'
url13 = 'http://www.nianshao.me/'
url14 = 'http://www.yun-daili.com/free.asp'				
url15 = 'http://www.httpsdaili.com/'					
url16 = 'http://www.iphai.com/free/ng'					
url17 = 'http://www.superfastip.com/'					
url18 = 'http://www.xsdaili.com/'						#lack
url19 = 'http://www.meiridaili.com/'					#lack
url20 = 'https://proxy.coderbusy.com/zh-cn/classical/anonymous-type/anonymous.aspx'
url21 = 'http://47.94.199.58:8080/proxyipcenter/proxyCenter/proxy/list'
url22 = 'https://www.hvaexlove.com/'

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

header_goubanjia = {
	'Host': 'www.goubanjia.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'zh,zh-CN;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding': 'gzip, deflate',
	'Referer': 'https://www.goubanjia.com/',
	'Connection': 'keep-alive'
}

header_ip181 = {
	
}

header_proxy360 = {
	
}

header_ip3366 = {
	
}

header_baizhongshou = {
	
}

header_pcdaili = {
	
}

header_nianshao = {
	
}

header_yundaili = {
	
}

header_httpsdaili = {
	
}

header_iphai = {
	
}

header_superfastip = {
	
}

header_coderbusy = {
	
}

header_iwfreevpn = {
	'Host': '47.94.199.58:8080',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Accept-Language': 'zh,zh-CN;q=0.8,en-US;q=0.5,en;q=0.3',
	'Referer': 'http://www.iwfreevpn.top/',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Origin': 'http://www.iwfreevpn.top'
}

post_iwfreevpn = {'size': '10', 'page': '0', 'sort': 'newest_date%2Cdesc'}

header_hvaexlove = {
	
}

#some global variable
status_code_dict = dict()
page_dirt = dict()

sum_raw_text_list = list()

xici_text_list = list()
kuaidaili_text_list = list()
httpdaili_text_list = list()
ip66_text_list = list()
xdaili_text_list = list()
data5u_text_list = list()
goubanjia_text_list = list()
ip181_text_list = list()
proxy360_text_list = list()
ip3366_text_list = list()
baizhongsou_text_list = list()
pcdaili_text_list = list()
nianshao_text_list = list()
yundaili_text_list = list()
httpsdaili_text_list = list()
iphai_text_list = list()
superfastip_text_list = list()
coderbusy_text_list = list()
iwfreevpn_text_list = list()
hvaexlove_text_list = list()


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
	url7_check = requests.get(url7, headers= header_goubanjia)
	url8_check = requests.get(url8, headers= header_ip181)
	url9_check = requests.get(url9, headers= header_proxy360)
	url10_check = requests.get(url10, headers= header_ip3366)
	url11_check = requests.get(url11, headers= header_baizhongshou)
	url12_check = requests.get(url12, headers= header_pcdaili)
	url13_check = requests.get(url13, headers= header_nianshao)
	url14_check = requests.get(url14, headers= header_yundaili)
	url15_check = requests.get(url15, headers= header_httpsdaili)
	url16_check = requests.get(url16, headers= header_iphai)
	url17_check = requests.get(url17, headers= header_superfastip)
	url20_check = requests.get(url20, headers= header_coderbusy)
	url21_check = requests.post(url21, headers= header_iwfreevpn, data= json.dumps(post_iwfreevpn))
	url22_check = requests.get(url22, headers = header_hvaexlove)


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
	status_code_dict['url7'] = url7_check.status_code
	status_code_dict['url8'] = url8_check.status_code
	status_code_dict['url9'] = url9_check.status_code
	status_code_dict['url10'] = url10_check.status_code
	status_code_dict['url11'] = url11_check.status_code
	status_code_dict['url12'] = url12_check.status_code
	status_code_dict['url13'] = url13_check.status_code
	status_code_dict['url14'] = url14_check.status_code
	status_code_dict['url15'] = url15_check.status_code
	status_code_dict['url16'] = url16_check.status_code
	status_code_dict['url17'] = url17_check.status_code
	status_code_dict['url20'] = url20_check.status_code
	status_code_dict['url21'] = url21_check.status_code
	status_code_dict['url22'] = url22_check.status_code

	for key, value in status_code_dict.items():
		print key + ' is ' + str(value)
		if str(value) != '200':
			print(str(key) + "'s status_code is not 200, please check")

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
	page_dirt['url7'] = url7_check.content
	page_dirt['url8'] = url8_check.content
	page_dirt['url9'] = url9_check.content
	page_dirt['url10'] = url10_check.content
	page_dirt['url11'] = url11_check.content
	page_dirt['url12'] = url12_check.content
	page_dirt['url13'] = url13_check.content
	page_dirt['url14'] = url14_check.content
	page_dirt['url15'] = url15_check.content
	page_dirt['url16'] = url16_check.content
	page_dirt['url17'] = url17_check.content
	page_dirt['url20'] = url20_check.content
	page_dirt['url21'] = url21_check.content
	page_dirt['url22'] = url22_check.content

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
		f.writelines(url6_1_check.content)
	with open('url6_2_page.html', 'a+') as f:
		f.writelines(url6_2_check.content)
	with open('url6_3_page.html', 'a+') as f:
		f.writelines(url6_3_check.content)
	with open('url6_4_page.html', 'a+') as f:
		f.writelines(url6_4_check.content)
	with open('url6_5_page.html', 'a+') as f:
		f.writelines(url6_5_check.content)
	with open('url7_page.html', 'w+') as f:
		f.writelines(url7_check.content)
	with open('url8_page.html', 'w+') as f:
		f.writelines(url8_check.content)
	with open('url9_page.html', 'w+') as f:
		f.writelines(url9_check.content)
	with open('url10_page.html', 'w+') as f:
		f.writelines(url10_check.content)
	with open('url11_page.html', 'w+') as f:
		f.writelines(url11_check.content)
	with open('url12_page.html', 'w+') as f:
		f.writelines(url12_check.content)
	with open('url13_page.html', 'w+') as f:
		f.writelines(url13_check.content)
	with open('url14_page.html', 'w+') as f:
		f.writelines(url14_check.content)
	with open('url15_page.html', 'w+') as f:
		f.writelines(url15_check.content)
	with open('url16_page.html', 'w+') as f:
		f.writelines(url16_check.content)
	with open('url17_page.html', 'w+') as f:
		f.writelines(url17_check.content)
	with open('url20_page.html', 'w+') as f:
		f.writelines(url20_check.content)
	with open('url21_page.html', 'w+') as f:
		f.writelines(url21_check.content)
	with open('url22_page.html', 'w+') as f:
		f.writelines(url22_check.content)

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

	for i in ip_list:
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

	# for ii in range(2, 6):
	# 	mesg_name = 'url6_' + str(ii) + '_page.html'
	# 	with open(mesg_name, 'r') as f:
	# 		raw_dict = json.loads(str(f))
	# 		raw_list = raw_dict['RESULT']['rows']  
	# 	for i in raw_list:
	# 		final_text = i['ip']+'-'+i['port']+'-'+i['position']+'-'+i['anony']+'-'+i['responsetime']+'-'+i['validatetime']+'-'+i['type']+'-'+i['post']
	# 		data5u_text_list.append(final_text)
	# with open(name + '.txt', 'w+') as f:
	# 	for i in data5u_text_list:
	# 		f.writelines(i.encode('utf-8') + '\n')
	with open('url6_2_page.html', 'r') as f:
		print f.read()

def goubanjia():
	name = sys._getframe().f_code.co_name
	ip_list = list()

	with open('url7_page.html', 'r') as f:
		soup = BeautifulSoup(f, 'lxml')
	infor = soup.find('table', attrs={'class': re.compile('table')})
	for i in infor.children:
		kill_none1 = re.compile('<p style="display:none;">.*?</p>')
		kill_none2 = re.compile('<p style="display: none;">.*?</p>')
		kill_space = re.compile('[\s]+<a class="href" href="http://www.goubanjia.com/free/.*?">')
		format_output = re.compile('</td>\n')
		i = kill_none1.sub("", str(i))
		i = kill_none2.sub("", str(i))
		i = kill_space.sub("", str(i))
		i = format_output.sub('</td>-', str(i))
		infor_soup = BeautifulSoup(str(i), 'lxml')
		goubanjia_text_list.append(infor_soup.get_text().encode('utf-8'))
		#print infor_soup.get_text()
	with open(name + '.txt', 'w+') as f:
		for i in goubanjia_text_list:
			f.writelines(i)

def ip181():
	name = sys._getframe().f_code.co_name
	ip_list = list()

	with open('url8_page.html', 'r') as f:
		soup = BeautifulSoup(f, 'lxml')
	infor = soup.find('table', attrs={'class': re.compile('table table-hover panel-default panel ctable')})
	for i in infor.children:
		i = str(i).replace('</td>\n', '</td>-')
		infor_soup = BeautifulSoup(str(i), 'lxml')
		ip_list.append(infor_soup)
	for i in ip_list:
		if str(i.get_text().encode('utf-8')).strip() != None:
			ip181_text_list.append(str(i.get_text().encode('utf-8')).strip())
	with open(name + '.txt', 'w+') as f:
		f.writelines(ip181_text_list)

def proxy360():
	name = sys._getframe().f_code.co_name

	with open('url9_page.html', 'r') as f:
		soup = BeautifulSoup(f, 'lxml')

	infor = soup.findAll('div', attrs={'class': re.compile('proxylistitem')})
	for i in infor:
		ii = re.sub('\s', '', str(i))
		ii = BeautifulSoup(ii.replace('','').replace('</','-</'), 'lxml')
		proxy360_text_list.append(ii.spanclass.get_text().encode('utf-8'))
		print ii.get_text()

	with open(name + '.txt', 'w+') as f:
		for i in proxy360_text_list:
			f.writelines(i + '\n')
 
def ip3366():
	name = sys._getframe().f_code.co_name
	ip_list = list()

	with open('url10_page.html', 'r') as f:
		soup = BeautifulSoup(f, 'lxml')
	infor = soup.find('table', attrs={'class': re.compile('table table-bordered table-striped')})
	for i in infor.children:
		i = str(i).replace('</td>\n', '</td>-')
		infor_soup = BeautifulSoup(str(i), 'lxml')
		ip_list.append(infor_soup)
	for i in ip_list:
		if str(i.get_text().encode('utf-8')).strip() != None:
			ip3366_text_list.append(str(i.get_text().encode('utf-8')))
	with open(name + '.txt', 'w+') as f:
		f.writelines(ip3366_text_list)

def baizhongshou():
	name = sys._getframe().f_code.co_name

	with open('url11_page.html', 'r') as f:
		soup = BeautifulSoup(f, 'lxml')
	infor = soup.find('div', attrs={'class': re.compile('daililist')})
	infor = str(infor).replace(':', '-')
	infor = str(infor).replace('</td>', '-</td>')
	infor_soup = BeautifulSoup(infor, 'lxml')
	baizhongsou_text_list.append(infor_soup.get_text().encode('utf-8'))
	with open(name + '.txt', 'w+') as f:
		f.writelines(str(infor_soup.get_text().encode('utf-8')))

def pcdaili():
	name = sys._getframe().f_code.co_name

	with open('url12_page.html', 'r') as f:
		soup = BeautifulSoup(f, 'lxml')
	infor = soup.find('table', attrs={'class': re.compile('table table-striped')})
	for i in infor.children:
		infor_soup = BeautifulSoup(str(i).replace('</td>\n', '</td>-'), 'lxml')
		pcdaili_text_list.append(infor_soup.get_text().encode('utf-8'))
	with open(name + '.txt', 'w+') as f:
		for i in pcdaili_text_list:
			f.writelines(i)

def nianshao():
	name = sys._getframe().f_code.co_name

	with open('url13_page.html', 'r') as f:
		soup = BeautifulSoup(f, 'lxml')
	infor = soup.find('table', attrs={'class': re.compile('table')})
	for i in infor.children:
		infor_soup = BeautifulSoup(str(i).replace('</td>\n', '</td>-'), 'lxml')
		nianshao_text_list.append(infor_soup.get_text().encode('utf-8'))

	with open(name + '.txt', 'w+') as f:
		for i in nianshao_text_list:
			f.writelines(i)

def yundaili():
	name = sys._getframe().f_code.co_name

	with open('url14_page.html', 'r') as f:
		soup = BeautifulSoup(f, 'lxml')
	infor = soup.find('table', attrs={'class': re.compile('table table-bordered table-striped')})
	for i in infor.children:
		i = str(i).replace('</td>\n', '</td>-')
		i = BeautifulSoup(i, 'lxml')
		yundaili_text_list.append(i.get_text().encode('utf-8'))

	with open(name + '.txt', 'w+') as f:
		for i in yundaili_text_list:
			f.writelines(i)

def httpsdaili():
	name = sys._getframe().f_code.co_name

	with open('url15_page.html', 'r') as f:
		soup = BeautifulSoup(f, 'lxml')
	infor = soup.find('table', attrs={'class': re.compile('table table-bordered table-striped')})
	for i in infor.children:
		i = str(i).replace('</td>\n', '</td>-')
		i = BeautifulSoup(i, 'lxml')
		httpsdaili_text_list.append(i.get_text().encode('utf-8'))

	with open(name + '.txt', 'w+') as f:
		for i in httpsdaili_text_list:
			f.writelines(i)

def iphai():
	name = sys._getframe().f_code.co_name

	with open('url16_page.html', 'r') as f:
		soup = BeautifulSoup(f, 'lxml')
	infor = soup.find('table', attrs={'class': re.compile('table table-bordered table-striped table-hover')})
	infor = re.sub('\s', '', str(infor))
	infor = infor.replace('</tr>', '</tr>\n')
	infor = BeautifulSoup(infor.replace('</td>', '</td>-'), 'lxml')
	iphai_text_list.append(infor.get_text().encode('utf-8'))

	with open(name + '.txt', 'w+') as f:
		for i in iphai_text_list:
			f.writelines(i)

def superfastip():
	name = sys._getframe().f_code.co_name

	with open('url17_page.html', 'r') as f:
		soup = BeautifulSoup(f, 'lxml')
	infor = soup.find('table', attrs= {'id': re.compile('iptable11')})
	infor = str(infor).replace('<td>中国</td>', '')
	infor = str(infor).replace('</td>\n', '</td>-')
	infor = BeautifulSoup(infor, 'lxml')
	superfastip_text_list.append(infor.get_text().encode('utf-8'))

	with open(name + '.txt', 'w+') as f:
		for i in superfastip_text_list:
			f.writelines(i)

def coderbusy():
	name = sys._getframe().f_code.co_name

	with open('url20_page.html', 'r') as f:
		soup = BeautifulSoup(f, 'lxml')

	soup = soup.find('table', attrs={'class': re.compile('table proxy-server-table')})
	soup = re.sub('<span class=".*?"></span>', '', str(soup))
	soup = re.sub('\s', '', str(soup))
	soup = re.sub('</tr>', '</tr>\n', str(soup))
	soup = re.sub('</td>', '</td>-', str(soup))
	infor = BeautifulSoup(soup, 'lxml')
	coderbusy_text_list.append(infor.get_text().encode('utf-8'))

	with open(name + '.txt', 'w+') as f:
		for i in coderbusy_text_list:
			f.writelines(i)

def iwfreevpn():
	name = sys._getframe().f_code.co_name

	with open('url21_page.html', 'r') as f:
		raw_dict =  json.loads(f.read())
	raw_list =  raw_dict['data']['content']
	for i in raw_list:
		final_output =  str(i['ip']) + '-' + str(i['port']) + '-' + i['country'].encode('utf-8') + '\n'
		iwfreevpn_text_list.append(final_output)
	with open(name + '.txt', 'w+') as f:
		f.writelines(iwfreevpn_text_list)

def hvaexlove():
	name = sys._getframe().f_code.co_name

	with open('url22_page.html', 'r') as f:
		soup = BeautifulSoup(f, 'lxml')
	infor = soup.find('table')
	infor = str(infor).replace('</td>\n', '</td->')
	infor = BeautifulSoup(infor, 'lxml')
	hvaexlove_text_list.append(infor.get_text().encode('utf-8'))

	with open(name + '.txt', 'w+') as f:
		for i in header_hvaexlove:
			f.writelines(i)

def test_output():
	# for i in xici_text_list:
	# 	print i
	# for i in kuaidaili_text_list:
	# 	print i
	# for i in httpdaili_text_list:
	# 	print i
	# for i in ip66_text_list:
	# 	print i
	# for i in xdaili_text_list:
	# 	print i 
	# data5u_text_list 
	# for i in goubanjia_text_list:
	# 	print i 
	# for i in ip181_text_list:
	# 	print i
	# for i in proxy360_text_list:
	# 	print i
	# for i in ip3366_text_list:
	# 	print i 
	# for i in baizhongsou_text_list:
	# 	print i
	# for i in pcdaili_text_list:
	# 	print i 
	# for i in nianshao_text_list:
	# 	print i 
	# for i in yundaili_text_list:
	# 	print i 
	# for i in httpsdaili_text_list:
	# 	print i 
	# for i in iphai_text_list:
	# 	print i 
	# for i in superfastip_text_list:
	# 	print i 
	# for i in coderbusy_text_list:
	# 	print i 
	# for i in iwfreevpn_text_list:
	# 	print i 
	# for i in hvaexlove_text_list:
	# 	print i
	pass 

def sum_raw_text():
	name = sys._getframe().f_code.co_name

	#Use for sum the information from other list 
	#But not all list in a format
	#So we have to dispose it first
	#We will show each list's format & how we deal with it below

	

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
	#pre_work()
	#xici()			-
	#kuaidaili()    -
	#httpdaili()	-
	#ip66()			-
	#xdaili()		-
	#data5u()
	#goubanjia()	-
	#ip181()		-
	#proxy360()
	#ip3366()		-
	#baizhongshou()	-
	#pcdaili()		-
	#nianshao()		-
	#yundaili()		-
	#httpsdaili()	-
	#iphai()		-
	#superfastip()	-
	#coderbusy()	-
	#iwfreevpn()	-
	#hvaexlove()	-

	#test_output()