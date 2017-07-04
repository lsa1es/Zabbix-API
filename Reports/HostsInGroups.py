#!/usr/bin/env python
from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="")
zapi.login("user", "pass" )

hg = zapi.hostgroup.get({ "output" : "extend"  }) 
for x in hg:
	grpid = x[u'groupid']
	host_get = zapi.host.get({ "output" : "extend", "groupids": grpid })
	for w in host_get:
		print x[u'name'] + ";" + w[u'host'] + ";" + w[u'name'] 
