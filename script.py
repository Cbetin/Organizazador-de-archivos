from tkinter import ttk
from tkinter import *

import shutil, os

# Ruta donde se guardo este archico y donde se desea hacer una organizacion de archivos
ruta_actual = os.getcwd()

# Lista con los nombres de los archivos que existen en ruta_actual                                       
lista_archivos = os.listdir(ruta_actual)

carpeta_principal = "Archivos organizados"

# Funcion para crear la carpetas en donde se organizaran los archivos
def crear_folders(carpetas):
    # carpetas: {"Texto": ".txt;.doc;.docx", "Video": ".jpg;.gif;.bmp;.png"}

    # Recorrer el diccionario
    for nombre, extension in carpetas.items():
        # crear la ruta
        a1 = os.path.join(ruta_actual, carpeta_principal, nombre)
        try:
            # crear la carpeta
            os.makedirs(a1)
        except:
            # No se pudo crear la carpeta
            print("Error creando la carpeta")

# Funcion para organizar los archivos
def organizar_archivos(lista_extensiones, carpeta):
    global lista_archivos
    
    # Recorrer lista de archivos en la carpeta
    for filename in lista_archivos:                     
        # Recorrer el diccionario
        for extension in lista_extensiones:
            # verificar extension
            if filename.endswith(extension):
                try:
                    a = os.path.join(ruta_actual, filename)    
                    shutil.move(a, carpeta)
                except:
                    print(f"Ya existe el archivo: {filename}")

def ordenar_archivos(carpetas):
    global ruta_actual
    # Recorrer el diccionario
    for nombre, extension in carpetas.items():
        # crear ruta
        a1 = os.path.join(ruta_actual, carpeta_principal, nombre)
        lista_extensiones = extension.split(";")
        # organizar todos los archivos de una extension
        organizar_archivos(lista_extensiones, a1)


class Application:
    def __init__(self, window):
        self.window = window
        self.window.title("Ordenador de Archivos")

        # Carpetas y extensiones por defecto
        self.carpetas = {
            "Texto": ".txt;.doc;.docx",
            "Video": ".jpg;.gif;.bmp;.png",
            "Ejecución o del sistema": ".exe;.bat;.dll;.sys",
            "Audio": ".mp3;.wav;.wma",
            "Archivos comprimidos": ".zip;.rar;.tar",
            "Lectura": ".pdf;.epub;.azw;ibook;.ppt;.pptx;.pptm;.epub"
        }

        # Subtitulo del formulario
        frame = LabelFrame(self.window, text="Registrar Extension")
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Input de Registro
        Label(frame, text = "Nombre de la nueva Carpeta").grid(row = 1, column = 0)
        self.nombre_carpeta = Entry(frame)
        self.nombre_carpeta.insert(0, "Imagen")
        self.nombre_carpeta.focus()
        self.nombre_carpeta.grid(row = 1, column = 1)

        # Extensiones
        Label(frame, text = "Extensiones que van en la Carpeta").grid(row = 2, column = 0)
        self.extensiones = Entry(frame)
        self.extensiones.insert(0, ".jpg;.gif;.bmp;.png")
        self.extensiones.focus()
        self.extensiones.grid(row = 2, column = 1)

        # Buton de Registro 
        ttk.Button(frame, text = 'Registrar Carpeta', command = self.registrar_carpeta).grid(row = 3, columnspan = 2, sticky = W + E)
        
        # Subtitulo de Correr aplicacion
        frame = LabelFrame(self.window, text="Correr Aplicacion")
        frame.grid(row=4, column=0, columnspan=3, pady=20)

        # Boton de ejecuar aplicacion
        ttk.Button(frame, text = 'Ejecutar Applicación', command = self.ejecutar_ordenador).grid(row = 6, columnspan = 2, sticky = W + E)

        # Tabla de carpetas y extensiones
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 8, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Carpeta', anchor = CENTER)
        self.tree.heading('#1', text = 'Extensiones', anchor = CENTER)
        self.mostrar_productos_en_tabla()

    def registrar_carpeta(self):
        # Se ejecuta cuando se da click en el boton "Registrar Carpeta"

        # Registra la carpeta
        nombre = self.nombre_carpeta.get()
        extension = self.extensiones.get()
        self.carpetas[nombre] = extension
        self.mostrar_productos_en_tabla()

        # Limpia los inputs
        self.nombre_carpeta.delete(0, END)
        self.extensiones.delete(0, END)

    def ejecutar_ordenador(self):
        # crear los folders
        crear_folders(self.carpetas)
        # Ordena los archivos en la carpeta correspondiente
        ordenar_archivos(self.carpetas)

    def mostrar_productos_en_tabla(self):
        # Elimina los datos en la tabla actual
        carpetas = self.tree.get_children()
        for element in carpetas:
            self.tree.delete(element)
        
        # Muestra los tados en la tabla
        for key, value in self.carpetas.items():
            self.tree.insert('', 0, text = key, values = value)

# Crear la ventana en Tkinter
window = Tk()
app = Application(window)
window.mainloop()