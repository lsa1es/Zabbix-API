#!/usr/bin/env python
# Luiz Sales
# luiz@lsales.biz

# Fila de Items com atraso
# TODO: convert 'que' para datetime

import time
from zabbix_api import ZabbixAPI
now = time.time()

zapi = ZabbixAPI(server="")
zapi.login("", "" )

hg = zapi.hostgroup.get({ "output" : "extend" })
for w in hg:
	gId = w[u'groupid']
	item_get = zapi.item.get({ "selectHosts": "extend", "output": "extend", "groupids": gId  })
	for x in item_get:
		name = x[u'name']
		key = x[u'key_']
		delay = x[u'delay']
		lastc = x[u'lastclock']
		hosts = x[u'hosts']
		for y in hosts:
			hname = y[u'host']

			que = int(now) - int(lastc)
			if que > int(delay):
				print "HOST: %s | ITEM: %s | Delay: %s | Tempo sem dado: %d" % (hname,name,delay,que)


