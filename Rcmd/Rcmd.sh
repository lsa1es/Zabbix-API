#!/bin/sh
# Remote Command over Zabbix Proxy
# Luiz Sales - lsales.biz

# Pre-requisito: O agent deve estar com a configuracao EnableRemoteCommands Habilitada.
# EnableRemoteCommands=1
# LogRemoteCommands=1

# O proxy que esta configurado no zabbix, tem que estar de preferencia com uma conexao com troca de chave com o servidor do zabbix-server.
# Dessa forma.. quando o comando for utilizado, ele irá descobrir qual o proxy o servidor está e irá se conectar nele e utilizar a 
# chave system.run para passar o comando remoto no zabbix.



# ACESSO 
API='http://zabbix-frontend/api_jsonrpc.php'
ZABBIX_USER='login'
ZABBIX_PASS='pass'

HOST=$1
CMD=$2
# FUNCAO DE AUTH
authenticate()
{
    wget -O- -o /dev/null $API --header 'Content-Type: application/json-rpc' --post-data "{
        \"jsonrpc\": \"2.0\",
        \"method\": \"user.login\",
        \"params\": {
                \"user\": \"$ZABBIX_USER\",
                \"password\": \"$ZABBIX_PASS\"},
        \"id\": 0}" | cut -d'"' -f8
}
AUTH_TOKEN=$(authenticate)

# FUNCAO que me retorna o IP, PORTA e o PROXYID que o host esta configurado no zabbix.
get_host() {

  wget -O- -o /dev/null $API --header 'Content-Type: application/json-rpc' --post-data "{
    \"jsonrpc\": \"2.0\",
    \"method\": \"host.get\",
    \"params\": {
        \"output\" : \"extend\",
	\"selectInterfaces\": [ \"ip\", \"port\" ],
	\"filter\": {
            \"host\": [
                \"$HOST\"
            ]
        }
    },
    \"auth\": \"$AUTH_TOKEN\",
    \"id\": 1}"
}
IP=$(get_host | awk -v RS='{' -F\" '{print $2" "$4}' | grep ip | awk '{print $2}')
PORT=$(get_host | awk -v RS='{' -F\" '{print $6" "$8}' | grep port | awk '{print $2}')
PRXID=$(get_host | awk -v RS=',"' -F\: '/^proxy_hostid/ {print $2}' | sed 's/"//g' )

# FUNCAO me retorna o nome do proxy, que esta configurado o host. baseado no id que recebi de outra funcao.

get_proxy() {

  wget -O- -o /dev/null $API --header 'Content-Type: application/json-rpc' --post-data "{
    \"jsonrpc\": \"2.0\",
    \"method\": \"proxy.get\",
    \"params\": {
        \"output\": [ \"host\", \"proxyid\" ],
    	\"filter\": {
		 \"proxyid\" : [ \"$PRXID\" ]
	 }
	},
    \"auth\": \"$AUTH_TOKEN\",
    \"id\": 1 }"
}
PRX=$(mktemp)
for x in `get_proxy | sed 's/},{/} {/g' | grep $PRXID`
do
	echo $x  | grep $PRXID >> $PRX
done
PROXY_NAME=$(cat $PRX| awk 'NF>0' | awk -v RS='{"' -F\" '/^host/ {print $3}')
rm -rf $PRX


#sshpass -p 'pass' ssh -o StrictHostKeyChecking=no root@$PROXY_NAME "zabbix_get -s $IP -p $PORT -k system.run[\" $CMD \"] "
ssh -o StrictHostKeyChecking=no root@$PROXY_NAME "zabbix_get -s $IP -p $PORT -k system.run[\"$CMD\"] "
