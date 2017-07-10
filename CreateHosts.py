#!/usr/bin/env python
# Luiz Sales
# luiz@lsales.biz

# Criaçao de Host via API

from zabbix_api import ZabbixAPI
import sys

GRUPO = sys.argv[1]
HOST = sys.argv[2]
DNS = sys.argv[3]
IP = sys.argv[4]

zapi = ZabbixAPI(server="")
zapi.login("", "" )

hg = zapi.hostgroup.get({ "output": "extend", "filter": { "name" : GRUPO } })
for x in hg:
	hgId = x[u'groupid']
	print GRUPO
	print hgId
	mkhost = zapi.host.create({ "host": HOST, "status" : 1, "interfaces": [{ "type": 1, "main": 1, "useip": 1, "ip": IP, "dns": DNS, "port": "10050" } ], "groups": [{ "groupid": hgId } ] })


