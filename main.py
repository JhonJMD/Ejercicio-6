import os
import ui.menu as m
import funciones.dependencias as d

isActive = True
opMenu = 0
headerD = """
************************
* REGISTRO DEPENDENCIA *
************************
"""

while (isActive):
    os.system("cls")
    try:
        opMenu = m.menuPrincipal()
    except ValueError:
        print(f"Error en el dato de ingreso")
    else:
        if (opMenu == 1):
            rta = "S"
            while(rta in ["S", "s"]):
                os.system("cls")
                print(headerD)
                valor = 0
                indice = 0
                isPresent = True
                while (isPresent):
                    codigo = d.regDependencia(valor, "código")
                    indice = d.buscarDependencia(codigo)
                    if (indice != -1):
                        print(f"El código ya se encuentra registrado")
                    else:
                        isPresent = False
                nombre = d.regDependencia(valor, "nombre")
                co2Producido = 0
                d.registroDependencia = [codigo, nombre, [], [], co2Producido]
                d.dependencias.append(d.registroDependencia)
                rta = input(f"¿Desea registrar otra dependencia? S(Sí) o Enter(No) : ")
            print(f"")
        elif (opMenu == 2):
            os.system("cls")
            m.menuDependencia()
            print(f"")
        elif (opMenu == 3):
            os.system("cls")
            d.calcularEmisiones()
            print(f"")
        elif (opMenu == 4):
            os.system("cls")
            max = 0
            nomMax = ""
            for i in range(len(d.dependencias)):
                if (float(d.dependencias[i][4]) > max):
                    max = float(d.dependencias[i][4])
                    nomMax = d.dependencias[i][1]
            print(f"DEPENDENCIA QUE PRODUCE MAYOR C02 : {nomMax}")
            print(f"")
        elif (opMenu == 5):
            print(f"")
            print(f"GRACIAS POR USAR NUESTRO SERVICIO")
            print(f"")
            isActive = False
        else:
            print(f"Ingrese una opción válida")
        os.system("pause")