#!/usr/bin/env python
from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="")
zapi.login("user", "pass" )

hosts = zapi.host.get({ "output": "extend","selectInterfaces" : "extend" })
print "HOST;NOME;IP;DNS"
for y in hosts:
	inter = y[u'interfaces']
	for x in inter:
		ip = x[u'ip']
		dns = x[u'dns']
		print y[u'host'] + ";" + y[u'name'] +  ";" + ip + ";" + dns 
