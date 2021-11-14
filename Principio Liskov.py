#Principio de sustitución de Liskov.

#El principio de sustitución de Liskov nos dice que, si en alguna parte de nuestro código estamos usando una clase, 
# y esta clase es extendida, tenemos que poder utilizar cualquiera de las clases hijas y que el programa siga siendo válido.

#Creamos la clase consola, la cual contiene un metodo controles que nos devolvera un valor que es entero >int.

class consola:
    @staticmethod
    def controles()->int:
        pass

#Creamos las clases (xboxone,playstation,nintendo), los cuales se extienden desde la clase (consola).

class xboxone(consola):
    @staticmethod
    def controles() -> int:
        return 2

class playstation(consola):
    @staticmethod
    def controles() -> int:
        return 2

class nintendo(consola):
    @staticmethod
    def controles() -> int:
        return 4

#En las clases anteriores nos devuelve return valores diferentes, estas 3 clases son la implementacion de la clase superior (consola).

if __name__ =="__main__":
   print(xboxone.controles())
   print(playstation.controles())
   print(nintendo.controles())

#Referencia: Este principio fue hecho acoplandome al enviado por el compañero Juan Carlos Monsalve G.