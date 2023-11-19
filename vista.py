import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import grafo
import caso_ejemplo
import vecino_mas_cercano as vmc
import fuerza_bruta as fb
import networkx as nx
import matplotlib.pyplot as plt

class Vista:
    def __init__(self, master):
        self.master = master
        self.master.title("Distribuidora")
        
        self.contenedor = tk.Frame(master, padx=20, pady=20)
        self.contenedor.pack(expand=True, fill="both")
        
        self.modelo = grafo.Grafo()

        self.estilo_botones = {
            'font': ('Arial', 12),
            'bg': 'green',
            'fg': 'white',
            'padx': 10,
            'pady': 5,
            'borderwidth': 2,
            'relief': 'groove'
        }

        self.btn_cargar_datos_caso_ejemplo = tk.Button(self.contenedor, text="Cargar Datos Caso Ejemplo", command=self.cargar_datos_caso_ejemplo, **self.estilo_botones)
        self.btn_cargar_datos_caso_ejemplo.pack(pady=10)
        
        self.btn_crear_nodo = tk.Button(self.contenedor, text="Crear Lugar", command=self.crear_nodo, **self.estilo_botones)
        self.btn_crear_nodo.pack(pady=10)
        
        self.btn_borrar_nodo = tk.Button(self.contenedor, text="Borrar Lugar", command=self.borrar_nodo, **self.estilo_botones)
        self.btn_borrar_nodo.pack(pady=10)

        self.btn_crear_arista = tk.Button(self.contenedor, text="Crear Ruta", command=self.crear_arista, **self.estilo_botones)
        self.btn_crear_arista.pack(pady=10)
        
        self.btn_borrar_arista = tk.Button(self.contenedor, text="Borrar Ruta", command=self.borrar_arista, **self.estilo_botones)
        self.btn_borrar_arista.pack(pady=10)

        self.btn_ver_grafo = tk.Button(self.contenedor, text="Ver Grafo", command=self.ver_grafo, **self.estilo_botones)
        self.btn_ver_grafo.pack(pady=10)

        self.btn_solucion_fb = tk.Button(self.contenedor, text="Solución Fuerza Bruta", command=self.solucion_fb, **self.estilo_botones)
        self.btn_solucion_fb.pack(pady=10)
        
        self.btn_solucion_vmc = tk.Button(self.contenedor, text="Solución Vecino Mas Cercano", command=self.solucion_vmc, **self.estilo_botones)
        self.btn_solucion_vmc.pack(pady=10)

    def cargar_datos_caso_ejemplo(self):
        caso_ejemplo.cargar_datos(self.modelo)

    def crear_nodo(self):
        FormularioCrearNodo(self.modelo, self.contenedor)
        
    def borrar_nodo(self):
        FormularioBorrarNodo(self.modelo, self.contenedor)

    def crear_arista(self):
        FormularioCrearArista(self.modelo, self.contenedor)

    def borrar_arista(self):
        FormularioBorrarArista(self.modelo, self.contenedor)

    def ver_grafo(self):
        grafo_networkx = nx.Graph()
        for nodo in self.modelo.nodos.values():
            grafo_networkx.add_node(nodo.nombre, ubicacion=nodo.ubicacion)
        for arista in self.modelo.aristas.values():
            grafo_networkx.add_edge(arista.nodo_1, arista.nodo_2, peso=arista.calcular_peso())
        posiciones = nx.get_node_attributes(grafo_networkx, 'ubicacion')
        pesos = nx.get_edge_attributes(grafo_networkx, 'peso')
        nx.draw(grafo_networkx, posiciones, with_labels=True, node_color='lightblue', node_size=2000)
        nx.draw_networkx_edge_labels(grafo_networkx, posiciones, edge_labels=pesos)
        plt.show()

    def solucion_fb(self):
        FormularioFB(self.modelo, self.contenedor)
        
    def solucion_vmc(self):
        FormularioVMC(self.modelo, self.contenedor)
     
class FormularioCrearNodo(tk.Toplevel):
    def __init__(self, grafo, master=None):
        super().__init__(master)
        self.title("Crear Lugar")
        self.grafo = grafo

        self.configure(bg='#E0E0E0')

        tk.Label(self, text="Nombre del lugar:", bg='#E0E0E0').pack(pady=5)
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)

        tk.Label(self, text="Tipo de lugar:", bg='#E0E0E0').pack(pady=5)
        tipos_lugar = ["almacen", "punto_venta"]
        self.tipo_combobox = ttk.Combobox(self, values=tipos_lugar)
        self.tipo_combobox.pack(pady=5)

        tk.Label(self, text="Ubicación (latitud, longitud):", bg='#E0E0E0').pack(pady=5)
        self.ubicacion_entry = tk.Entry(self)
        self.ubicacion_entry.pack(pady=5)

        btn_agregar = tk.Button(self, text="Agregar Lugar", command=self.agregar_nodo, bg='green', fg='white', padx=10, pady=5)
        btn_agregar.pack(pady=10)

    def agregar_nodo(self):
        nombre = self.nombre_entry.get()
        tipo = self.tipo_combobox.get()
        ubicacion = tuple(map(float, self.ubicacion_entry.get().split(',')))
        self.grafo.agregar_nodo(nombre, tipo, ubicacion)
        self.destroy()
      
