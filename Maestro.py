from Persona import Persona

class Maestro(Persona):
    prof=""
    usuario=""
    contra=""

    def setProfe(self, prof):
        self.profesion = prof
    def getProfe(self):
        return self.prof
    
    def setUsuario(self, usuario):
        self.usuario = usuario
    def getUsuario(self):
        return self.usuario
    
    def setContraseña(self, contraseña):
        self.contraseña = contraseña
    def getContraseña(self):
        return self.contraseña 