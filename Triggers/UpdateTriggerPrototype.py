#!/usr/bin/env python
# Luiz Sales
# luiz@lsales.biz - lsales.biz
from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="http://zabbix-frontend/")
zapi.login("user", "pass" )

template_get = zapi.template.get({"output" : "extend" })
for y in template_get:
	tmpId = y[u'templateid']
	tmpHost = y[u'host']
	trigger_proto = zapi.triggerprototype.get({ "search" : { "description": "Critical usage at" }, "output": "extend", "expandExpression": "extend", "templateids" : tmpId})
	for x in trigger_proto:
		trgId = x[u'triggerid']
		trgExp_OLD = x[u'expression']
		trgDsc_OLD = x[u'description']
		trgExp_NEW = "{%s:vfs.fs.size[{#FSNAME},pfree].last()}<{$FS_THRESHOLD}" % (tmpHost)
		trgDsc_NEW = "Particao {#FSNAME}} do host {HOSTNAME}} com {ITEM.VALUE} do {ITEM.VALUE2} tamanho total  de espaco disponivel"		
		trgUP_Exp = zapi.triggerprototype.update({ "triggerid": trgId, "expression": trgExp_NEW })
		trgUP_Dsc = zapi.triggerprototype.update({ "triggerid": trgId, "description": trgDsc_NEW })  
		print trgUP_Exp
		print trgUP_Dsc
