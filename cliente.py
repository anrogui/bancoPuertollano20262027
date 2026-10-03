from models import Cliente
from logs import Log

log = Log()

from models import Cliente
from logs import Log

log = Log()

def cargarCliente(tipo):
    cliente = None
    cargando = True

    while cargando:
        num = input("Introduce el número de cliente: ")

        if len(num) != 6 or not num.isdigit():
            print("El formato introducido no es correcto")

        try:
            if tipo == "movimientos":
                cliente = leerFichero(num)
            elif tipo == "guardado":
                cliente = cargarClienteGuardado(num)


            if cliente is None:
                raise FileNotFoundError(f"El fichero del cliente {num} no existe.")

            cargando = False

        except FileNotFoundError as e:
            print("El usuario no tiene ninguna cuenta con el banco o el cliente no existe.")
            log.error(f"ERROR: Intento de consultar cliente inexistente ({num}). Detalle: {e}")
            cliente = None
            cargando = False

        except Exception as e:
            print("Ocurrió un error inesperado al procesar la solicitud.")
            log.error(f"ERROR crítico al cargar el cliente {num}: {e}")
            cliente = None
            cargando = False
    return cliente

def leerFichero(numCliente):
    try:
        with open(f"ficherosClientes/{numCliente}.txt", "r") as f:
            linea = f.readline()

            cliente = Cliente(numCliente)

            while linea:
                datos = linea.strip().split(";")

                cantidad = float(datos[0])
                operacion = datos[1]
                destino = datos[2]

                if destino == "Cuenta" and operacion == "Ingreso":
                    cliente.cuenta.ingresar(cantidad)

                elif destino == "Cuenta" and operacion == "Retirada":
                    cliente.cuenta.retirar(cantidad)

                elif destino == "Deposito" and operacion == "Ingreso":
                    cliente.deposito.ingresar(cantidad)

                elif destino == "Deposito" and operacion == "Retirada":
                    cliente.deposito.retirar(cantidad)

                linea = f.readline()
        cliente.guardar()

        print("Datos del cliente cargados correctamente")

        resumen_mensaje = (f"Resumen de carga - Cliente: {numCliente} | "f"Saldo cuenta: {cliente.cuenta.saldo} € | "f"Saldo depósito: {cliente.deposito.saldo} €"
        )
        log.info(resumen_mensaje)

        return cliente

    except FileNotFoundError:
        mensaje_error = f"Intento fallido de cargar movimientos: El cliente {numCliente} no existe en ficherosClientes."
        print("El usuario no tiene ninguna cuenta con el banco")
        log.error(mensaje_error)
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