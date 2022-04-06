import os

def zenboAwake():
    
    filePath = 'C:\ZenboApplications\zenboAwake.py'    
    runFile(filePath)
    
    return 'OK'


def zenboListAppointments(userId):
    
    filePath = 'C:\ZenboApplications\zenboInformacaoTratamento.py'    
    runFileParam(filePath, [str(userId)])
    
    return 'OK' 


def zenboListWeekAppointments(userId):
    
    filePath = 'C:\ZenboApplications\zenboListAllMedication.py'    
    runFileParam(filePath, [str(userId)])
    
    return 'OK'


def zenboListTreatments(userId):
    
    filePath = 'C:\ZenboApplications\zenboListAllMedication.py'    
    runFileParam(filePath, [str(userId)])
    
    return 'OK'


def zenboIngestMed(userId, treatmentId):
    
    filePath = 'C:\ZenboApplications\zenboListAllMedication.py'    
    runFileParam(filePath, [str(userId), str(treatmentId)])
    
    return 'OK'


def zenboNextMedication(userId):
    
    filePath = 'C:\ZenboApplications\zenboListAllMedication.py'    
    runFileParam(filePath, [str(userId)])
    
    return 'OK'


def runFile(filePath):
    
    os.system('python '+ filePath)
    
def runFileParam(filePath, param):
    
    paramStr = ' '.join(param)
    
    os.system('python '+ filePath + ' ' + paramStr)
    
    
'''
    passar parametros para a execucao
    
    python filePath var1 var2 var3
    
    -> Para acessar:
    
    import sys
        print sys.argv[0] # prints filePath.py -> bom pro debug
        print sys.argv[1] # prints var1
        print sys.argv[2] # prints var2
        
'''
    