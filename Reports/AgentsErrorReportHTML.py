#!/usr/bin/env python
from zabbix_api import ZabbixAPI


zapi = ZabbixAPI(server="")
zapi.login("user", "pass" )

hosts = zapi.host.get({ "output": ["host", "name", "description", "status","proxy_hostid", "error"  ], "filter": { "available": 2 } } )
error = open('ErrorReport.csv', 'w')
print "<table>"
print "<tr>"
print "<td>HOST</td>"
print "<td>NOME</td>"
print "<td>ERROR</td>"
print "<td>STATUS</td>"
print "<td>PROXY</td>"
print "</tr>"

#print "HOST;NOME;STATUS;ERROR;LAST ACCESS;ON/OFF;PROXY"


for y in hosts:
	proxyid = y[u'proxy_hostid']
	#proxy = zapi.proxy.get({ "output": [ "host" ], "filter": { "proxyid": proxyid } })
	#for w in proxy:
	#	print y[u'host']
#		print w
	print "<tr>"
	print "<td>%s</td>" % (y[u'host']) 
	print "<td>%s</td>"	% (y[u'name'])
	print "<td>%s</td>" % (y[u'error'])
	print "<td>%s</td>" % (y[u'status'])
	print "<td>%s</td>" % (y[u'proxy_hostid'])
	print "</tr>"

#print y[u'host'] + ";" + y[u'name'] +  ";" + y[u'error'] +  ";" + y[u'status'] +  ";" + y[u'proxy_hostid']
	

print "</table>"
