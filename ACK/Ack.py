#!/usr/bin/env python
from zabbix_api import ZabbixAPI
import sys

EVENTID = sys.argv[1]
MSG = sys.argv[2]

zapi = ZabbixAPI(server="")
zapi.login("user", "pass" )

ack = zapi.event.acknowledge({ "eventids" : EVENTID, "message" : MSG, "action" : 0 })