class FormularioBorrarNodo(tk.Toplevel):
    def __init__(self, grafo, master=None):
        super().__init__(master)
        self.title("Borrar Lugar")
        self.grafo = grafo

        self.configure(bg='#E0E0E0')

        tk.Label(self, text="Nombre del lugar:", bg='#E0E0E0').pack(pady=5)
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)

        btn_agregar = tk.Button(self, text="Borrar Lugar", command=self.borrar_nodo, bg='green', fg='white', padx=10, pady=5)
        btn_agregar.pack(pady=10)

    def borrar_nodo(self):
        nombre = self.nombre_entry.get()
        self.grafo.borrar_nodo(nombre)
        self.destroy()
        
class FormularioCrearArista(tk.Toplevel):
    def __init__(self, grafo, master=None):
        super().__init__(master)
        self.title("Crear Ruta")
        self.grafo = grafo

        self.configure(bg='#E0E0E0')

        tk.Label(self, text="Nombre del lugar 1:", bg='#E0E0E0').pack(pady=5)
        self.lugar_1_entry = tk.Entry(self)
        self.lugar_1_entry.pack(pady=5)
        
        tk.Label(self, text="Nombre del lugar 2:", bg='#E0E0E0').pack(pady=5)
        self.lugar_2_entry = tk.Entry(self)
        self.lugar_2_entry.pack(pady=5)
        
        tk.Label(self, text="Costo promedio (miles de pesos):", bg='#E0E0E0').pack(pady=5)
        self.costo_entry = tk.Entry(self)
        self.costo_entry.pack(pady=5)
        
        tk.Label(self, text="Tiempo promedio (horas):", bg='#E0E0E0').pack(pady=5)
        self.tiempo_entry = tk.Entry(self)
        self.tiempo_entry.pack(pady=5)
        
        tk.Label(self, text="Distancia (kilometros):", bg='#E0E0E0').pack(pady=5)
        self.distancia_entry = tk.Entry(self)
        self.distancia_entry.pack(pady=5)

        btn_agregar = tk.Button(self, text="Agregar Ruta", command=self.agregar_ruta, bg='green', fg='white', padx=10, pady=5)
        btn_agregar.pack(pady=10)

    def agregar_ruta(self):
        lugar_1 = self.lugar_1_entry.get()
        lugar_2 = self.lugar_2_entry.get()
        costo = int(self.costo_entry.get())
        tiempo = int(self.tiempo_entry.get())
        distancia = int(self.distancia_entry.get())
        self.grafo.agregar_arista(lugar_1, lugar_2, costo, tiempo, distancia)
        self.destroy()

class FormularioBorrarArista(tk.Toplevel):
    def __init__(self, grafo, master=None):
        super().__init__(master)
        self.title("Borrar Ruta")
        self.grafo = grafo

        self.configure(bg='#E0E0E0')

        tk.Label(self, text="Nombre del lugar 1:", bg='#E0E0E0').pack(pady=5)
        self.lugar_1_entry = tk.Entry(self)
        self.lugar_1_entry.pack(pady=5)
        
        tk.Label(self, text="Nombre del lugar 2:", bg='#E0E0E0').pack(pady=5)
        self.lugar_2_entry = tk.Entry(self)
        self.lugar_2_entry.pack(pady=5)

        btn_agregar = tk.Button(self, text="Borrar Ruta", command=self.agregar_ruta, bg='green', fg='white', padx=10, pady=5)
        btn_agregar.pack(pady=10)

    def agregar_ruta(self):
        lugar_1 = self.lugar_1_entry.get()
        lugar_2 = self.lugar_2_entry.get()
        self.grafo.borrar_arista(lugar_1, lugar_2)
        self.destroy()
        
class FormularioFB(tk.Toplevel):
    def __init__(self, grafo, master=None):
        super().__init__(master)
        self.title("Calcular mejor ruta (fuerza bruta)")
        self.grafo = grafo

        self.configure(bg='#E0E0E0')

        tk.Label(self, text="Nombre del almacen:", bg='#E0E0E0').pack(pady=5)
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)

        btn_agregar = tk.Button(self, text="Calcular", command=self.mostrar, bg='green', fg='white', padx=10, pady=5)
        btn_agregar.pack(pady=10)

    def mostrar(self):
        origen = self.nombre_entry.get()
        mejor_ruta = fb.fuerza_bruta(self.grafo, origen)
        messagebox.showinfo("Solución FB", f"La mejor ruta es: {mejor_ruta}")
        self.destroy()
        
class FormularioVMC(tk.Toplevel):
    def __init__(self, grafo, master=None):
        super().__init__(master)
        self.title("Calcular mejor ruta (vecino mas cercano)")
        self.grafo = grafo

        self.configure(bg='#E0E0E0')

        tk.Label(self, text="Nombre del almacen:", bg='#E0E0E0').pack(pady=5)
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)

        btn_agregar = tk.Button(self, text="Calcular", command=self.mostrar, bg='green', fg='white', padx=10, pady=5)
        btn_agregar.pack(pady=10)

    def mostrar(self):
        origen = self.nombre_entry.get()
        mejor_ruta = vmc.vecino_mas_cercano(self.grafo, origen)
        messagebox.showinfo("Solución VMC", f"La mejor ruta es: {mejor_ruta}")
        self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Vista(root)
    root.mainloop()