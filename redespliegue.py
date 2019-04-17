##############################################################################
##
## Para tracear el script python
##
##############################################################################
#import pdb;
#pdb.set_trace()
##############################################################################
##
## Conecta con el servidor WebLogic
##
##############################################################################

def conectar(direccion, puerto, usuario, password):
    try:
        connect(usuario, password, direccion+':'+puerto)
    except:
        print ("No se puede conectar con el servidor WebLogic " + serverName + " (" + direccion +":" + puerto + ")")


##############################################################################
##
## Realiza el despliegue de una aplicacion
##
## $APLICACION $DOMINIO/EAR $TARGET $WLS_PW $IPDOM $PUERTODOM $USUARIO
##############################################################################

def redesplegarAplicacion(appName, path, server, ipdom, puertodom, usuariowl,passwwl):
    conectar(ipdom, puertodom, usuariowl, passwwl)
    if checkHealth(server) == "RUNNING":
	#edit()
        #cancelEdit('y')
	edit()
	startEdit()
        #serverConfig()
        redeploy(appName=appName, targets=server, stageMode='nostage')
	save()
	activate()
	exit()
    else:
        print ("No se va a redesplegar la Aplicacion pues el servidor no estfuncionando correctamente")

##############################################################################
##
## Devuelve el estado del servidor
##
##############################################################################
def checkHealth(serverName):
    slBean = getSLCRT(serverName)
    status = slBean.getState()
    print ("Status of Managed Server is "+status)
    return status
	
##############################################################################
##
## Metodo que devuelve el estado de un servidor
##
##############################################################################
def getSLCRT(svrName):

    print ("Consultando el estado... "+svrName)
    
    domainRuntime()
    slrBean = cmo.lookupServerLifeCycleRuntime(svrName)
    return slrBean	

#############################################################################
##
## Funcion main
## $APLICACION $DOMINIO/EAR $TARGET $WLS_PW $IPDOM $PUERTODOM $USUARIO
##############################################################################

if __name__ == "main":
    if len(sys.argv) < 8:
        print ("Uso: java weblogic.WLST " + sys.argv[0] + sys.argv[1])
    else:
        redesplegarAplicacion(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
