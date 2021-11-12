from Persona import Persona

class PadreFamilia(Persona):
    nombreTraba=""
    telTraba=0
    dirTraba=""

    def setNomTraba(self, nombreTraba):
        self.nombreTraba = nombreTraba
    def getNomTraba(self):
        return self.nombreTraba
    
    def setTelTraba(self, telTraba):
        self.telTraba = telTraba
    def getTelTraba(self):
        return self.telTraba
    
    def setDirTraba(self, dirTraba):
        self.dirTraba = dirTraba
    def getDirTraba(self):
        return self.dirTraba
    
