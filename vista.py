import tkinter as tk
from tkinter import ttk, messagebox
import grafo
import caso_ejemplo
import vecino_mas_cercano as vmc
import fuerza_bruta as fb
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Vista:
    def __init__(self, master):
        self.master = master
        self.master.title("Optimizacion de ruta")

        self.contenedor = tk.Frame(master, padx=20, pady=20)
        self.contenedor.pack(expand=True, fill="both")

        # Título
        titulo_label = tk.Label(self.contenedor, text="Optimización de ruta", font=('Arial', 16, 'bold'))
        titulo_label.pack(side="top", pady=10)

        self.grafo = grafo.Grafo()

        # Panel izquierdo con botones
        self.panel_izquierdo = tk.Frame(self.contenedor)
        self.panel_izquierdo.pack(side="left", padx=10)

        self.estilo_botones = {
            'font': ('Arial', 12),
            'bg': 'green',
            'fg': 'white',
            'padx': 10,
            'pady': 5,
            'borderwidth': 2,
            'relief': 'groove'
        }

        self.crear_botones()

        # Panel derecho para mostrar la información y los formularios
        self.panel_derecho = tk.Frame(self.contenedor, bg='lightgray')
        self.panel_derecho.pack(side="left", padx=10, fill="both", expand=True)

        # Crear un nuevo panel a la derecha para los formularios
        self.panel_formularios = tk.Frame(self.contenedor, bg='lightgray')
        self.panel_formularios.pack(side="right", padx=10, fill="both", expand=True)

        # Crear el lienzo para la visualización del grafo en tiempo real
        self.fig, self.ax = plt.subplots(figsize=(5, 5), tight_layout=True)
        self.canvas = FigureCanvasTkAgg(self.fig, self.panel_derecho)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Mostrar grafo por defecto en el panel derecho
        self.actualizar_visualizacion()
        
        # Variable para almacenar el formulario actual
        self.formulario_actual = None

        # Vincular el evento de cierre de la ventana a self.cerrar_ventana
        master.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        
    def cerrar_ventana(self):
        self.master.destroy()
        self.master.quit()

    def crear_botones(self):
        botones_izquierda = [
            ("Cargar Datos Caso Ejemplo", self.cargar_datos_caso_ejemplo),
            ("Crear Lugar", self.crear_nodo),
            ("Borrar Lugar", self.borrar_nodo),
            ("Crear Ruta", self.crear_arista),
            ("Borrar Ruta", self.borrar_arista),
            ("Ver Grafo", self.ver_grafo),
            ("Solución Fuerza Bruta", self.solucion_fb),
            ("Solución Vecino Mas Cercano", self.solucion_vmc),
        ]

        for texto, comando in botones_izquierda:
            boton = tk.Button(self.panel_izquierdo, text=texto, command=comando, **self.estilo_botones)
            boton.pack(pady=10, fill='x')

    def cargar_datos_caso_ejemplo(self):
        caso_ejemplo.cargar_datos(self.grafo)
        self.actualizar_visualizacion()

    def crear_nodo(self):
        self.destruir_formulario_actual()
        self.formulario_actual = FormularioCrearNodo(self.grafo, self.panel_formularios)
        self.actualizar_visualizacion()

    def borrar_nodo(self):
        self.destruir_formulario_actual()
        self.formulario_actual = FormularioBorrarNodo(self.grafo, self.panel_formularios)
        self.actualizar_visualizacion()

    def crear_arista(self):
        self.destruir_formulario_actual()
        self.formulario_actual = FormularioCrearArista(self.grafo, self.panel_formularios)
        self.actualizar_visualizacion()

    def borrar_arista(self):
        self.destruir_formulario_actual()
        self.formulario_actual = FormularioBorrarArista(self.grafo, self.panel_formularios)
        self.actualizar_visualizacion()

    def solucion_fb(self):
        self.destruir_formulario_actual()
        self.formulario_actual = FormularioFB(self.grafo, self.panel_formularios)
        self.actualizar_visualizacion()

    def solucion_vmc(self):
        self.destruir_formulario_actual()
        self.formulario_actual = FormularioVMC(self.grafo, self.panel_formularios)
        self.actualizar_visualizacion()

    def destruir_formulario_actual(self):
        # Destruye el formulario actual si existe
        if self.formulario_actual:
            self.formulario_actual.destroy()

    def ver_grafo(self):
        grafo_networkx = nx.Graph()
        for nodo in self.grafo.nodos.values():
            grafo_networkx.add_node(nodo.nombre, ubicacion=nodo.ubicacion)
        for arista in self.grafo.aristas.values():
            grafo_networkx.add_edge(arista.nodo_1, arista.nodo_2, peso=arista.calcular_peso())
        posiciones = nx.get_node_attributes(grafo_networkx, 'ubicacion')
        pesos = nx.get_edge_attributes(grafo_networkx, 'peso')
        nx.draw(grafo_networkx, posiciones, with_labels=True, node_color='lightblue', node_size=2000)
        nx.draw_networkx_edge_labels(grafo_networkx, posiciones, edge_labels=pesos)
        plt.show()

    def actualizar_visualizacion(self):
        # Limpiar el gráfico antes de actualizar
        self.ax.clear()

        # Ejemplo: Dibujar nodos
        for nodo in self.grafo.nodos.values():
            self.ax.scatter(*nodo.ubicacion, label=nodo.nombre)

        # Ejemplo: Dibujar aristas
        for arista, ruta in self.grafo.aristas.items():
            nodo_1, nodo_2 = arista
            self.ax.plot([self.grafo.nodos[nodo_1].ubicacion[0], self.grafo.nodos[nodo_2].ubicacion[0]],
                         [self.grafo.nodos[nodo_1].ubicacion[1], self.grafo.nodos[nodo_2].ubicacion[1]], 'k-')

        # Configurar etiquetas, leyenda, etc.
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.legend()

        # Actualizar el lienzo
        self.canvas.draw()
     
