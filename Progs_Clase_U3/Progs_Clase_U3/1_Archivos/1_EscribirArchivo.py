
archivo = open("datosResultado.csv", "w")

lineas  = [["Antonio", 23],["Alejandra", 19]]

#print(lineas)

#archivo.write( "{0},{1}\n".format(nombre, dato) for nombre, dato in lineas)

for i in lineas:
    print("linea: ", i )
    archivo.write( i[0] + "," + str(i[1]) +"\n")


