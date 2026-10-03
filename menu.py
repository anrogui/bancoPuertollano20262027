import os
from cliente import cargarCliente
from logs import Log

log = Log()


def menu():
    while True:

        print("1) Cargar Datos Cliente")
        print("2) Consultar cuenta Deposito")
        print("3) Listar clientes cargados")
        print("4) Salir")

        opt = input("Introduce la opción deseada: ")

        if opt == "1":
            cargarCliente("movimientos")

        elif opt == "2":
            cliente = cargarCliente("guardado")
            if cliente is not None:
                log.escribir("INFO", f"CONSULTA DATOS CLIENTE CON NÚMERO: {cliente.numero}")
                print(f"Cliente: {cliente.numero}")
                print(f"Saldo cuenta: {cliente.cuenta.saldo} €")
                print(f"Saldo depósito: {cliente.deposito.saldo} €")

        elif opt == "3":
            log.escribir("INFO", "CONSULTA LISTADO DE CLIENTES CARGADOS")
            print("\nClientes cargados:\n")

            try:
                archivos = os.listdir("datosClientes")
                for archivo in archivos:
                    if archivo.endswith(".txt"):
                        num_cliente = archivo.replace(".txt", "")
                        print(f"- {num_cliente}")

            except FileNotFoundError:
                print("Todavía no hay ningún cliente cargado.")

            print()

        elif opt == "4":
            log.escribir("INFO","FIN EJECUCIÓN")
            print("Hasta pronto")
        else:
            log.escribir(
                "WARNING",
                "SE HA INTRODUCIDO UNA OPCION EN EL MENÚ NO RECONOCIDA"
            )
            print("No se ha seleccionado ninguna opción correcta")