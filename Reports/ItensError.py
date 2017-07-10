#!/usr/bin/env python
# Luiz Sales
# luiz@lsales.biz

# Relatorio de Item com Erros

import os
import ast
from zabbix_api import ZabbixAPI


#zapi = ZabbixAPI(server="")
#zapi.login("", "" )

hosts = zapi.host.get({ "output": ["host", "name", "description", "status", "available", "proxy_hostid", "error", "lastaccess"  ] } )
#error = open('ErrorReport.csv', 'w')
print "NOME;HOST;ITEM;KEY;ERROR"

for x in hosts:
	hostId = x[u'hostid']
	hname = x[u'name']
	hhost = x[u'host'] 
	item_get = zapi.item.get({ "output" : "extend", "hostids": hostId, "filter" : { "state" : 1 , "status" : 0 }  })
	for y in item_get:
		iname = y[u'name'] 
		ikey = y[u'key_']
		ierror = y[u'error'] 
		print hname + ";" + hhost + ";" + iname + ";" + ikey + ";" + ierror  
