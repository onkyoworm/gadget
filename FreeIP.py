#coding:utf-8
import requests
import re
from bs4 import BeautifulSoup
import urllib2
import xlwt
import xlrd
import sys


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

header_ip66 = {}


#some global variable
status_code_dict = dict()
page_dirt = dict()
xici_text_list = list()
kuaidaili_text_list = list()
httpdaili_list = list()
ip66_text_list = list()

#function of check & get the website
def pre_work():
	url1_check = requests.get(url1, headers= header_xici)
	url2_check = requests.get(url2, headers= header_kuaidaili)
	url3_check = requests.get(url3, headers= header_httpdaili)
	url4_check = requests.get(url4, headers= header_ip66)

	#dict for store the status_code
	status_code_dict['url1'] = url1_check.status_code
	status_code_dict['url2'] = url2_check.status_code
	status_code_dict['url3'] = url3_check.status_code
	status_code_dict['url4'] = url4_check.status_code
	for key, value in status_code_dict.items():
		print key + str(value)
		if str(value) != '200':
			print({0} + "'s status_code is not 200, please check").format(str(key))

	#dirt for store the page
	page_dirt['url1'] = url1_check.content
	page_dirt['url2'] = url2_check.content
	page_dirt['url3'] = url3_check.content
	page_dirt['url4'] = url4_check.content

	#localize the page
	with open('url1_page.html', 'w+') as f:
		f.writelines(url1_check.content)
	with open('url2_page.html', 'w+') as f:
		f.writelines(url2_check.content)
	with open('url3_page.html', 'w+') as f:
		f.writelines(url3_check.content)
	with open('url4_page.html', 'w+') as f:
		f.writelines(url4_check.content)

#each website's crawler
def xici():

	ip_list = list()

	with open('url1_page.html', 'r') as f:
		soup = BeautifulSoup(f, 'lxml')
	infor = soup.find('table', attrs={'id': re.compile('ip_list')})
	for i in infor.children:
		i = re.sub('<img src="http://fs.xicidaili.com/images/flag/cn.png" alt="Cn">','',str(i))
		i = re.sub('<img alt="Cn" src="http://fs.xicidaili.com/images/flag/cn.png"/>','',str(i))
		i = re.sub('<td class="country"></td>', '',str(i))
		infor_soup = BeautifulSoup(str(i), 'lxml')
		ip_list.append(infor_soup)

	for i in ip_list:
		if str(i.get_text().encode('utf-8')).strip() != None:
			xici_text_list.append(str(i.get_text().encode('utf-8')).strip())

	#Finally xici_text_list store all the information
	with open('123.txt', 'w+') as f:
		for i in xici_text_list:
			f.writelines(i + '\n')
	print sys._getframe().f_code.co_name
'''
def kuaidaili(url2):
	
	#this website divide into two parts: anonymity and normal
	
	infor_list = list()
	#part1--anonymity proxy
	anon = urllib2.urlopen(url2 + 'inha').read()
	#anon = requests.get(url2 + 'inha', headers=header_kuaidaili)
	anon_soup = BeautifulSoup(anon, 'lxml')

	#locate the table
	part1 = anon_soup.find('table', attrs={'class' : re.compile('')})
	for i in part1.children:
		if i != '\n':
			infor_soup = BeautifulSoup(str(i), 'lxml')
			#add infor
			infor_list.append(infor_soup)
	#infor_list[0] is the format of output		
	#print infor_list[0].get_text()

	#others is proxy's detail
	length1 = len(infor_list)
	for i in range(1, length1):
		for j in infor_list[i]:
			print j.get_text()

	infor_list2 = list()
	#part2--normal proxy
	#norm = requests.get(url2 + 'intr', headers=header_kuaidaili)
	norm = urllib2.urlopen(url2 + 'inha').read()
	norm_soup = BeautifulSoup(norm, 'lxml')

	#locate the table
	part2 = norm_soup.find('table', attrs={'class': re.compile('table table-bordered table-striped')})
	for i in part2.children:
		if i != '\n':
			infor_soup2 = BeautifulSoup(str(i), 'lxml')
			#for the same format of output, so do not add name again

	#others is proxy's detail
	length2 = len(infor_list2)
	for i in range(1, length2):
		for j in infor_list2[i]:
			print j.get_text()		
def httpdaili(url3):

	#for avoid banned we store the raw html file

	surf = requests.get(url=url3, headers=header_httpdaili)
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
def ip66(url4):
	
	infor_list = list()

	#locate the information
	surf = urllib2.urlopen(url4).read()
	surf_soup = BeautifulSoup(surf, 'lxml')

	infor = surf_soup.find('table', attrs= {'width': re.compile('100%')})

	for i in infor.children:
		infor_soup = BeautifulSoup(str(i), 'lxml')
		infor_list.append(infor_soup)
		
	# in this website, if you use get_text() directly there will be some problem while display	
	# for i in infor_list:
	# 	print i.get_text()
	match = re.compile(r'<tr>(.*?)</tr>')
	for i in infor_list:
		print i
		print str(match.findall(str(i))) + '2333'
'''

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
	xici()
	#kuaidaili(url2)
	#httpdaili(url3)
	#ip66(url4)
	
	