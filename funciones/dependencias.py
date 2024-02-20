dependencias = []
registroDependencia = []
isIncorrect = True

def buscarDependencia(codigoDepedencia : str) -> int:
    global indice
    indice = -1
    for item in dependencias:
        if codigoDepedencia in item:
            indice = dependencias.index(item)
    return indice

def regDependencia(valorDato, nombreDato):
    global isIncorrect
    isEmpty = True
    valorDato = 0
    while (isEmpty):
        valorDato = input(f"Ingrese {nombreDato} de la dependencia: ")
        if (valorDato == ""):
            print(f"El {nombreDato} no puede estar vacío")
        else:
            isEmpty = False
    return valorDato

def regConsumoDispositivos(indiceDependencia : int):
    global isIncorrect
    isIncorrect = True
    while (isIncorrect):
        try:
            potencia = float(input(f"Ingrese la potencia del dispositivo en W : "))
        except ValueError:
            print(f"Ingrese un dato correcto")
        else:
            isIncorrect = False
    isIncorrect = True
    while (isIncorrect):
        try:
            tiempoUso = int(input(f"Ingrese el tiempo de uso en horas : "))
        except ValueError:
            print(f"Ingrese un dato correcto")
        else:
            isIncorrect = False
    consumoDispositivo = (potencia * tiempoUso) / 1000
    dependencias[indiceDependencia][2].append(consumoDispositivo)

def regConsumoTransporte(indiceDependencia : int):
    global isIncorrect
    isIncorrect = True
    while (isIncorrect):
        try:
            kmRecorridos = float(input(f"Ingrese el número de kilómetros recorridos por el transporte : "))
        except ValueError:
            print(f"Ingrese un dato correcto")
        else:
            isIncorrect = False
    dependencias[indiceDependencia][3].append(kmRecorridos)

def calcularEmisiones():
    print(f"REPORTE")
    print(f"----------------------------------------")
    print("{:<15} {:<15}".format("DEPENDENCIA", "CO2 PRODUCIDO"))
    for i in range(len(dependencias)):
        emiDispositivos = sum(dependencias[i][2]) * 0.1
        emiTransporte = sum(dependencias[i][3]) * 0.3
        emiTotal = emiDispositivos + emiTransporte
        dependencias[i][4] = emiTotal
        print("{:<15} {:<15}".format(dependencias[i][1], dependencias[i][4]))
    print(f"")
