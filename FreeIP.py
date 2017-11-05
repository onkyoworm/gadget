#coding:utf-8
import requests
import re
from bs4 import BeautifulSoup
import urllib2


url1 = 'http://www.xicidaili.com/'								#西刺
url2 = 'http://www.kuaidaili.com/free/'							#快代理
url3 = 'http://www.httpdaili.com/mfdl/'							#httpdaili
url4 = 'http://www.66ip.cn/'									#66ip

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

def xici(url1):
	surf = requests.get(url=url1, headers=header_xici)
	parse = BeautifulSoup(surf.content, 'lxml')
	print surf.status_code

	#xici_format
	output_format_list = list()										#format use for output standard

	search_table =  parse.find_all(name='table')					#find the table store data
	data = BeautifulSoup(str(search_table[0]), 'lxml')

	output_format =  data.find_all('tr', attrs={'class':re.compile('subtitle')})		#get the format used for output

	#输出格式 共八个
	#国家 代理IP地址 端口 服务器地址 是否匿名 类型 存活时间 验证时间
	for i in output_format[0].text:
		output_format_list.append(i)

	#deal IP's info
	get_IP = data.find_all('tr', attrs={'class':re.compile('(odd)|( )')})			#ps here is a space
	# for j in get_IP[0]:
	# 	print j.string, 
	#print type(len(get_IP))
	# for j in range(len(get_IP)):
	# 	# for k in get_IP[j]:
	# 	# 	#print '{0}--{1}--{2}--{3}--{4}--{5}--{6}--{7}'.format(get_IP[0],get_IP[1],get_IP[2],get_IP[3],get_IP[4],get_IP[5],get_IP[6],get_IP[7])
	# 	# 	print k.string
	# 	cc =  get_IP[j].text
	# 	print cc
	print get_IP[2]

def kuaidaili(url2):
	pass
def httpdaili(url3):

	#for avoid banned we store the raw html file

	surf = requests.get(url=url2, headers=header_httpdaili)
	surf = urllib2.urlopen(url3).read()
	with open('123.html', 'w+') as f:
		f.write(surf)
	f.close()
	#divide into three parts
	analyze = BeautifulSoup(surf, 'lxml')
	
	#part1--Chinese's http proxy
	infor_list1 = list()										#include the name and the ip's detail

	#locate the informations
	part1 = analyze.find('li', attrs={'style': re.compile('position: absolute; left: 10.5px; top: 0px;')})
	for i in part1.table.children:
		if i != '\n':
			infor_soup = BeautifulSoup(str(i), 'lxml')
			#add all infor
			infor_list1.append(infor_soup)

	length1 = len(infor_list1)
	for i in range(length1):
		for j in infor_list1[i]:
			#print j.get_text()
			pass

	#print infor_list1[0].get_text()							
	#infor_list1[0] is the format of name
	#others is ip's detail
	for i in range(1, length1):
		for j in infor_list1[i]:
			#print j.get_text()
			pass

	#######################################################################################################		

	#part2--foreign http proxy
	infor_list2 = list()

	#locate the informations
	part2 = analyze.find('li', attrs={'style': re.compile('position: absolute; left: 410.5px; top: 0px;')})
	for i in part2.table.children:
		if i != '\n':
			infor_soup2 = BeautifulSoup(str(i), 'lxml')
			#add infor
			infor_list2.append(infor_soup2)
	length2 = len(infor_list2)
	for i in range(length2):
		for j in infor_list2[i]:
			#print j.get_text()
			pass
	#print infor_list2[0].get_text()
	#infor_list2[0] is the format of name
	#others is ip's detail
	for i in range(1, length1):
		for j in infor_list2[i]:
			#print j.get_text()
			pass

	#######################################################################################################		

	#part3-- https proxy	
	infor_list3 = list()

	#locate the informations
	part3 = analyze.find('li', attrs={'style': re.compile('position: absolute; left: 810.5px; top: 0px;')})
	for i in part3.table.children:
		if i != '\n':
			infor_soup3 = BeautifulSoup(str(i), 'lxml')
			#add infor
			infor_list3.append(infor_soup3)
	length3 = len(infor_list3)
	for i in range(length3):
		for j in infor_list3[i]:
			#print j.get_text()
			pass
	#print infor_list3[0].get_text()
	#infor_list3[0] is the format of name
	#others is ip's detail
	for i in range(1, length1):
		for j in infor_list3[i]:
			#print j.get_text()
			pass
			
if __name__ == '__main__':
	#xici(url1)
	kuaidaili(url2)
	#httpdaili(url3)
