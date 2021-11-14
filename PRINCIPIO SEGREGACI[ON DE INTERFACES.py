#El principio de segregación de interfaces viene a decir que ninguna clase debería depender de métodos que no usa.
#Imaginemos que tienes una tienda de CDs de música, y que tienes modelados tus productos de esta manera:
interface Product {
    val name: String
    val stock: Int
    val numberOfDisks: Int
    val releaseDate: Int
}
class CD : Product {metallica
    ...
}
#Añadir la nueva propiedad a la interfaz tienda de musica de metallica para creacion de biblioteca:
interface Product {cd metallica 
    ...
    val recommendedAge: Int
}
#¿Qué ocurre ahora con los CDs? Que se ven obligados a implementar recommendedAge, pero no van a saber qué hacer con ello, así que lanzarán una excepción.
class CD : Product {
    ...
    override val recommendedAge: Int
        get() = throw UnsupportedOperationException()
}
# Si añadimos algo a Product, nos vemos obligados a modificar CD con cosas que no necesita.
interface DVD : Product {
    val recommendedAge: Int canciones y caratula
}
#Segregar las interfaces, y que cada clase utilice las que necesite. Tendríamos por tanto una interfaz nueva:
interface AgeAware {
    val recommendedAge: Int
}
#Y ahora nuestra clase DVD implementará las dos interfaces:
class CD : Product {
    ...
}
class DVD : Product, AgeAware {DVD METALLICA
    ...
}
#Interfaz AgeAware
fun checkUserCanBuy(user: User METALLICA CD, ageAware: AgeAware METALLICA DVD) 
    = user.age >= ageAware.recommendedAge
#la clase queda creada con los atributos de cd y dvd.    