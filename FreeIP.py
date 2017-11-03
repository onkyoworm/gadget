#coding:utf-8
import requests
import re
from bs4 import BeautifulSoup


url1 = 'http://www.xicidaili.com/'								#西刺
url2 = 'http://www.kuaidaili.com/free/'							#快代理
url3 = 'http://www.httpdaili.com/mfdl/'							#httpdaili
url4 = 'http://www.66ip.cn/'									#66ip

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
	'Cache-Control': 'max-age=0'

}


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

def httpdaili(url2):

	#divide into three parts
	analyze = BeautifulSoup(httpdaili_text, 'lxml')
	
	#part1--Chinese's http proxy
	part1 = analyze.find('li', attrs={'style': re.compile('position: absolute; left: 10.5')})

	#format of output
	name_list = list()
	for i in part1.tr.children:
		if i != '\n':
			name_list.append(i.text) 

	#traverse to get the ip
	ip_list = list()
	for i in part1.table.children:
		if i != '\n':
			cc = BeautifulSoup(str(i), 'lxml')
	#aa = BeautifulSoup(str(ip_list[2]), 'lxml')
	#print aa.text
if __name__ == '__main__': 

	#xici(url1)
	httpdaili(url2)