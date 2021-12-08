
#
# PROYECTO DE UNIDAD 2 EN EQUIPO:
#
#   MODIFICAR EL PROGRAMA DE ONE MAX PROBLEM (PROPIO O PROPORCIONADO)
#   PARA DAR SOLUCIÓN AL PROBLEMA DE LA "SPHERE"
#
#   DOCUMENTAR TODO EL CÓDIGO, HACIENDO ENFASIS EN LAS MODIFICACIONES REALIZADAS
#
#   REALIZAR UN VÍDEO CORTO EN EL QUE SE REALICE EXPLIQUE EL CÓDIGO Y
#   AL MENOS UNA EJECUCIÓN EXPLICADA PASO A PASO!
#
#


# Algoritmo Genetico

def crearPoblacion():
    import random as rnd
    for ind in range(poblacion_length):
        ##[ cromosomas, fo, pi]
        poblacion.append( [ [int(rnd.random()*2) for i in range(individuo_length)], 0, 0] )
    print(poblacion)

def evaluarFO():
    for ind in range(poblacion_length):
        fo_i = sum(poblacion[ind][0]) ##calcular la cantidad de 1 que tiene cada vector
        poblacion[ind][1] = fo_i
    print(poblacion)

def seleccion():
    sum_fi = 0   #sumatoria de los valores Fo de todos los ind (poblacion)
    for ind in range(padres_length):
        sum_fi += poblacion[ind][1]
    print(sum_fi)

    #calcular la P_i  = Fo_i / Sum_Fi . Calcular la probabilidad de i, se obtiene de
    #dividir la función objetivo de i entre la sumatoria de las funciones objetivo de todos los
    #individuos
    for ind in range(padres_length):
        pi = poblacion[ind][1]/sum_fi
        poblacion[ind][2] = pi
        print(poblacion[ind][2])

    #aplicación de la ruleta
    import random as rnd

    padres = []
    for i in range(hijos_length): #por cada hijo que se necesite
        v = rnd.random()  #aleatorio entre 0 y 1
        temp = 0
        print("valor de v: " + str(v))
        for j in range(padres_length):
            temp +=  poblacion[j][2]
            print("valor de temp:" + str(temp))
            if v < temp:  #se ejecutará cuando la suma de temp sea mayor que V
                padres.append(poblacion[j])
                break
    return padres

def cruza():
    hijos = []
    for i in range(0, hijos_length, 2): #de 2 en 2 porque se ocupan 2 padres por cada 2 hijos
        padre1 = padres[i][0]
        padre2 = padres[i+1][0]
        print("Padre 1:", padre1)
        print("Padre 2:", padre2)

        import random as rnd
        punto_de_cruza = int(rnd.random()*individuo_length)
        print("Punto de Cruza : " + str(punto_de_cruza))

        hijo1 = padre1[0:punto_de_cruza] + padre2[punto_de_cruza:]
        hijo2 = padre1[punto_de_cruza:] + padre2[0:punto_de_cruza]

                    #vector  fo  pi
        hijos.append([hijo1, 0, 0])
        hijos.append([hijo2, 0, 0])

    return hijos


poblacion_length = 6  # 4 padres + 2 hijos

hijos_length = 2
padres_length = 4

individuo_length = 5 #(Tamaño del arreglo binario) ## >= 3

poblacion = []



print("Creacion de la población:")
crearPoblacion()

print("\nEvaluación de la Funcion Objetivo (FO):")
evaluarFO()

generaciones = 500
generacion_actual = 1

#Obtención de los X mejores individuos.  x = 4
poblacion.sort(key=lambda poblacion: poblacion[1], reverse=True)
poblacion = poblacion[0:padres_length]  #Mejores individuos
print(poblacion)

#Detencion por dos razones:
#   *se logra la mejor solución
#   *se terminan las generaciones

while(generacion_actual <= generaciones):

    print("\nGeneración Actual : " + str(generacion_actual) + "\n")

    print("\nMejor F0 actual:")
    mejor = poblacion[0][1] #Cuantos unos tiene el vector que tiene más unos
    print(mejor)

    if mejor == individuo_length:
        break

    print("\n\nSelección de Padres:")
    padres = seleccion() #Se requiere 2 padres por hijo
    print(padres)

    print("\nCruza:") #Obtencion de hijos - Cruza en un Punto
    ##100% Probabilidad de Cruza...
    hijos = cruza()
    print(hijos)


    print("\nMuta") #Muta de hijos
    ##80% de probabilida de muta de cada hijo (cada vector)
    #10% de probabilidad de muta de cada gen (cada elemento del vector)
    import random as rnd
    for hijo in hijos:
        print("Hijo: ")
        print(hijo)
        u = rnd.random()
        print(u)
        print(hijo[0])
        if   u <= 0.8:
            for i in range(len(hijo[0])): #por cada elemento del vector hijo
                m = rnd.random()
                if m <= .10:  #existe una probabilidad del 10% de que mute
                    # para cada variable del vector hijo
                    #se tiene una probabilidad del 50% para ser 1 o 0
                    hijo[0][i] = 1 if (rnd.random() > .5) else 0
                    #hijo [0 1 0 1 1]

            print("Hijo Mutado:")
            print(hijo[0])
        print()



    #Combinación de padres con hijos
    poblacion = poblacion + hijos
    print("Población Nueva: ")
    print(poblacion)

    print("\nEvaluación FO nueva poblacion:")
    evaluarFO()  #se pudiera solo evaluar a los hijos nuevos

    # Obtención de los X mejores individuos.  x = 4
    poblacion.sort(key=lambda poblacion: poblacion[1], reverse=True)
    poblacion = poblacion[0:padres_length]

    generacion_actual += 1

#Fuera del cilo while...

print("El programa finalizó en la generación: ", (generacion_actual-1))
print("Mejor F0 obtenido: " ,poblacion[0][1])
print("Mejor Solución: ")
print(poblacion[0][0])