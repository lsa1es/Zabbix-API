#!/usr/bin/env python
# Luiz Sales
# luiz@lsales.biz

# Criar UserMacro de um host especifico 

from zabbix_api import ZabbixAPI
import sys
import ast

HOST = sys.argv[1]
MACRO = sys.argv[2]
VALOR = sys.argv[3]

zapi = ZabbixAPI(server="http://apizabbix.mandic.net.br/")
zapi.login("zbxsystem", "YTg5OTU4YiAgLQo=" )

host_get = zapi.host.get({ "output" : "hostid", "filter" : { "host" : [ HOST ] } })
for  x in host_get:
	hostId = x[u'hostid']

macro_mk = zapi.usermacro.create({ "hostid": hostId, "macro": MACRO, "value": VALOR })
