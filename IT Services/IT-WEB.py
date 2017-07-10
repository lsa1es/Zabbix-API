#!/usr/bin/env python
# Luiz Sales
# luiz@lsales.biz

# Criacao de Arvore IT Service baseado nos itens de WEB do Host: Web URLs PRD, ja criando a trigger junto com o item.


from zabbix_api import *

zapi = ZabbixAPI(server="")
zapi.login("", "" )

host = zapi.host.get({ "output": "extend", "filter": { "host": "Web URLs PRD" } })
for x in host:
	hId = x[u'hostid']
	name = x[u'name']
	host = x[u'host']
	print "%s %s %s " % (hId,name,host)
	mk = zapi.service.create({ "name": host, "algorithm": 1, "showsla": 1, "goodsla": 95.00, "sortorder": 1 })
	items = zapi.item.get ({ "output": "extend", "webitems": 1, "with_triggers": 1, "selectTriggers": "extend", "hostids" : hId })
	for w in items:
		get_pai = zapi.service.get({ "output": "name", "filter": { "name": host } })
		for a in get_pai:
			sId = a[u'serviceid']
		
		it_name = w[u'name']
		it_trg = w[u'triggers'] 
		for a in it_trg:
			it_trgId = a[u'triggerid']
			it_desc = a[u'description']
			
		trigger = zapi.service.create({ "name": it_desc, "algorithm": 1, "showsla": 1, "goodsla": 95.0, "sortorder": 1, "parentid" : sId, "triggerid": it_trgId })

