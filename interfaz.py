# Librerias de Tkinter
import tkinter as tk
from tkinter import messagebox

# Clases del proyecto
from modelos.cliente import Cliente

# Registro de logs
from logger_config import registrar_evento, registrar_error


# Lista donde se almacenan los clientes
clientes = []


# Registrar cliente
def registrar_cliente():

    try:

        cliente = Cliente(
            txt_codigo.get(),
            txt_nombre.get(),
            txt_documento.get(),
            txt_telefono.get(),
            txt_correo.get()
        )

        clientes.append(cliente)

    except Exception as error:

        registrar_error(str(error))

        messagebox.showerror(
            "Error",
            str(error)
        )

    else:

        registrar_evento(
            f"Cliente registrado: {cliente.nombre}"
        )

        messagebox.showinfo(
            "Éxito",
            "Cliente registrado correctamente."
        )

        limpiar()

    finally:

        actualizar_lista()


# Mostrar clientes
def actualizar_lista():

    lista.delete(0, tk.END)

    for cliente in clientes:

        lista.insert(
            tk.END,
            f"{cliente.codigo} - {cliente.nombre}"
        )


# Limpiar cajas
def limpiar():

    txt_codigo.delete(0, tk.END)
    txt_nombre.delete(0, tk.END)
    txt_documento.delete(0, tk.END)
    txt_telefono.delete(0, tk.END)
    txt_correo.delete(0, tk.END)


# Ventana principal

ventana = tk.Tk()

ventana.title("Sistema Gestión Software FJ")

ventana.geometry("700x500")

ventana.resizable(False, False)

# Codigo

tk.Label(ventana, text="Código").pack()

txt_codigo = tk.Entry(ventana)

txt_codigo.pack()

# Nombre

tk.Label(ventana, text="Nombre").pack()

txt_nombre = tk.Entry(ventana)

txt_nombre.pack()

# Documento

tk.Label(ventana, text="Documento").pack()

txt_documento = tk.Entry(ventana)

txt_documento.pack()

# Telefono

tk.Label(ventana, text="Teléfono").pack()

txt_telefono = tk.Entry(ventana)

txt_telefono.pack()

# Correo

tk.Label(ventana, text="Correo").pack()

txt_correo = tk.Entry(ventana)

txt_correo.pack()

# Boton

tk.Button(
    ventana,
    text="Registrar Cliente",
    command=registrar_cliente
).pack(pady=10)

# Lista

lista = tk.Listbox(
    ventana,
    width=70,
    height=10
)

lista.pack()

ventana.mainloop()