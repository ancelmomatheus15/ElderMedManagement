import mysql.connector
from apiSrc_application import persistanceProperties
from apiSrc_entity import appointmentEntity, treatmentEntity
from datetime import datetime
from apiSrc_entity.medicEntity import Medic

def getAppointmentsById(id):
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "SELECT * FROM appointment WHERE id = "+ str(id) +";";
        dbCursor.execute(query)
    
        dbQueryResult = dbCursor.fetchall()
        
        dbCursor.close()
        dbConn.close()
        
        return(entityConverter(dbQueryResult))
    
    except:
        
        return("Erro ao conectar com o banco de dados") 
    
def getTreatmentById(id):
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "SELECT * FROM treatment WHERE id = "+ str(id) +";";
        dbCursor.execute(query)
    
        dbQueryResult = dbCursor.fetchall()
        
        dbCursor.close()
        dbConn.close()
        
        return(entityConverterTreatment(dbQueryResult))
    
    except:
        
        return("Erro ao conectar com o banco de dados") 
    
def createAppointment(user, hora, data, hospital, medic, descricao):
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase) 
    
        dbCursor = dbConn.cursor()
    
        query = "INSERT INTO appointment (user, hora, data, hospital, medic, descricao) VALUES('"+ user +"', '"+ hora +"', '"+ data +"', '"+ hospital +"', '"+ medic +"', '"+ descricao +"');"
        dbCursor.execute(query)
    
        dbConn.commit()
        
        retMesage = ""
        
        if dbCursor.lastrowid:
            retMessage = ('last insert id: ' + str(dbCursor.lastrowid))

        else:
            retMessage = 'could not insert register'

        
        dbCursor.close()
        dbConn.close()
        
        return(retMessage)
    
    except:
        
        return("Erro ao conectar com o banco de dados")
    
    
def createTreatment(user, medication, data_inicio, data_fim, last_occurrence, medic, descricao):

    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "INSERT INTO treatment (user, medication, data_inicio, data_fim, last_occurrence, medic, descricao) VALUES('"+ user +"', '"+ medication +"', '"+ data_inicio +"', '"+ data_fim +"', '"+ last_occurrence +"', '"+ medic +"', '"+ descricao +"');"
        dbCursor.execute(query)
    
        dbConn.commit()
        
        retMesage = ""
        
        if dbCursor.lastrowid:
            retMessage = ('last insert id: ' + str(dbCursor.lastrowid))

        else:
            retMessage = 'could not insert register'

        
        dbCursor.close()
        dbConn.close()
        
        return(retMessage)
    
    except:
        
        return("Erro ao conectar com o banco de dados")

def updateAppointment(appointment):
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "UPDATE appointment SET user = '"+ appointment.user +"', hora = '"+ str(appointment.hora) +"', data = '"+ appointment.data +"', hospital = '"+ str(appointment.hospital) +"', medic = '"+ str(appointment.medic) +"', descricao = '"+ appointment.descricao +"' WHERE id = "+ str(appointment.id) +";";
        dbCursor.execute(query)
    
        dbConn.commit()
        
        return("Registro alterado")
    
    except:
        
        return("Erro ao conectar com o banco de dados")
    
    
def updateTreatment(treatment):  
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "UPDATE treatment SET user = '"+ str(treatment.user) +"', medication = '"+ str(treatment.medication) +"', data_inicio = '"+ str(treatment.data_inicio) +"', data_fim = '"+ str(treatment.data_fim) +"', last_occurrence = '"+ str(treatment.last_occurrence) +"', medic = '"+ str(treatment.medic) +"', descricao = '"+ treatment.descricao +"' WHERE id = "+ str(treatment.id) +";";
        dbCursor.execute(query)
    
        dbConn.commit()
        
        return("Registro alterado")
    
    except:
        
        return("Erro ao conectar com o banco de dados")
      
      
      
def deleteAppointmentById(id):
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "DELETE FROM appointment WHERE id = "+ id +";";
        
        dbCursor.execute(query)
    
        dbConn.commit()
        
        return("Registro alterado")
    
    except:
        
        return("Erro ao conectar com o banco de dados")
 
 
def deleteTreatmentById(id):
    
    try:
        
        paramHost = persistanceProperties.getProperty("host")
        paramUser = persistanceProperties.getProperty("user")
        paramPassword = persistanceProperties.getProperty("password")
        paramDatabase = persistanceProperties.getProperty("database")
        
        dbConn = mysql.connector.connect(host=paramHost, user=paramUser, password=paramPassword, database=paramDatabase)
    
        dbCursor = dbConn.cursor()
    
        query = "DELETE FROM treatment WHERE id = "+ id +";";
        
        dbCursor.execute(query)
    
        dbConn.commit()
        
        return("Registro alterado")
    
    except:
        
        return("Erro ao conectar com o banco de dados")
 

    
def entityConverter(queryResults):
    
    returnArray = []
    
    for item in queryResults:
        
        newAppointment = appointmentEntity.Appointment()
        
        newAppointment.id = item[0]
        newAppointment.user = item[1]
        newAppointment.hora = item[2]
        newAppointment.data = item[3].strftime("%d/%B/%Y")
        newAppointment.hospital = item[4]
        newAppointment.medic = item[5]
        newAppointment.descricao = item[6]
        
        returnArray.append(newAppointment)
        
    return(returnArray)

def entityConverterTreatment(queryResults):
    
    returnArray = []
    
    for item in queryResults:
        
        newTreatment = treatmentEntity.Treatment()
        
        newTreatment.id = item[0]
        newTreatment.user = item[1]
        newTreatment.medication = item[2]
        newTreatment.data_inicio = item[3]
        newTreatment.data_fim = item[4]
        newTreatment.last_occurrence = item[5]
        newTreatment.medic = item[6]
        newTreatment.descricao = item[7]
        
        returnArray.append(newTreatment)
        
    return(returnArray)
        
