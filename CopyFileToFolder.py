import shutil
import os

#Se tiene el archivo en la ruta \\192.168.14.70\login
#Se crea una unidad de red que apunte a esa ruta y se le asigna la letra G a la unidad.
#En el ejemplo el usuario y clave seria invitado
#Se crea la carpeta exe1 en la unidad C
#Seria interesante cada cierto tiempo verificar si hay alguna actualización. 
#Se podria por ejemplo analizar el MD5 o SHA256 de los dos archivos, si es diferente entonces remplazarlo.


src="U:"         #ejemplo: Unidad compartida
dest="C:\exe1"   #Ruta creada en la unidad C
toSearch="login.exe"                                  #example: "archivo.extension"
folder=file=0

try:
    os.makedirs(dest)
except:
    print("ARCHIVO EXISTE")
def checkFile(src,searchFile):                                  #Recursive Fuction to Check the file in each Folder
    global folder,file
    src_file = os.listdir(src)                                  #listDir returns all files and folder within the src in src_file
    for file_name in src_file:
        full_file_name = os.path.join(src, file_name)           #this create a path by joining src and file_name
        if os.path.isdir(full_file_name):                       #check weather it is a directory or a file
            folder += 1
            checkFile(full_file_name,toSearch)                  #Again call the function recursively until it reach the last folder
        else:
            if file_name == toSearch:
                shutil.copy(full_file_name, dest)               #Copy the file to the destination folder
            file += 1

checkFile(src,toSearch)
print("FOLDER",folder)                                            #COUNT OF TOTAL FOLDERS
print("FILE",file)                                                #COUNT OF TOTAL FILES
