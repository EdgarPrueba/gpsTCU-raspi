#!/usr/bin/python3
import tkinter as tk
import subprocess

# Nombres de los scripts de las interfaces
name_bus = "src/interfaz.py"
name_parada = "src/Interfaz_Paradas.py"


# Función para correr interfaz y cerrar pantalla.
def run_script(script_name):
    root.destroy()
    subprocess.run(["python3", script_name])


# Crear la pantalla para escoger
root = tk.Tk()
root.title("Seleccionar Interfaz")
root.attributes('-fullscreen', True)
root.configure(bg='white')

# Frame principal
frame = tk.Frame(root, bg='white')
frame.place(relx=0.5, rely=0.5, anchor='center')

# Título
title_label = tk.Label(frame, text="Escoja interfaz:",
                       font=("Arial", 24, "bold"), bg='white')
title_label.pack(pady=20)

# Botones para escoger interfaz
bus_button = tk.Button(frame, text="Bus", font=("Arial", 20),
                       width=15, height=2,
                       command=lambda: run_script(name_bus))
bus_button.pack(pady=10)

parada_button = tk.Button(frame, text="Parada", font=("Arial", 20),
                          width=15, height=2,
                          command=lambda: run_script(name_parada))
parada_button.pack(pady=10)


# Si se sale de pantalla completa se destruye.
def exit_fullscreen(event):
    root.destroy()


# Se usa Esc como tecla para salir de pantalla completa.
root.bind("<Escape>", exit_fullscreen)

# Inicia la aplicación
root.mainloop()
