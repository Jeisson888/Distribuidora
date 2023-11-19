import tkinter as tk
from tkinter import messagebox
import grafo as g
import caso_ejemplo
import vecino_mas_cercano as vmc
import fuerza_bruta as fb
import networkx as nx
import matplotlib.pyplot as plt

class FormularioCrearNodo(tk.Toplevel):
    def __init__(self, grafo, master=None):
        super().__init__(master)
        self.grafo = grafo
        self.title("Crear Nodo")

        # Estilos del formulario
        self.configure(bg='#E0E0E0')  # Color de fondo

        # Etiquetas y campos de entrada
        tk.Label(self, text="Nombre del nodo:", bg='#E0E0E0').pack(pady=5)
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)

        tk.Label(self, text="Tipo del nodo (almacen/punto_venta):", bg='#E0E0E0').pack(pady=5)
        self.tipo_entry = tk.Entry(self)
        self.tipo_entry.pack(pady=5)

        tk.Label(self, text="Ubicación (latitud, longitud):", bg='#E0E0E0').pack(pady=5)
        self.ubicacion_entry = tk.Entry(self)
        self.ubicacion_entry.pack(pady=5)

        # Botón para agregar el nodo
        btn_agregar = tk.Button(self, text="Agregar Nodo", command=self.agregar_nodo, bg='#4CAF50', fg='white', padx=10, pady=5)
        btn_agregar.pack(pady=10)

    def agregar_nodo(self):
        # Obtener valores del formulario
        nombre = self.nombre_entry.get()
        tipo = self.tipo_entry.get()
        ubicacion = tuple(map(float, self.ubicacion_entry.get().split(',')))

        # Agregar el nodo al grafo
        self.grafo.agregar_nodo(nombre, tipo, ubicacion)

        # Cerrar la ventana después de agregar el nodo
        self.destroy()

class InterfazGrafica:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplicación de Grafo")
        self.master.geometry("400x300")  # Tamaño de la ventana
        
        self.grafo = g.Grafo()

        # Estilo de botones
        self.estilo_botones = {
            'font': ('Arial', 12),
            'bg': '#4CAF50',  # Color de fondo verde
            'fg': 'white',    # Color de texto blanco
            'padx': 10,
            'pady': 5,
            'borderwidth': 2,
            'relief': 'groove'
        }

        # Botones
        self.btn_crear_nodo = tk.Button(master, text="Crear Nodo", command=self.abrir_formulario_nodo, **self.estilo_botones)
        self.btn_crear_nodo.pack(pady=10)

        self.btn_crear_arista = tk.Button(master, text="Crear Arista", command=self.crear_arista, **self.estilo_botones)
        self.btn_crear_arista.pack(pady=10)

        self.btn_ver_grafo = tk.Button(master, text="Ver Grafo", command=self.ver_grafo, **self.estilo_botones)
        self.btn_ver_grafo.pack(pady=10)

        self.btn_solucion_vmc = tk.Button(master, text="Solución VMC", command=self.solucion_vmc, **self.estilo_botones)
        self.btn_solucion_vmc.pack(pady=10)

        self.btn_solucion_fb = tk.Button(master, text="Solución FB", command=self.solucion_fb, **self.estilo_botones)
        self.btn_solucion_fb.pack(pady=10)
        
    def abrir_formulario_nodo(self):
        # Abre la ventana del formulario para crear un nodo
        FormularioCrearNodo(self.grafo, self.master)

    def crear_arista(self):
        # Implementa la lógica para crear una arista
        messagebox.showinfo("Crear Arista", "Funcionalidad para crear arista aún no implementada")

    def ver_grafo(self):
        # Implementa la lógica para visualizar el grafo
        messagebox.showinfo("Ver Grafo", "Funcionalidad para ver el grafo aún no implementada")

    def solucion_vmc(self):
        # Implementa la lógica para la solución VMC
        messagebox.showinfo("Solución VMC", "Funcionalidad para solución VMC aún no implementada")

    def solucion_fb(self):
        # Implementa la lógica para la solución FB
        messagebox.showinfo("Solución FB", "Funcionalidad para solución FB aún no implementada")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazGrafica(root)
    root.mainloop()