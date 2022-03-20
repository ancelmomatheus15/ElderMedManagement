from apiSrc_service import appointmentService

def getAppointment(userId):
    
    results = appointmentService.getAppointment(userId)
    
    return results 

def getTreatment(userId):
    
    results = appointmentService.getTreatment(userId)
    
    return results

def createAppointment(user, hora, data, hospital, medic, descricao):
    
    results = appointmentService.createAppointment(user, hora, data, hospital, medic, descricao)
    
    return results

def createTreatment(user, medication, data_inicio, data_fim, last_occurrence, medic, descricao):
    
    results = appointmentService.createTreatment(user, medication, data_inicio, data_fim, last_occurrence, medic, descricao)
    
    return results

def updateAppointment(appointmentId, user, hora, data, hospital, medic, descricao):
        
    results = appointmentService.updateAppointment(appointmentId, user, hora, data, hospital, medic, descricao)
    
    return results 

def updateTreatment(treatmentId, user, medication, data_inicio, data_fim, last_occurrence, medic, descricao):
        
    results = appointmentService.updateTreatment(treatmentId, user, medication, data_inicio, data_fim, last_occurrence, medic, descricao)
    
    return results 

def deleteTreatmentById(id):
    
    results = appointmentService.deleteTreatmentById(id)

    return results

def deleteAppointmentById(id):
    
    results = appointmentService.deleteAppointmentById(id)

    return results











