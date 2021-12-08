
archivo = open("datos.csv", "r")

contenido = archivo.readlines() ##lee el contenido completo del archivo
#convierte el archivo en una lista de lineas.

print("######################################################")
print("Contenido del Archivo: ")
print(contenido)
# Tenemos esto:
# contenido = ['luis,20\n', 'javier,19\n', 'grisel,16\n', 'cesar,21\n', 'jorge,18\n', 'maria,17']
#Pero la idea es pasar el contenido del archivo a:
#     lista = [["luis", 20], ["javier", 19], ...]
print("######################################################")

print("######################################################")
print("Contenido del archivo en lista de listas: ")
lista = [linea.split(",") for linea in contenido]
print(lista)
#Tenemos esto:
#[['luis', '20\n'], ['javier', '19\n'], ['grisel', '16\n'], ['cesar', '21\n'], ['jorge', '18\n'], ['maria', '17']]
#Falta convertir el valor númerico a numero y no cadena de caracteres como esta hasta ahora
print("######################################################")


print("######################################################")
print("Contenido del archivo finalmente convertido al formato deseado: ")
lista = [[linea[0], int(linea[1])] for linea in lista]
print(lista)
print("######################################################")

##UNA VEZ QUE TENEMOS LA LISTA COMO SE DESEA, SE PUEDE COMENZAR A TRABAJAR CON ELLA DE LA MANERA QUE
# SE REQUIERA... EN ESTE CASO, SE CALCULARA EL PROMEDIO DE TODOS LOS VALORES NUMERICOS DEL ARCHIVO

print("######################################################")
print("Promedio de edades en los registros(lineas) del archivo: ")
edades = [linea[1] for linea in lista]
print("Edades:", edades)
prom = sum(edades) / len(lista)
print("Promedio: ",prom)
print("######################################################")


#EEJEMPLO: BUSCAR EL ALUMNO CON LA EDAD MENOR E IMPRIMIR SU EDAD Y SU NOMBRE
print("######################################################")
print("Edades en los registros(lineas) del archivo: ")
edades = [linea[1] for linea in lista]
print(edades)
edadMenor = min(edades)
print("Edad menor: ", edadMenor)
indexAux = edades.index(edadMenor)
print("Indice Asociado a la Edad: ", indexAux)
print("Nombre del Alumno con Menor Edad: ", lista[indexAux][0])
