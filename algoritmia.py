#Prueba de algoritmia se solicitaran al usuario una lista de números que funcionaran como
#la base para una futura validación donde se indicará el menor de los mayores y el número
#mayor de los menores se utiliza estructuras ciclicas y condicionales

#Inicialización de variables
cantidadNumerosEvaluar = int(input("Ingrese el número correspondiente al tamaño de la lista: "))
# print("Tamaños lista: ", cantidadNumerosEvaluar)


listaNumeros = []
listaNumerosEvaluar = []

listaNumerosBase = input("Ingrese por favor los números de la lista en una sola linea separados por un espacio: ")
# print("Numeros de la lista: ",numerosLista)

#Formateo de los números de la lista
listaNumerosBaseFormateados = listaNumerosBase.split()
for i in range(0, len(listaNumerosBaseFormateados)):
    listaNumeros.append(int(listaNumerosBaseFormateados[i]))
# print("Lista numeros:", listaNumeros)

#Solicitud de cantidad de consultas a realizar
cantidadConsultas = int(input("Ingrese el número de consultas a realizar: "))
# print("cantidad de consultas: ", cantidadConsultas)

#Solicitud de los números a evaluar
numerosEvaluar = input("Ingrese los números que desee consultar separados por un espacio: ")

#Formateo de los números a evaluar
listaNumerosEvaluarFormateda = numerosEvaluar.split()
for i  in range(0, len(listaNumerosEvaluarFormateda)):
    listaNumerosEvaluar.append(int(listaNumerosEvaluarFormateda[i]))
# print("Lista números a evaluar: ", listaNumerosEvaluar)

#Inicio lógica
for i in listaNumerosEvaluar:
    auxMenor= "X"
    for j in listaNumeros:
        #Validación número mayor de los menores
        if j < i:
            auxMenor = j
            if auxMenor > j:
                auxMenor = auxMenor
            else:
                auxMenor = j
        else:
            break
    # print(auxMenor)
#Validación número menor de los mayores
    auxMayor = "X"
    for j in listaNumeros:
        if j > i:
            auxMayor = j
            break
    print(auxMenor, auxMayor)

# for i in listaNumerosEvaluar:
#     auxMayor = "X"
#     for j in listaNumeros:
#         if j > i:
#             auxMayor = j
#             break
#     print(auxMayor)
