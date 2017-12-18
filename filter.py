#coding:utf-8

import re

map_dict = dict()

with open('port-server.txt', 'r') as f:
	alist = f.readlines()
	for i in alist:
		# sometimes this re go wrong
		# dd = re.match('(?P<server>\w+)\s+(?P<port>\d+)\s+(?P<linkway>tcp|udp)+', str(i).replace('\n', ' '))
		# "server:{0}-port:{1}-link:{2}".format(bb.group('server'), bb.group('port'), bb.group('linkway'))
		toSpace = re.sub('\s', '-', i)
		split = toSpace.split('--')
		#print '{server}, {port}, {linkway}'.format(server=str(split[0]), port=split[1], linkway=split[2])
		detail_list = list()
		detail_set = set()
		if map_dict.has_key(split[1]):
			map_dict[split[1]] = detail_list.append(detail_set.add(str(split[0] +'-'+ split[2])))
		else:
			map_dict = { split[1] : detail_list.append(detail_set.add(str(split[0] +'-'+ split[2])))} # port:detail


