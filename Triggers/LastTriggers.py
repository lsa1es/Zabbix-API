#!/usr/bin/env python
# Luiz Sales
# luiz@lsales.biz

# Ultima trigger ativa com menos de 5 minutos de idade

from datetime import datetime,timedelta
import time 
from zabbix_api import ZabbixAPI

inicio = datetime.now()
START  = time.mktime(inicio.timetuple())
fim = inicio - timedelta(minutes=5)
END = time.mktime(fim.timetuple())

zapi = ZabbixAPI(server="")
zapi.login("", "" )

trigger_get = zapi.trigger.get({ "limit": 1, "expandDescription" : 1, "filter" : { "value" : 1 }, "lastChangeSince": END,
								 "lastChangeTill" : START, "maintenance" : 0, "min_severity" : 2, "monitored" : 1,
								 "output" : "extend", "skipDependent" : 1, "selectHosts": "extend",
								 "selectLastEvent" : "extend", "sortorder": "DESC", "sortfield": "lastchange"})

for x in trigger_get:
	sev = x[u'priority']
	trigger = x[u'description']
 	hosts = x['hosts']
	for y in hosts:
		host = y[u'name']
		print "HOSTNAME: %s TRIGGER: %s SEVERIDADE: %s" % (host,trigger,sev)


