
def Guardar(nombreArchivo, datos):
    archivo = open("../../Progs_Clase_U3/"+nombreArchivo+".csv","w")
 #.../
 # /

    for i in datos:
        archivo.write(str(i) + "\n")
    archivo.flush()
    archivo.close()


d = ["10,4,5,8", "20,12,56,87,24,78,54", "30,12,56,34"]
Guardar("Prueba", d)