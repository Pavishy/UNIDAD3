
def funcionObjetivo(vector):
    sum = 0
    for i in vector:
        sum += i**2
    return sum


def crearParticulas():
    global gbest
    import random as rnd
    for i in range(total_particulas):
        ##[ cromosomas, fo, velocidad]
        enjambre.append( [ [int(rnd.random() * (max-min) + min) for i in range(total_caracteristicas)], 0, [ 0 for i in range(total_caracteristicas)]] )
        enjambre[i][1] = funcionObjetivo(enjambre[i][0])  #actualizar la FO de la particula
                        #a través de la evaluación del vector de dicha particula
        pbest.append(enjambre[i])
        #pbest[0][1] = 25

        if pbest[i][1] < gbest[1]:
            gbest = pbest[i]

    print(enjambre)
    print(pbest)
    print(gbest)


total_particulas = 10
total_caracteristicas = 5

enjambre = []
pbest = []
gbest = [[],1000000000]

min = -10
max = 10

crearParticulas()

tot_iteraciones  = 50

import random as rnd

w = 0.2
C1 = .5
C2 = .3

for it in range(tot_iteraciones):

    for i in range(len(enjambre)):  #Para cada particula

        for j in range(len(enjambre[i][0])):

            r1 = rnd.random()  #
            r2 = rnd.random()

            enjambre[i][2][j] = enjambre[i][2][j] * w + \
                                C1*r1* ( pbest[i][0][j] - enjambre[i][0][j]) +\
                                C2*r2* ( gbest[0][j] - enjambre[i][0][j])

            enjambre[i][0][j] +=  enjambre[i][2][j]

        enjambre[i][1] = funcionObjetivo(enjambre[i][0])

        if enjambre[i][1] < pbest[i][1]:
            pbest = enjambre[i][1]

        if pbest[i][1] < gbest[1]:
            gbest = pbest[i]

    print(gbest[1])


