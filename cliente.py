from models import Cliente
from logs import Log

log = Log()

def cargarCliente(tipo):
    while True:
        num = input("Introduce el número de cliente: ")

        if len(num) != 6 or not num.isdigit():
            print("El formato introducido no es correcto")
            continue

        if tipo == "movimientos":
            return leerFichero(num)

        elif tipo == "guardado":
            return cargarClienteGuardado(num)


def leerFichero(numCliente):


    cliente = Cliente(numCliente)
    contador_movimientos = 0

    while linea:

    try:
        with open(f"ficherosClientes/{numCliente}.txt", "r") as f:

            linea = f.readline()

            while linea:

                datos = linea.strip().split(";")

                cantidad = float(datos[0])
                operacion = datos[1]
                destino = datos[2]

                if destino == "Cuenta" and operacion == "Ingreso":
                    cliente.cuenta.ingresar(cantidad)
                    contador_movimientos += 1

                elif destino == "Cuenta" and operacion == "Retirada":
                    cliente.cuenta.retirar(cantidad)
                    contador_movimientos += 1

                elif destino == "Deposito" and operacion == "Ingreso":
                    cliente.deposito.ingresar(cantidad)
                    contador_movimientos += 1

                elif destino == "Deposito" and operacion == "Retirada":
                    cliente.deposito.retirar(cantidad)
                    contador_movimientos += 1
                linea = f.readline()

        # Guardamos el estado final del cliente
        cliente.guardar()

        print("Datos del cliente cargados correctamente")

        mensaje_contador = f"Movimientos procesados: {contador_movimientos}"
        print(mensaje_contador)
        log.info(mensaje_contador)

        cliente.guardar()
        return cliente

    except FileNotFoundError:
        print("El usuario no tiene ninguna cuenta con el banco")
        return None


def cargarClienteGuardado(numCliente):

    try:
        with open(f"datosClientes/{numCliente}.txt", "r") as f:

            linea = f.readline()
            datos = linea.split(";")

            cliente = Cliente(datos[0])

            cliente.cuenta.saldo = float(datos[1])
            cliente.deposito.saldo = float(datos[2])

            return cliente

    except FileNotFoundError:
        print("Primero tienes que cargar los datos de este cliente")
        return None