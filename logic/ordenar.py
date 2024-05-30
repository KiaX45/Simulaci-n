import os
import shutil
class Ordenamiento:
    
    
    def __init__(self, lista_Extenciones, direccion):
        self.lista_Extenciones = lista_Extenciones
        self.direccion = direccion
        
    def ordenar(self):
        print(self.lista_Extenciones)
        os.chdir(self.direccion)
        print(os.getcwd())
        #Creamos las carpetas
        for nombre, extencion in self.lista_Extenciones:
            nombre_carpeta = crearDirectorio(nombre)
            #movemos los archivos a las carpetas
            print(nombre_carpeta)
            directorio_objetivo = os.path.join(self.direccion, nombre_carpeta)
            archivos_directorio = os.listdir()
            for archivo in archivos_directorio:
                if os.path.isfile(archivo):
                 ruta_archivo_origen = os.path.join(self.direccion, archivo)  
                 nombre_Archivo, extencion_arcivo = os.path.splitext(archivo)
                 if extencion_arcivo == extencion:
                     shutil.move(ruta_archivo_origen, directorio_objetivo)
                     print(f"el archivo {nombre_Archivo} se deberia mover a la carpeta {nombre_carpeta}")
        
                
def crearDirectorio(nombre, intento=1):
    try:
        os.mkdir(nombre)
        print(f"Directorio '{nombre}' creado.")
        return(nombre)
    except FileExistsError:
        nuevoNombre = f"{nombre}_{intento}"
        print(f"El directorio '{nombre}' ya existe, se reemplazará por '{nuevoNombre}'")
        return crearDirectorio(nuevoNombre, intento + 1)
