import tkinter as tk
from tkinter import ttk, messagebox

from modelos.reserva_sala import ReservaSala
from modelos.alquiler_equipo import AlquilerEquipo
from modelos.asesoria import Asesoria

class VistaServicios:

    def __init__(self, frame, sistema):

        self.sistema = sistema
        self.frame = frame


        # Título

        titulo = tk.Label(
            frame,
            text="GESTIÓN DE SERVICIOS",
            font=("Arial", 16, "bold")
        )

        titulo.pack(pady=15)


        # Formulario

        formulario = tk.LabelFrame(
            frame,
            text="Datos del Servicio",
            padx=15,
            pady=15
        )

        formulario.pack(
            fill="x",
            padx=20
        )


        # Código

        tk.Label(
            formulario,
            text="Código"
        ).grid(row=0, column=0, sticky="w")

        self.codigo = tk.Entry(
            formulario,
            width=30
        )

        self.codigo.grid(
            row=0,
            column=1,
            padx=10,
            pady=5
        )


        # Nombre

        tk.Label(
            formulario,
            text="Nombre"
        ).grid(row=1, column=0, sticky="w")

        self.nombre = tk.Entry(
            formulario,
            width=30
        )

        self.nombre.grid(
            row=1,
            column=1,
            padx=10,
            pady=5
        )


        # Costo base

        tk.Label(
            formulario,
            text="Costo base"
        ).grid(row=2, column=0, sticky="w")

        self.costo_base = tk.Entry(
            formulario,
            width=30
        )

        self.costo_base.grid(
            row=2,
            column=1,
            padx=10,
            pady=5
        )


        # Tipo de servicio

        tk.Label(
            formulario,
            text="Tipo de servicio"
        ).grid(row=3, column=0, sticky="w")


        self.tipo = ttk.Combobox(
            formulario,
            values=[
                "Reserva Sala",
                "Alquiler Equipo",
                "Asesoria"
            ],
            state="readonly",
            width=27
        )

        self.tipo.grid(
            row=3,
            column=1,
            padx=10,
            pady=5
        )


        # Campo adicional

        tk.Label(
            formulario,
            text="Cantidad"
        ).grid(row=4, column=0, sticky="w")


        self.cantidad = tk.Entry(
            formulario,
            width=30
        )

        self.cantidad.grid(
            row=4,
            column=1,
            padx=10,
            pady=5
        )


        # Botones

        botones = tk.Frame(frame)

        botones.pack(pady=10)


        self.btn_registrar = tk.Button(
            botones,
            text="Registrar",
            width=15,
            command=self.registrar_servicio
        )

        self.btn_registrar.grid(
            row=0,
            column=0,
            padx=5
        )


        self.btn_limpiar = tk.Button(
            botones,
            text="Limpiar",
            width=15,
            command=self.limpiar
        )

        self.btn_limpiar.grid(
            row=0,
            column=1,
            padx=5
        )

        self.btn_eliminar = tk.Button(
            botones,
            text="Eliminar",
            width=15,
            command=self.eliminar_servicio
        )

        self.btn_eliminar.grid(
            row=0,
            column=2,
            padx=5
        )

        # Tabla

        columnas = (
            "codigo",
            "nombre",
            "tipo",
            "costo"
        )


        self.tabla = ttk.Treeview(
            frame,
            columns=columnas,
            show="headings",
            height=10
        )


        self.tabla.heading(
            "codigo",
            text="Código"
        )

        self.tabla.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla.heading(
            "tipo",
            text="Tipo"
        )

        self.tabla.heading(
            "costo",
            text="Costo"
        )


        self.tabla.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        self.tabla.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_servicio
        )

    # Obtiene datos del formulario

    def obtener_datos(self):

        return {
            "codigo": self.codigo.get(),
            "nombre": self.nombre.get(),
            "costo_base": float(self.costo_base.get()),
            "tipo": self.tipo.get(),
            "cantidad": int(self.cantidad.get())
        }


    # Crea el objeto según el tipo seleccionado

    def crear_servicio(self, datos):

        if datos["tipo"] == "Reserva Sala":

            return ReservaSala(
                datos["codigo"],
                datos["nombre"],
                datos["costo_base"],
                datos["cantidad"]
            )


        elif datos["tipo"] == "Alquiler Equipo":

            return AlquilerEquipo(
                datos["codigo"],
                datos["nombre"],
                datos["costo_base"],
                datos["cantidad"]
            )


        elif datos["tipo"] == "Asesoria":

            return Asesoria(
                datos["codigo"],
                datos["nombre"],
                datos["costo_base"],
                datos["cantidad"]
            )


        else:

            raise ValueError(
                "Debe seleccionar un tipo de servicio."
            )


    # Registrar servicio

    def registrar_servicio(self):

        try:

            datos = self.obtener_datos()
            servicio = self.crear_servicio(datos)

            self.sistema.agregar_servicio(
                servicio
            )


            self.tabla.insert(
                "",
                "end",
                values=(
                    servicio.codigo,
                    servicio.nombre,
                    datos["tipo"],
                    servicio.calcular_costo()
                )
            )


            messagebox.showinfo(
                "Éxito",
                "Servicio registrado correctamente."
            )


            self.limpiar()


        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # Limpia formulario

    def limpiar(self):

        self.codigo.delete(
            0,
            tk.END
        )

        self.nombre.delete(
            0,
            tk.END
        )

        self.costo_base.delete(
            0,
            tk.END
        )

        self.cantidad.delete(
            0,
            tk.END
        )

        self.tipo.set("")


    def seleccionar_servicio(self, event):

        seleccion = self.tabla.focus()

        if not seleccion:
            return


        datos = self.tabla.item(seleccion)["values"]


        self.codigo.delete(0, tk.END)
        self.nombre.delete(0, tk.END)
        self.costo_base.delete(0, tk.END)


        self.codigo.insert(0, datos[0])
        self.nombre.insert(0, datos[1])

    def eliminar_servicio(self):

        seleccion = self.tabla.focus()


        if not seleccion:

            messagebox.showwarning(
                "Advertencia",
                "Seleccione un servicio."
            )

            return


        datos = self.tabla.item(seleccion)["values"]


        codigo = datos[0]


        try:

            self.sistema.eliminar_servicio(codigo)


            self.tabla.delete(seleccion)


            messagebox.showinfo(
                "Éxito",
                "Servicio eliminado correctamente."
            )


        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )