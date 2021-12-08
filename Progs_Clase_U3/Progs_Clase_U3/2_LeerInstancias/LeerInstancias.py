archivo = open("instancia.csv","r")

contenido = archivo.readlines()

print("######################################################")
print("Contenido del Archivo: ")
print(contenido)
# Tenemos esto:
# contenido = ['LEYVA,20,20,14, APROBADO\n', 'PABLO,19,15,20, REPROBADO\n', 'PEDRO,16,10,6, REPROBADO\n', 'VICTOR,21,23,10, APROBADO\n']
#Pero la idea es pasar el contenido del archivo a:
#     lista = ["luis", [20, 20, 14], "APROBADO"],...]
print("######################################################")


print("######################################################")
print("Contenido del archivo en lista de listas: ")
lista = [linea.split(",") for linea in contenido]
print(lista)
#Tenemos esto:
#[['LEYVA', '20', '20', '14', ' APROBADO\n'], ['PABLO', '19', '15', '20', ' REPROBADO\n']]
#Falta convertir el valor númerico a numero y no cadena de caracteres como esta hasta ahora
print("######################################################")

print("######################################################")
print("Contenido del archivo finalmente convertido al formato deseado: ")
#########  nombre  vector caracteristicas    clase
lista =  [ [x[0], list(map(int, x[1:4])), x[4].replace("\n","") ]  for x in lista]
print(lista)
print("######################################################")