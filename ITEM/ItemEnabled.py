#!/usr/bin/env python
# Luiz Sales
# luiz@lsales.biz

# Habilitar o item  baseado na chave que ele recebe

from zabbix_api import *
import sys

HOST = sys.argv[1]
CHAVE = sys.argv[2]

zapi = ZabbixAPI(server="")
zapi.login("", "" )

host_get = zapi.host.get({ "output": "hostid", "filter": { "name" : HOST } })
for x in host_get:
	hId = x[u'hostid']
	item_get = zapi.item.get({ "output": "extend", "hostids" : hId, "search" : { "key_" : CHAVE } })
	for w in item_get:
		iId = w[u'itemid']
		item_update = zapi.item.update({ "itemid" : iId, "status": 0 }) 
		

