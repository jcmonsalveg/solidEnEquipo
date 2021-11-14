#Principio open close.
#Imaginemos que tenemos una clase con un método que se encarga de dibujar un vehículo, cada vehículo tiene su propia forma de ser pintado. Nuestro vehículo tiene la siguiente forma:.

class Vehicle(val type: VehicleType). 
#Básicamente es una clase que especifica su tipo mediante un enumerado. Podemos tener por ejemplo un enum con un par de tipos:.

enum class VehicleType{
    CAR, MOTORBIKE
}
#Y éste es el método de la clase que se encarga de pintarlos:.
fun draw(vehicle: Vehicle) {
    when(vehicle.type){
        VehicleType.CAR -> drawCar(vehicle)
        VehicleType.MOTORBIKE -> drawMotorbike(vehicle)
    }
}
#Si lo solucionamos mediante herencia o polimorfismo, el paso evidente es sustituir ese enumerado por clases reales, y que cada clase sepa cómo pintarse:.
interface Vehicle {
    fun draw()
}
class Car : Vehicle {
    override fun draw() {
        // Draw the car
    }
}
class Motorbike : Vehicle {
    override fun draw() {
        // Draw the motorbike
    }
}
#Ahora nuestro método anterior se reduce a:.
fun draw(vehicle: Vehicle) {
    vehicle.draw()
}
#Añadir nuevos vehículos ahora es tan sencillo como crear la clase correspondiente que extienda de Vehicle:
class Truck: Vehicle {
    override fun draw() {
        // Draw the truck
    }
}