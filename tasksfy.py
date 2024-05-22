import tkinter as tk
from tkinter import messagebox
import json
import os

class RecordatorioDeTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Recordatorio de Tareas")
        self.tareas = []

        # Ruta del archivo de tareas
        self.ruta_tareas = os.path.join(os.path.expanduser("~"), "tareas.json")

        # Cargar tareas al inicio
        self.cargar_tareas()

        # Configuración de la interfaz gráfica
        self.label = tk.Label(root, text="Tarea:")
        self.label.pack()

        self.entry = tk.Entry(root, width=40)
        self.entry.pack()

        self.button_agregar = tk.Button(root, text="Agregar Tarea", command=self.agregar_tarea)
        self.button_agregar.pack()

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack()

        self.button_completar = tk.Button(root, text="Marcar como Completada", command=self.marcar_como_completada)
        self.button_completar.pack()

        self.actualizar_listbox()

    def agregar_tarea(self):
        tarea = self.entry.get()
        if tarea:
            self.tareas.append(tarea)
            self.guardar_tareas()
            self.listbox.insert(tk.END, tarea)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea.")

    def marcar_como_completada(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            index = seleccion[0]
            tarea = self.listbox.get(index)
            messagebox.showinfo("Tarea Completada", f"La tarea '{tarea}' ha sido marcada como completada.")
            self.listbox.delete(index)
            self.tareas.remove(tarea)
            self.guardar_tareas()
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea.")

    def guardar_tareas(self):
        try:
            with open(self.ruta_tareas, "w") as archivo:
                json.dump(self.tareas, archivo)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar las tareas: {e}")

    def cargar_tareas(self):
        if os.path.exists(self.ruta_tareas):
            try:
                with open(self.ruta_tareas, "r") as archivo:
                    self.tareas = json.load(archivo)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar las tareas: {e}")
                self.tareas = []

    def actualizar_listbox(self):
        self.listbox.delete(0, tk.END)
        for tarea in self.tareas:
            self.listbox.insert(tk.END, tarea)

def main():
    root = tk.Tk()
    app = RecordatorioDeTareas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
