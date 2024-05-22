import random
import string
import tkinter as tk
from tkinter import ttk

MAX_LONGITUD = 50  # Longitud máxima permitida

def generar_contraseña(longitud, usar_mayus, usar_minus, usar_numeros, usar_simbolos):
    caracteres = ''
    if usar_mayus:
        caracteres += string.ascii_uppercase
    if usar_minus:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Seleccione al menos una opción de caracteres."

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def generar_nueva_contraseña():
    try:
        longitud = int(entry_longitud.get())
        if longitud > MAX_LONGITUD:
            lbl_contraseña.config(text=f"La longitud máxima es {MAX_LONGITUD} caracteres.")
            return
        
        usar_mayus = var_mayus.get()
        usar_minus = var_minus.get()
        usar_numeros = var_numeros.get()
        usar_simbolos = var_simbolos.get()
        
        contraseña = generar_contraseña(longitud, usar_mayus, usar_minus, usar_numeros, usar_simbolos)
        lbl_contraseña.config(text=contraseña)
    except ValueError:
        lbl_contraseña.config(text="Por favor, ingrese un número válido.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Generador de Contraseñas")

# Estilo para una apariencia más moderna
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TCheckbutton", font=("Helvetica", 12))

# Frame principal
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Longitud de la contraseña
lbl_longitud = ttk.Label(frame, text="Longitud de la contraseña:")
lbl_longitud.grid(row=0, column=0, pady=5, sticky=tk.W)
entry_longitud = ttk.Entry(frame, width=5)
entry_longitud.grid(row=0, column=1, pady=5, sticky=tk.W)

# Opciones de generación
var_mayus = tk.BooleanVar()
var_minus = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_simbolos = tk.BooleanVar()

chk_mayus = ttk.Checkbutton(frame, text="Incluir mayúsculas", variable=var_mayus)
chk_mayus.grid(row=1, column=0, pady=5, sticky=tk.W)
chk_minus = ttk.Checkbutton(frame, text="Incluir minúsculas", variable=var_minus)
chk_minus.grid(row=1, column=1, pady=5, sticky=tk.W)
chk_numeros = ttk.Checkbutton(frame, text="Incluir números", variable=var_numeros)
chk_numeros.grid(row=2, column=0, pady=5, sticky=tk.W)
chk_simbolos = ttk.Checkbutton(frame, text="Incluir símbolos", variable=var_simbolos)
chk_simbolos.grid(row=2, column=1, pady=5, sticky=tk.W)

# Botón para generar la contraseña
btn_generar = ttk.Button(frame, text="Generar Contraseña", command=generar_nueva_contraseña)
btn_generar.grid(row=3, column=0, columnspan=2, pady=10)

# Etiqueta para mostrar la contraseña generada
lbl_contraseña = ttk.Label(frame, text="", foreground="blue", font=("Helvetica", 12, "bold"))
lbl_contraseña.grid(row=4, column=0, columnspan=2, pady=5)

# Configurar la ventana para que se ajuste al contenido
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=1)
frame.rowconfigure(4, weight=1)

# Ajustar el tamaño de la ventana
root.geometry("400x300")
root.resizable(False, False)

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()
