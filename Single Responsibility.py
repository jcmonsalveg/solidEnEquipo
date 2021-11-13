#Principio S

#Una clase debe encargarse de una sola cosa.

#Creamos la clase pacientes, cuya unica tarea es almacenar los pacientes en la base de datos.
class Pacientes():
    def __init__(self):
        self.pacientes = {}
        self.id = 0

    def add_paciente(self, paciente):
        self.id += 1
        self.pacientes[self.id] = paciente

    def __str__(self):
        return str(self.pacientes)

#Creamos otra clase para el registro de los pacientes en la base de datos.
class PacientesRegistrados():
    @staticmethod
    def guardar_pacientes(filename, pacientes):
        with open(filename, "w") as f:
            f.write(str(pacientes))

#Implementacion de la clase para verifica su funcionamiento.
p = Pacientes()
p.add_paciente("Hernan Mejia")
p.add_paciente("Herminia Rodriguez")
p.add_paciente("Celina Rodriguez")
p.add_paciente("Juan Vargas")
print(f"Pacientes registrados: {p}")

#Implentacion de la clase encargada de almacenar la informaciong

g = PacientesRegistrados()
g.guardar_pacientes("pacientes.txt", p)