class FormularioCrearNodo(tk.Frame):
    def __init__(self, grafo, master=None):
        super().__init__(master)
        self.grafo = grafo
        self.configure(bg='#E0E0E0')
        self.pack(fill="both", expand=True)

        tk.Label(self, text="Nombre del lugar:", bg='#E0E0E0').pack(pady=3)
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=3)

        tk.Label(self, text="Ubicación (x, y):", bg='#E0E0E0').pack(pady=3)
        self.ubicacion_entry = tk.Entry(self)
        self.ubicacion_entry.pack(pady=3)

        guardar_btn = tk.Button(self, text="Guardar", command=self.guardar, bg='green', fg='white')
        guardar_btn.pack(pady=5)

    def guardar(self):
        nombre = self.nombre_entry.get()
        ubicacion_str = self.ubicacion_entry.get()

        if not nombre or not ubicacion_str:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
        else:
            try:
                # Verificar si el nombre ya existe
                if nombre in self.grafo.nodos:
                    messagebox.showerror("Error", "Ya existe un lugar con ese nombre.")
                else:
                    ubicacion = tuple(map(float, ubicacion_str.split(',')))

                    # Verificar si las coordenadas ya existen en otro nodo
                    if any(nodo.ubicacion == ubicacion for nodo in self.grafo.nodos.values()):
                        messagebox.showerror("Error", "Ya existe un lugar en esa ubicación.")
                    else:
                        self.grafo.agregar_nodo(nombre, ubicacion)
                        messagebox.showinfo("Éxito", "Lugar creado exitosamente.")
                        self.destroy()
            except ValueError:
                messagebox.showerror("Error", "Ubicación inválida. Asegúrate de ingresar las coordenadas como números separados por coma.")

