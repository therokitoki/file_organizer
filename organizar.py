import os
import shutil

#Diccionario de agrupaciones
EXT_DICT = {
    "Imágenes" : ["jpg","png","jpeg","gif"],
    "Documentos" : ["doc","docx","pdf"],
    "Música" : ["mp3","wav","flac"],
    "Videos" : ["mp4","mkv"],
    "Ejecutables" : ["exe","msi"],
    "APKs": ["apk"],
    "Sheets": ["xlsx", "xls", "csv"],
    "Photoshop":["psd"],
    "Archivos Comprimidos":["zip","rar","7z"]
}

#Decisión de directorio
print("Directorio actual: ",os.getcwd())
choice = int(input("¿Desea correr el script en el directorio actual? Si-1 No-0: "))
if choice == 1:
    path = os.getcwd()
else:
    path = input("Ingrese el directorio deseado: (Pegar con ctrl + V)")

print(f"Directorio seleccionado: {path}")

files = []
extensiones = []
directories = 0
for file in os.listdir(path):
    path_completo = os.path.join(path, file)
    if os.path.isdir(path_completo):
        directories += 1
        # skip directories
        continue
    else:
        files.append(file)
        extensiones.append(os.path.splitext(file)[1].replace('.',''))


print(f"Hay {len(files)} archivo/s y {directories} directorios en el directorio otorgado.\n")

menu = 1
while menu == 1:
    
    print("¿Qué desea hacer?")
    print(" 1. Organizar archivos por extensión automaticamente.")
    print(" 2. Organizar archivos que contengan cierta palabra en su nombre.")
    print(" 3. Organizar archivos con cierto filetype y cierta palabra en su nombre.")
    print(" 4. Organizar archivos por categoría.")
    print(" 0. Cancelar")
    eleccion = int(input("Ingrese la opción deseada: "))

    match eleccion:
        case 0:
            menu = 0

        case 1: #Organizar archivos por extensión automaticamente
            for file in files: 
                extension = (os.path.splitext(file))[1].replace('.','')
                if os.path.exists(path+'/'+extension):
                    shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
                else:
                    os.makedirs(path+'/'+extension)
                    shutil.move(path+'/'+file,path+'/'+extension+'/'+file)

        case 2: #Organizar archivos con cierto filetype y cierta palabra en su nombre.
            palabra = input("Ingrese la palabra: ")
            palabra.lower()
            count = 0

            for file in files:
                
                nombre = (os.path.splitext(file))[0]
                if palabra in nombre.lower():
                     count += 1
                     if os.path.exists(path+'/'+palabra):
                        shutil.move(path+'/'+file,path+'/'+palabra+'/'+file)
                     else:
                        os.makedirs(path+'/'+palabra)
                        shutil.move(path+'/'+file,path+'/'+palabra+'/'+file)
            if count == 0:
                print(f"No se encontraron archivos con la palabra '{palabra}'")        
            else:
                print(f"Se encontraron y guardaron {count} archivos con la palabra '{palabra}' en ellos.")
        
        case 3: #Organizar archivos que contengan cierta palabra en su nombre.
            palabra = input("Ingrese la palabra: ")
            palabra.lower()
            count = 0
            cancelar = 0
            
            #Selección de la extensión.
            print("Extensiones disponibles: ")
            for i in extensiones:
                print(i)
            flag = 1
            while flag == 1:
                ext = input("Ingrese la extensión a buscar: ")
                if ext == '0':
                    flag = 0
                    cancelar = 1
                    break
                elif ext not in extensiones:
                    print("La extensión debe estar presente en el directorio. Ingrese 0 para cancelar.")
                else:
                    flag = 0
            
            #Busca la palabra y la extensión
            for file in files:
                nombre = (os.path.splitext(file))
                if (palabra in (nombre[0]).lower()) and (ext in nombre[1]):
                     count += 1
                     if os.path.exists(path+'/'+palabra):
                        shutil.move(path+'/'+file,path+'/'+palabra+'/'+file)
                     else:
                        os.makedirs(path+'/'+palabra)
                        shutil.move(path+'/'+file,path+'/'+palabra+'/'+file)
            
            #Checks finales
            if cancelar == 1:
                print("Se canceló la operación.")
            elif count == 0:
                print(f"No se encontraron archivos con la palabra '{palabra}' y la extensión '{ext}'")        
            else:
                print(f"Se encontraron y guardaron {count} archivos con la palabra '{palabra}' y la extension '{ext}' en ellos.")
        case 4:
            categorias = EXT_DICT.keys()
            extensiones_presentes = set(extensiones) # Elimino duplicados
            for key,values in EXT_DICT.items():
                for extension in extensiones_presentes:
                    if extension in values:
                        if os.path.exists(path+'/'+key):
                            break
                        else:
                            os.makedirs(path+'/'+key)
            
            for file in files: 
                extension = (os.path.splitext(file))[1].replace('.','')
                for key,values in EXT_DICT.items():
                    if extension in values:
                    
                        shutil.move(path+'/'+file,path+'/'+key+'/'+file)
                        break

        case _:
            print("El número ingresado no es válido, inténtelo de nuevo.")
    
    if menu != 0:
        menu = int(input("¿Desea realizar otra acción? (Si-1/No-0)"))
