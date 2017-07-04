#!/usr/bin/env python
from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="")
zapi.login("","")

print "HOST;GROUP;TEMPLATES"
host_get = zapi.host.get({ "output": "extend", "selectGroups" : "extend", "selectParentTemplates": "extend" })
for x in host_get:
	tmpl = x[u'parentTemplates']
	grps = x[u'groups']
	host = x[u'host']
	for w in grps:
		gname = w[u'name']
	for y in tmpl:
		tname = y[u'name']
		print "%s;%s;%s" % (host,gname,tname)
