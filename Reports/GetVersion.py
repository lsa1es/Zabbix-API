#!/usr/bin/env python
from zabbix_api import ZabbixAPI


zapi = ZabbixAPI(server="")
zapi.login("user", "pass" )

print "HOST;ITEM;VERSION"
host_get = zapi.host.get({ "output": "extend" })
for x in host_get:
    hHost = x[u'host']
    hId = x[u'hostid'] 
    item_get = zapi.item.get({ "output" : "extend", "hostids" : hId, "search" : { "key_" : "agent.version" }  })
    for w in item_get:
        iName = w[u'name'] 
        iLv = w[u'lastvalue']
        print hHost + ";" + iName + ";" + iLv