class FormularioBorrarNodo(tk.Frame):
    def __init__(self, grafo, master=None):
        super().__init__(master)
        self.grafo = grafo
        self.configure(bg='#E0E0E0')
        self.pack(fill="both", expand=True)

        tk.Label(self, text="Seleccione el lugar a borrar:", bg='#E0E0E0').pack(pady=5)

        # Combobox para mostrar los nodos disponibles
        self.nodos_combobox = ttk.Combobox(self, values=list(self.grafo.nodos.keys()))
        self.nodos_combobox.pack(pady=5)

        btn_agregar = tk.Button(self, text="Borrar Lugar", command=self.borrar_nodo, bg='green', fg='white')
        btn_agregar.pack(pady=10)

    def borrar_nodo(self):
        # Obtener el nombre del nodo seleccionado
        nombre = self.nodos_combobox.get()

        # Verificar si se seleccionó un nodo
        if not nombre:
            messagebox.showerror("Error", "Seleccione un lugar para borrar.")
            return

        self.grafo.borrar_nodo(nombre)
        messagebox.showinfo("Éxito", "Lugar borrado exitosamente.")
        self.destroy()
        
class FormularioCrearArista(tk.Frame):
    def __init__(self, grafo, master=None):
        super().__init__(master)
        self.grafo = grafo
        self.configure(bg='#E0E0E0')
        self.pack(fill="both", expand=True)

        # Combobox para lugar 1
        tk.Label(self, text="Seleccione el lugar 1:", bg='#E0E0E0').pack(pady=5)
        self.lugar_1_combobox = ttk.Combobox(self, values=list(self.grafo.nodos.keys()))
        self.lugar_1_combobox.pack(pady=5)

        # Combobox para lugar 2
        tk.Label(self, text="Seleccione el lugar 2:", bg='#E0E0E0').pack(pady=5)
        self.lugar_2_combobox = ttk.Combobox(self, values=list(self.grafo.nodos.keys()))
        self.lugar_2_combobox.pack(pady=5)

        # Entrada para costo
        tk.Label(self, text="Costo promedio (miles de pesos):", bg='#E0E0E0').pack(pady=5)
        self.costo_entry = tk.Entry(self)
        self.costo_entry.pack(pady=5)

        # Entrada para tiempo
        tk.Label(self, text="Tiempo promedio (horas):", bg='#E0E0E0').pack(pady=5)
        self.tiempo_entry = tk.Entry(self)
        self.tiempo_entry.pack(pady=5)

        # Entrada para distancia
        tk.Label(self, text="Distancia (kilometros):", bg='#E0E0E0').pack(pady=5)
        self.distancia_entry = tk.Entry(self)
        self.distancia_entry.pack(pady=5)

        # Botón para agregar ruta
        btn_agregar = tk.Button(self, text="Agregar Ruta", command=self.agregar_ruta, bg='green', fg='white')
        btn_agregar.pack(pady=10)

    def agregar_ruta(self):
        # Obtener los nombres de los lugares seleccionados
        lugar_1 = self.lugar_1_combobox.get()
        lugar_2 = self.lugar_2_combobox.get()

        # Verificar si se seleccionó un lugar para ambos nodos
        if not lugar_1 or not lugar_2:
            messagebox.showerror("Error", "Seleccione ambos lugares para crear la ruta.")
            return

        # Verificar que los lugares 1 y 2 no sean iguales
        if lugar_1 == lugar_2:
            messagebox.showerror("Error", "Los lugares 1 y 2 no pueden ser iguales.")
            return

        # Verificar que los campos de costo, tiempo y distancia sean numéricos
        try:
            costo = int(self.costo_entry.get())
            tiempo = int(self.tiempo_entry.get())
            distancia = int(self.distancia_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos en los campos de costo, tiempo y distancia.")
            return

        # Agregar la arista al grafo
        self.grafo.agregar_arista(lugar_1, lugar_2, costo, tiempo, distancia)
        messagebox.showinfo("Éxito", "Ruta creada exitosamente.")
        self.destroy()
        

class FormularioBorrarArista(tk.Frame):
    def __init__(self, grafo, master=None):
        super().__init__(master)
        self.grafo = grafo
        self.configure(bg='#E0E0E0')
        self.pack(fill="both", expand=True)

        # Combobox para lugar 1
        tk.Label(self, text="Seleccione el lugar 1:", bg='#E0E0E0').pack(pady=5)
        self.lugar_1_combobox = ttk.Combobox(self, values=list(self.grafo.nodos.keys()))
        self.lugar_1_combobox.pack(pady=5)

        # Combobox para lugar 2
        tk.Label(self, text="Seleccione el lugar 2:", bg='#E0E0E0').pack(pady=5)
        self.lugar_2_combobox = ttk.Combobox(self, values=list(self.grafo.nodos.keys()))
        self.lugar_2_combobox.pack(pady=5)

        # Botón para borrar ruta
        btn_agregar = tk.Button(self, text="Borrar Ruta", command=self.borrar_ruta, bg='green', fg='white')
        btn_agregar.pack(pady=10)

    def borrar_ruta(self):
        # Obtener los nombres de los lugares seleccionados
        lugar_1 = self.lugar_1_combobox.get()
        lugar_2 = self.lugar_2_combobox.get()

        # Verificar si se seleccionó un lugar para ambos nodos
        if not lugar_1 or not lugar_2:
            messagebox.showerror("Error", "Seleccione ambos lugares para borrar la ruta.")
            return

        # Verificar si la ruta existe antes de intentar borrarla
        if not self.grafo.existe_arista(lugar_1, lugar_2):
            messagebox.showerror("Error", "La ruta no existe.")
            return

        # Borrar la arista del grafo
        self.grafo.borrar_arista(lugar_1, lugar_2)
        messagebox.showinfo("Éxito", "Ruta borrada exitosamente.")
        self.destroy()
        
class FormularioFB(tk.Frame):
    def __init__(self, grafo, master=None):
        super().__init__(master)
        self.grafo = grafo
        self.configure(bg='#E0E0E0')
        self.pack(fill="both", expand=True)

        tk.Label(self, text="Nombre del almacen:", bg='#E0E0E0').pack(pady=5)
        self.lugar_combobox = ttk.Combobox(self, values=list(self.grafo.nodos.keys()))
        self.lugar_combobox.pack(pady=5)

        btn_agregar = tk.Button(self, text="Calcular", command=self.mostrar, bg='green', fg='white')
        btn_agregar.pack(pady=10)
        
    def mostrar(self):
        origen = self.lugar_combobox.get()
        if not origen:
            messagebox.showerror("Error", "Por favor, selecciona un lugar.")
        else:
            mejor_ruta = fb.fuerza_bruta(self.grafo, origen)
            
            # Verificar si la mejor ruta es None o un mensaje de error
            if mejor_ruta is None:
                messagebox.showinfo("Solución FB", "No hay rutas disponibles en el grafo. Esto se debe a que hay un nodo problema, por favor verifique que todos los nodos estén debidamente conectados o elimine el nodo problema.")
            else:
                solucion = ''
                for nodo in mejor_ruta:
                    solucion += nodo + '\n'
                messagebox.showinfo("Solución Fuerza Bruta", f"La mejor ruta es:\n\n{solucion}")
        self.destroy()
        
class FormularioVMC(tk.Frame):
    def __init__(self, grafo, master=None):
        super().__init__(master)
        self.grafo = grafo
        self.configure(bg='#E0E0E0')
        self.pack(fill="both", expand=True)

        tk.Label(self, text="Nombre del lugar:", bg='#E0E0E0').pack(pady=5)
        lugares = list(self.grafo.nodos.keys())
        self.nombre_combobox = ttk.Combobox(self, values=lugares)
        self.nombre_combobox.pack(pady=5)

        btn_agregar = tk.Button(self, text="Calcular", command=self.mostrar, bg='green', fg='white')
        btn_agregar.pack(pady=10)

    def mostrar(self):
        origen = self.nombre_combobox.get()
        if not origen:
            messagebox.showerror("Error", "Por favor, selecciona un lugar.")
        else:
            try:
                mejor_ruta = vmc.vecino_mas_cercano(self.grafo, origen)
                solucion = ''
                for nodo in mejor_ruta:
                    solucion += nodo + '\n'
                messagebox.showinfo("Solución Fuerza Bruta", f"La mejor ruta es:\n\n{solucion}")
            except KeyError:
                messagebox.showerror("Error", "No hay rutas disponibles en el grafo. Esto se debe a que hay un nodo problema, por favor verifique que todos los nodos estén debidamente conectados o elimine el nodo problema.")
        self.destroy()
                
if __name__ == "__main__":
    root = tk.Tk()
    app = Vista(root)
    root.mainloop()