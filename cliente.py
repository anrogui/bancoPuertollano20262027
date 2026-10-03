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


from models import Cliente
from logs import Log

log = Log()


def leerFichero(numCliente):
    try:
        with open(f"ficherosClientes/{numCliente}.txt", "r") as f:
            linea = f.readline()

            cliente = Cliente(numCliente)

            while linea:
                # Limpiamos espacios y saltos de línea para un registro limpio
                linea_limpia = linea.strip()

                # Opcional: si la línea está vacía, saltamos a la siguiente
                if not linea_limpia:
                    linea = f.readline()
                    continue

                try:
                    datos = linea_limpia.split(";")

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

                except (ValueError, IndexError) as e:
                    mensaje_error = f"ERROR: Línea problemática ignorada en el cliente {numCliente} ('{linea_limpia}'). Detalle: {e}"
                    log.error(mensaje_error)

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