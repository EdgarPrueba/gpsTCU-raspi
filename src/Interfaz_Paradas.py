import tkinter as tk
import threading
import sqlite3
import requests
import json
from tkinter import ttk

font = ("Helvetica", 20)

    
class InterfazMain(tk.Tk):
    """Clase para la generación de la interfaz principal.


    :param tk: Clase para interfaces con Tkinter
    :type tk: Objeto Tk
    """
    def __init__(self):
        super().__init__()
        # Inicia en fullscreen, para salir se usa Esc
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", lambda event:
                  self.attributes("-fullscreen", False))
        self.title("Tabla con Tkinter")

        self.geometry("800x480")
        def seleccionar(event):
            print("Has seleccionado:", combobox.get())

        # Crear el Combobox
        opciones = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]
        combobox = ttk.Combobox(self, values=opciones, state="readonly")
        combobox.pack(pady=20)

        # Configurar la opción predeterminada
        combobox.set("Selecciona una opción")

        # Asociar un evento al combobox
        combobox.bind("<<ComboboxSelected>>", seleccionar)






        # Datos para la tabla
        headers = ["Direccion", "Llegada"]
        data = self.buscar_data()
        table_frame = tk.Frame(self)
        table_frame.pack(pady=20)

        # Crear los encabezados
        for col, header in enumerate(headers):
            label = tk.Label(table_frame, text=header, bg="gray", fg="white", width=25, font=font)
            label.grid(row=0, column=col, padx=10, pady=10)

        # Agregar los datos a la tabla
        for row, record in enumerate(data, start=1):
            for col, value in enumerate(record.values()):
                color_fondo = "white"
                if col == 1:
                    if value < 5:
                        color_fondo = "red"
                    elif value < 15:
                        color_fondo = "yellow"
                    else:
                        color_fondo = "green"

                label = tk.Label(table_frame, text=value, bg=color_fondo, fg="black", width=25, font=font)
                label.grid(row=row, column=col, padx=10, pady=10)
    def create_widgets_Parada(self):
        self.login_frame = tk.Frame(self, bg="lightblue")
        self.login_frame.pack(fill='both')

        self.parada_pass_frame = tk.Frame(self.login_frame, bg="lightblue")
        self.parada_pass_frame.pack(pady=20)

        
    def on_closing(self):
        """Finaliza el programa correctamente.
        """
        # Asegurarse de que el hilo de GPS se detenga antes de cerrar
        self.destroy()
    def buscar_data(self):
        #Busquedad en Archivo
        with open("src/prueba_paradas.json") as paradas:
            data = json.load(paradas)
        
        #Busqueda en API
        ###################



        ###################


        return data["buses_por_llegar"]



if __name__ == "__main__":
    app = InterfazMain()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()