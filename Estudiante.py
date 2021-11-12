from Persona import Persona

class Estudiante(Persona):
    carne=0
    grado=""

    def setCarne(self, carne):
        self.carne = carne
    def getCarne(self):
        return self.carne
    
    def setGrado(self, grado):
        self.grado = grado
    def getGrado(self):
        return self.grado
    
