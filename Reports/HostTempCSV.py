import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import csv
from zabbix_api import ZabbixAPI

c = csv.writer(open("HostTemplate-280917.csv", "wb"), delimiter=";" )

c.writerow(["TEMPLATE","HOSTNAME"])

zapi = ZabbixAPI(server="http://zabbix/")
zapi.login("user", "password" )

templates = zapi.template.get({ "output" : "extend", "selectHosts" : "extend" })
print "TEMPLATE;HOST"
tmp_lst = []
for x in templates:
	tName = x[u'name']
	hosts = x[u'hosts']
	tmp_lst.append(tName)
	for w in hosts:
		hName = w[u'name']
		print "%s;%s" % (tName,hName)
		c.writerow([str(tName),str(hName)])

