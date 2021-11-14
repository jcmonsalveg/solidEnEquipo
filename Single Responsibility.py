#Principio S: Responsabilidad Unica.

#Esta establece que una clase, componente o microservicio debe ser responsable de una sola cosa.

#Creamos la clase pacientes, cuya funcion es crear el consecutivo del numero de pacientes.
class Pacientes():
    def __init__(self):
        self.pacientes = {}
        self.id = 0

    def add_paciente(self, paciente):
        self.id += 1
        self.pacientes[self.id] = paciente

    def __str__(self):
        return str(self.pacientes)

#Creamos la clase PacientesRegistrados, cuya funcion es guardar el nombre del paciente en el archivo de texto.
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

#Implentacion de la clase encargada de almacenar la informacion.

g = PacientesRegistrados()
g.guardar_pacientes("pacientes.txt", p)

#Referencia: Este principio fue hecho acoplandome al enviado por el compañero Juan Carlos Monsalve G.