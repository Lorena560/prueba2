from Maestro import Maestro

class Tecnico(Maestro):
    especializacion=""

    def setEspecialidad(self, especializacion):
        self.especializacion = especializacion
    def getEspecialidad(self):
        return self.especializacion