def getProperty(propName):
    
    try:       
        return(propDict[propName])

    except:
        return("ERRO: Propriedade nao encontrada")
    
    
    return propName

propDict = {    
    "host" : "localhost",
    "user" : "root",
    "password" : "102030",
    "database" : "zenbointegrationdb"
}





    
    