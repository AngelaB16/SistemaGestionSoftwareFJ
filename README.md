# Sistema Integral de Gestión - Software FJ

## Descripción

Este proyecto consiste en el desarrollo de un Sistema Integral de Gestión para la empresa **Software FJ**, implementado en Python bajo el paradigma de Programación Orientada a Objetos (POO).

El sistema permite administrar clientes, servicios y reservas mediante una interfaz gráfica desarrollada con Tkinter, sin utilizar bases de datos, almacenando la información en memoria durante la ejecución.

---

## Funcionalidades

- Gestión de clientes
  - Registrar clientes
  - Modificar clientes
  - Eliminar clientes

- Gestión de servicios
  - Reserva de salas
  - Alquiler de equipos
  - Asesorías especializadas
  - Registro, modificación y eliminación

- Gestión de reservas
  - Registrar reservas
  - Confirmar reservas
  - Cancelar reservas
  - Eliminar reservas

- Reportes
  - Total de clientes
  - Total de servicios
  - Total de reservas
  - Estado de las reservas
  - Ingresos estimados

- Registro de eventos mediante Logger.

- Manejo de excepciones personalizadas.

---

## Tecnologías utilizadas

- Python 3
- Tkinter
- Programación Orientada a Objetos
- Git
- GitHub

---

## Principios de Programación Orientada a Objetos aplicados

- Abstracción
- Encapsulamiento
- Herencia
- Polimorfismo

---

## Estructura del proyecto

```
SistemaGestionSoftwareFJ
│
├── main.py
├── interfaz.py
├── sistema.py
├── excepciones.py
├── logger_config.py
├── README.md
│
├── modelos
│   ├── entidad.py
│   ├── cliente.py
│   ├── servicio.py
│   ├── reserva.py
│   ├── reserva_sala.py
│   ├── alquiler_equipo.py
│   └── asesoria.py
│
├── vistas
│   ├── clientes.py
│   ├── servicios.py
│   ├── reservas.py
│   └── reportes.py
│
└── logs

