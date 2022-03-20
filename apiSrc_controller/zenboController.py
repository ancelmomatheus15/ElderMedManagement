import os

def awake():
    
    filePath = 'C:\ZenboApplications\zenboAwake.py'    
    runFile(filePath)
    
    return 'OK'

def listAllMedication():
    
    filePath = 'C:\ZenboApplications\zenboListAllMedication.py'    
    runFile(filePath)
    
    return 'OK'

def incomingAppointment():
    
    filePath = 'C:\ZenboApplications\zenboIncomingAppointment.py'   
    runFileParam(filePath, '1')
    
    return 'OK' 

def runFile(filePath):
    
    os.system('python '+ filePath)
    
def runFileParam(filePath, param):
    
    os.system('python '+ filePath + ' ' + param)
    
    
'''
    passar parametros para a execucao
    
    python filePath var1 var2 var3
    
    -> Para acessar:
    
    import sys
        print sys.argv[0] # prints filePath.py -> bom pro debug
        print sys.argv[1] # prints var1
        print sys.argv[2] # prints var2
        
'''
    