import tkinter as tk
from tkinter import messagebox
import json
import os

class GuardadorDeContactos:
    def __init__(self, root):
        self.root = root
        self.root.title("Guardador de Contactos")
        self.contactos = []

        # Ruta del archivo de contactos
        self.ruta_contactos = os.path.join(os.path.expanduser("~"), "contactos.json")

        # Cargar contactos al inicio
        self.cargar_contactos()

        # Configuración de la interfaz gráfica
        self.label_nombre = tk.Label(root, text="Nombre:")
        self.label_nombre.pack()

        self.entry_nombre = tk.Entry(root, width=40)
        self.entry_nombre.pack()

        self.label_telefono = tk.Label(root, text="Teléfono:")
        self.label_telefono.pack()

        self.entry_telefono = tk.Entry(root, width=40)
        self.entry_telefono.pack()

        self.label_correo = tk.Label(root, text="Correo Electrónico (opcional):")
        self.label_correo.pack()

        self.entry_correo = tk.Entry(root, width=40)
        self.entry_correo.pack()

        self.label_direccion = tk.Label(root, text="Dirección (opcional):")
        self.label_direccion.pack()

        self.entry_direccion = tk.Entry(root, width=40)
        self.entry_direccion.pack()

        self.button_agregar = tk.Button(root, text="Agregar Contacto", command=self.agregar_contacto)
        self.button_agregar.pack()

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack()

        self.button_eliminar = tk.Button(root, text="Eliminar Contacto", command=self.eliminar_contacto)
        self.button_eliminar.pack()

        self.actualizar_listbox()

    def agregar_contacto(self):
        nombre = self.entry_nombre.get()
        telefono = self.entry_telefono.get()
        correo = self.entry_correo.get()
        direccion = self.entry_direccion.get()

        if nombre and telefono:
            contacto = {"nombre": nombre, "telefono": telefono}
            if correo:
                contacto["correo"] = correo
            if direccion:
                contacto["direccion"] = direccion

            self.contactos.append(contacto)
            self.guardar_contactos()
            self.listbox.insert(tk.END, f"{nombre} - {telefono}")
            self.entry_nombre.delete(0, tk.END)
            self.entry_telefono.delete(0, tk.END)
            self.entry_correo.delete(0, tk.END)
            self.entry_direccion.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa al menos el nombre y el teléfono del contacto.")

    def eliminar_contacto(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            index = seleccion[0]
            contacto = self.listbox.get(index)
            self.listbox.delete(index)
            self.contactos.pop(index)
            self.guardar_contactos()
            messagebox.showinfo("Contacto Eliminado", f"El contacto '{contacto}' ha sido eliminado.")
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona un contacto.")

    def guardar_contactos(self):
        try:
            with open(self.ruta_contactos, "w") as archivo:
                json.dump(self.contactos, archivo)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar los contactos: {e}")

    def cargar_contactos(self):
        if os.path.exists(self.ruta_contactos):
            try:
                with open(self.ruta_contactos, "r") as archivo:
                    self.contactos = json.load(archivo)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar los contactos: {e}")
                self.contactos = []

    def actualizar_listbox(self):
        self.listbox.delete(0, tk.END)
        for contacto in self.contactos:
            display_text = f"{contacto['nombre']} - {contacto['telefono']}"
            if 'correo' in contacto:
                display_text += f" - {contacto['correo']}"
            if 'direccion' in contacto:
                display_text += f" - {contacto['direccion']}"
            self.listbox.insert(tk.END, display_text)

def main():
    root = tk.Tk()
    app = GuardadorDeContactos(root)
    root.mainloop()

if __name__ == "__main__":
    main()
