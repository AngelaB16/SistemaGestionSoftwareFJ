# Vista de Clientes

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from modelos.cliente import Cliente

class VistaClientes:

    def __init__(self, frame, sistema):
        self.sistema = sistema
        self.frame = frame

        # Titulo 

        titulo = tk.Label(
            frame,
            text="GESTIÓN DE CLIENTES",
            font=("Arial", 16, "bold")
        )

        titulo.pack(pady=15)

        # Formulario 

        formulario = tk.LabelFrame(
            frame,
            text="Datos del Cliente",
            padx=15,
            pady=15
        )

        formulario.pack(fill="x", padx=20)

        # Codigo

        tk.Label(formulario, text="Código").grid(row=0, column=0, sticky="w")

        self.codigo = tk.Entry(formulario, width=30)

        self.codigo.grid(row=0, column=1, padx=10, pady=5)

        # Nombre

        tk.Label(formulario, text="Nombre").grid(row=1, column=0, sticky="w")

        self.nombre = tk.Entry(formulario, width=30)

        self.nombre.grid(row=1, column=1, padx=10, pady=5)

        # Documento

        tk.Label(formulario, text="Documento").grid(row=2, column=0, sticky="w")

        self.documento = tk.Entry(formulario, width=30)

        self.documento.grid(row=2, column=1, padx=10, pady=5)

        # Telefono

        tk.Label(formulario, text="Teléfono").grid(row=3, column=0, sticky="w")

        self.telefono = tk.Entry(formulario, width=30)

        self.telefono.grid(row=3, column=1, padx=10, pady=5)

        # Correo

        tk.Label(formulario, text="Correo").grid(row=4, column=0, sticky="w")

        self.correo = tk.Entry(formulario, width=30)

        self.correo.grid(row=4, column=1, padx=10, pady=5)

        # Botones

        botones = tk.Frame(frame)
        botones.pack(pady=10)

        self.btn_registrar = tk.Button(
            botones,
            text="Registrar",
            width=15,
            command=self.registrar_cliente
        )
        self.btn_registrar.grid(row=0, column=0, padx=5)

        self.btn_modificar = tk.Button(
            botones,
            text="Modificar",
            width=15,
            command=self.modificar_cliente
        )
        self.btn_modificar.grid(row=0, column=1, padx=5)

        self.btn_eliminar = tk.Button(
            botones,
            text="Eliminar",
            width=15,
            command=self.eliminar_cliente
        )
        self.btn_eliminar.grid(row=0, column=2, padx=5)

        self.btn_limpiar = tk.Button(
            botones,
            text="Limpiar",
            width=15,
            command=self.limpiar
        )
        self.btn_limpiar.grid(row=0, column=3, padx=5)

        # Tabla 

        columnas = (
            "codigo",
            "nombre",
            "documento",
            "telefono",
            "correo"
        )

        self.tabla = ttk.Treeview(
            frame,
            columns=columnas,
            show="headings",
            height=10
        )

        self.tabla.heading("codigo", text="Código")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("documento", text="Documento")
        self.tabla.heading("telefono", text="Teléfono")
        self.tabla.heading("correo", text="Correo")

        self.tabla.pack(fill="both", expand=True, padx=20, pady=15)

        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_cliente)

    def obtener_datos(self):
        """Obtiene la información escrita en el formulario."""

        return {
            "codigo": self.codigo.get(),
            "nombre": self.nombre.get(),
            "documento": self.documento.get(),
            "telefono": self.telefono.get(),
            "correo": self.correo.get()
        }
    
    def registrar_cliente(self):

        try:

            datos = self.obtener_datos()

            cliente = Cliente(
                datos["codigo"],
                datos["nombre"],
                datos["documento"],
                datos["telefono"],
                datos["correo"]
            )

            self.sistema.agregar_cliente(cliente)

            self.tabla.insert(
                "",
                "end",
                values=(
                    cliente.codigo,
                    cliente.nombre,
                    cliente.documento,
                    cliente.telefono,
                    cliente.correo
                )
            )

            messagebox.showinfo(
                "Éxito",
                "Cliente registrado correctamente."
            )

            self.limpiar()

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    def limpiar(self):
        """Limpia el formulario."""

        self.codigo.delete(0, tk.END)
        self.nombre.delete(0, tk.END)
        self.documento.delete(0, tk.END)
        self.telefono.delete(0, tk.END)
        self.correo.delete(0, tk.END)

    def seleccionar_cliente(self, event):

        seleccion = self.tabla.focus()

        if not seleccion:
            return

        datos = self.tabla.item(seleccion)["values"]

        self.limpiar()

        self.codigo.insert(0, datos[0])
        self.nombre.insert(0, datos[1])
        self.documento.insert(0, datos[2])
        self.telefono.insert(0, datos[3])
        self.correo.insert(0, datos[4])


    def modificar_cliente(self):

        seleccion = self.tabla.focus()

        if not seleccion:
            messagebox.showwarning(
                "Advertencia",
                "Seleccione un cliente."
            )
            return

        datos_tabla = self.tabla.item(seleccion)["values"]

        documento_original = datos_tabla[2]

        datos = self.obtener_datos()

        try:

            self.sistema.modificar_cliente(
                documento_original,
                datos
            )

            self.tabla.item(
                seleccion,
                values=(
                    datos["codigo"],
                    datos["nombre"],
                    datos["documento"],
                    datos["telefono"],
                    datos["correo"]
                )
            )

            messagebox.showinfo(
                "Éxito",
                "Cliente modificado correctamente."
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    def eliminar_cliente(self):

        seleccion = self.tabla.focus()

        if not seleccion:
            messagebox.showwarning(
                "Advertencia",
                "Seleccione un cliente."
            )
            return

        datos = self.tabla.item(seleccion)["values"]

        documento = datos[2]

        try:

            self.sistema.eliminar_cliente(documento)

            self.tabla.delete(seleccion)

            messagebox.showinfo(
                "Éxito",
                "Cliente eliminado correctamente."
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )