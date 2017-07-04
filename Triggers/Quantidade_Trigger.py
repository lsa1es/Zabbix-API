#!/usr/bin/env python

from zabbix_api import *
import sys

GRUPO = sys.argv[1]
SEV = sys.argv[2]

zapi = ZabbixAPI(server="")
zapi.login("p", "" )

hg = zapi.hostgroup.get({ "output": "extend", "search": { "name": [ GRUPO ] } })
qntd_grp = []
for x in hg:
	hgId =  x[u'groupid']
 	trigger_get = zapi.trigger.get({ "skipDependent" : 1, "active" : 1, "monitored" : 1, "filter": { "value" : 1, "priority": SEV  } ,  "only_true": 1, "output": "extend", "groupids" : hgId })
	qntd_grp.append(len(trigger_get))

print sum(qntd_grp)
