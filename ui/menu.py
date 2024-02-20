import os
import funciones.dependencias as d
import ui.titles as t

menu = "1. Registrar Dependencia\n2. Registrar Consumo por Dependencia\n3. Ver CO2 Producido\n4. Dependencia que produce mayor CO2\n5. Salir"
subMenuDependencias = "1. Dispositivos\n2. Transporte\n3. Regresar al menu principal"

def menuPrincipal() -> int:
    global hasError
    hasError = True
    t.headerP()
    print(menu)
    while (hasError):
        try:
            print(f"")
            return int(input(f": "))
        except ValueError:
            hasError = True

def menuDependencia():
    os.system("cls")
    isActiveMenu = True
    isIncorrect = True
    while (isActiveMenu):
        os.system("cls")
        t.headerD()
        try:
            print(subMenuDependencias)
            print(f"")
            opMenu = int(input(f": "))
        except ValueError:
            print(f"Opción inválida")
        else:
            if(opMenu == 1):
                isIncorrect = True
                os.system("cls")
                t.headerCD()
                while (isIncorrect):
                    codigo = input(f"Ingrese el código de la dependencia cuyos datos va a registrar : ")
                    d.buscarDependencia(codigo)
                    if (d.indice == -1):
                        print(f"No se encontró dependencia")
                        print(f"")
                        os.system("pause")
                    else:
                        rta = "S"
                        while (rta in ["S", "s"]):
                            d.regConsumoDispositivos(d.indice)
                            rta = input(f"¿Desea registrar otro dispositivo? S(Sí) o Enter(No) : ")
                        print(f"")
                        isIncorrect = False
                    os.system("pause")
                print(f"")
            elif(opMenu == 2):
                isIncorrect = True
                os.system("cls")
                t.headerCT()
                while (isIncorrect):
                    codigo = input(f"Ingrese el código de la dependencia cuyos datos va a registrar : ")
                    d.buscarDependencia(codigo)
                    if (d.indice == -1):
                        print(f"No se encontró dependencia")
                        print(f"")
                        os.system("pause")
                    else:
                        rta = "S"
                        while (rta in ["S", "s"]):
                            d.regConsumoTransporte(d.indice)
                            rta = input(f"¿Desea registrar otro transporte? S(Sí) o Enter(No) : ")
                        print(f"")  
                        isIncorrect = False  
                    os.system("pause")
            elif(opMenu == 3):
                isActiveMenu = False
            else:
                print(f"La opción ingresada es inválida")
