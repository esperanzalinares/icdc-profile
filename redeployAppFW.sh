#!/bin/ksh
#set -x

WLS_PW=`cat /datos/wl10.3-64/.weblogic/passwd`

# JAVA_OPTIONS de WL
echo $JAVA_OPTIONS
JAVA_OPTIONS="$JAvA_OPTIONS -Dweblogic.security.SSL.trustedCAKeyStore=$WL_HOME/server/lib/cacerts"

##############################################
# $1 Es el nombre del ear a desplegar 
# $2 ruta completa dominio de despliegue
# $3 Es el target sobre el que se realizar el redespliegue
# $4 IP del dominio
# $5 Puerto del dominio
# Guardamos los parmetos recibidos puesto que al cargar el DomainEnv se perder su valor
##############################################

APLICACION=$1
DOMINIO=$2
TARGET=$3
IPDOM=$4
PUERTODOM=$5
USUARIOWL=$6

. $2/bin/setDomainEnv.sh

cd /datos/scripts/IC

java weblogic.WLST redespliegue.py $APLICACION $DOMINIO/EAR $TARGET $IPDOM $PUERTODOM $USUARIOWL $WLS_PW
