

###CARGAR INSTANCIA

archivo = open("Instancia.txt","r")

contenido = archivo.readlines()

print(contenido)


lista = [linea.split("\t") for linea in contenido]
print(lista)

# [ [ [ 1, 80, 90 ,..., 90 ], 'Guerrero'],
#   [ [ 2, 75, 59 ,..., 90 ], 'Duelista']
# ]

instancia = [ [ list(map(int,x[:6])), x[6] ] for x in lista ]
print(instancia)

##############################################################################
##SELECCIÓN / CREACIÓN DEL VECTOR A CLASIFICAR
NC = [89, 67, 33, 50, 100, 76]
##############################################################################
###DEFINIR EL VALOR DE "K"  - Un número entre 1 y el total de registros de la instancia
K = 5
##############################################################################

estructuraDatos = {}

from MetricasSimilitud import Metricas as m

for contador, i in enumerate(instancia):
    distancia_NC_i = m.Euclidiana(NC, i[0])
    #print(distancia_NC_i)
    estructuraDatos[contador] = distancia_NC_i

print(estructuraDatos)

ordenado = sorted(estructuraDatos.items(), key=lambda x: x[1])

print(ordenado)


temporalK = []
for i in range(K):
    etiqueta = ordenado[i][0]
    #print(etiqueta)
    registro = instancia[etiqueta]
    #print(registro)
    temporalK.append(registro[1])

print(temporalK)

########################################################################
##ENCONTRAR LA MODA EN "TEMPORAL_K" PARA ASIGNAR ESA ETIQUETA/CLASE AL VECTOR "NC"

#TAREA X.   ENCONTRAR LA MODA EN LOS K VECTORES

