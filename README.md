Proyecto Gestión de Hotel – Documentación de Desarrollo
1. Descripción del Proyecto

Este proyecto consiste en el desarrollo de un sistema en Python para la gestión básica de:

Clientes (Customer)

Hoteles (Hotel)

Reservaciones (Reservation)

El sistema utiliza archivos JSON como mecanismo de persistencia de datos mediante una clase auxiliar FileManager, simulando una base de datos ligera basada en archivos.

El objetivo principal fue aplicar buenas prácticas de ingeniería de software, incluyendo:

Programación orientada a objetos

Persistencia de datos

Pruebas unitarias

Control de calidad con herramientas estáticas

Control de versiones con Git

2. Estructura del Proyecto
project/
│
├── customer.py
├── hotel.py
├── reservation.py
├── file_manager.py
│
├── data/
│   ├── customers.json
│   ├── hotels.json
│   └── reservations.json
│
└── tests/
    ├── test_customer.py
    ├── test_hotel.py
    ├── test_reservation.py
    └── test_file_manager.py
3. Implementación Inicial

Se desarrollaron inicialmente las clases principales con funcionalidades básicas:

Customer

Crear cliente

Eliminar cliente

Mostrar cliente

Hotel

Crear hotel

Mostrar hotel

Reservar habitaciones

Control de disponibilidad

Reservation

Crear reservaciones

Consultar reservaciones

FileManager

Cargar datos desde archivos JSON

Guardar datos en archivos JSON

Manejo de errores de archivo
4. Evaluación Inicial de Calidad de Código

Antes de realizar las correcciones, se ejecutaron las herramientas de análisis estático:

Pylint (análisis de calidad y buenas prácticas)

Flake8 (validación de estilo PEP8)

Los resultados iniciales mostraron múltiples problemas estructurales y de estilo en todos los módulos del proyecto.

Resultados iniciales de Pylint
Archivo	Calificación inicial	Problemas principales
customer.py	0.00 / 10	Sin docstrings, indentación incorrecta, excepciones genéricas, líneas largas
hotel.py	≈0.3 / 10	Indentación incorrecta, imports mal posicionados, falta de documentación
reservation.py	≈1.1 / 10	Espaciado incorrecto, docstrings faltantes, estructura no PEP8
file_manager.py	<5 / 10	Manejo incompleto de errores y estilo inconsistente
tests/test_customer.py	0.00 / 10	Imports incorrectos, indentación inválida, falta de docstrings
tests/test_hotel.py	0.38 / 10	Indentación incorrecta y documentación faltante
tests/test_reservation.py	1.14 / 10	Violaciones extensivas de PEP8
tests/test_file_manager.py	Inicialmente inexistente	No había pruebas para persistencia
Tipos de errores detectados

Los errores más comunes reportados por Pylint y Flake8 fueron:

1. Indentación incorrecta
Bad indentation. Found 1 spaces, expected 4
2. Falta de documentación
missing-module-docstring
missing-class-docstring
missing-function-docstring
3. Importaciones mal ubicadas
wrong-import-position
module level import not at top
4. Violaciones PEP8

Espacios faltantes alrededor de operadores

Líneas mayores a 79 caracteres

Separación incorrecta entre funciones

5. Problemas en pruebas unitarias

Uso incorrecto de assertTrue(True)

Tests mal estructurados

Módulos no detectados por Python

8. Evaluación Final de Calidad

Después del proceso completo de refactorización y corrección:

Resultados finales de Pylint
Archivo	Calificación final
customer.py	10.00 / 10
hotel.py	10.00 / 10
reservation.py	10.00 / 10
file_manager.py	10.00 / 10
tests/test_customer.py	10.00 / 10
tests/test_hotel.py	10.00 / 10
tests/test_reservation.py	10.00 / 10
tests/test_file_manager.py	10.00 / 10
Resultados Flake8 (Final)
No style violations detected

Todos los archivos cumplen completamente con el estándar PEP8.

9. Mejora de Calidad del Código (Comparación)
Archivo	Inicial	Final	Mejora
customer.py	0.00	10.00	+10.00
hotel.py	0.38	10.00	+9.62
reservation.py	1.14	10.00	+8.86
tests/test_customer.py	0.00	10.00	+10.00
tests/test_hotel.py	0.38	10.00	+9.62
tests/test_reservation.py	1.14	10.00	+8.86
