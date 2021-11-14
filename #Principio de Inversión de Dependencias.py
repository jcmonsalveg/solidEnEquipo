#Principio de Inversión de Dependencias
#Los módulos de alto nivel no deberían depender de módulos de bajo nivel. Ambos deberían depender de abstracciones.
#Las abstracciones no deberían depender de los detalles. Los detalles deberían depender de las abstracciones.
# como ejemplo se creara un carro de mercado donde se carga un metodo de pago
class compras { ... }
class compraBasket {
    fun buy(compra: compra?) {
        val db = SqlDatabase()
        db.save(compra)
        val creditCard = CreditCard(visa)
        creditCard.pay(compra)
    }
}
class SqlDatabase {
    fun save(compra: compra?) {
        // Saves data in SQL database
    }
}
class CreditCard {
    fun pay(compra: compra?) {
        // Performs payment using a credit card
    }
}
# si queremos agregar un metodo de pago
interface Persistence {
    fun save(compra: compra?)
}
class SqlDatabase : Persistence {
    override fun save(compra: compra?) {
        // Saves data in SQL database
    }
}
interface PaymentMethod {
    fun pay(compra: compra?)
}
class CreditCard : PaymentMethod {
    override fun pay(compra: compra?) {
        // Performs payment using a credit card. american
#se deben invertir las dependencias
class compraBasket(
    private val persistence: Persistence,
    private val paymentMethod: PaymentMethod
) {
    fun buy(compra: compra?) {
        persistence.save(compra)
        paymentMethod.pay(compra)
    }
#Si se quiere adicionar otro metodo de pago
 class Server : Persistence {
    override fun save(compra: compra?) {
        // Saves data in a server
    }
}
class Paypal : PaymentMethod {
    override fun pay(compra: compra?) {
        // Performs payment using Paypal account
    }
}   