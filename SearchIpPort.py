#!/usr/bin/env python
# Luiz Sales
# luiz@lsales.biz 

import sys
from zabbix_api import ZabbixAPI

HOST = sys.argv[1]

zapi = ZabbixAPI(server="")
zapi.login("", "" )

host = zapi.host.get({ "output": "extend", "selectInterfaces": "extend", "filter" : { "host" : HOST } })
for x in host:
    inter = x[u'interfaces'] 
    for w in inter: 
        print "IP: %s PORTA: %s " % (w[u'ip'],w[u'port'] )
         
