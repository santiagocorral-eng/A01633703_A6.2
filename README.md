6.2 Ejercicio de programación 3 y pruebas de unidad
1. Descripción de la Actividad

Este proyecto consiste en un sistema en Python para la gestión de:

Clientes (Customer)

Hoteles (Hotel)

Reservaciones (Reservation)

El sistema utiliza archivos JSON como persistencia de datos mediante la clase FileManager, simulando una base de datos ligera basada en archivos.

Objetivos principales:

Aplicar programación orientada a objetos

Implementar persistencia de datos en JSON

Realizar pruebas unitarias completas

Mantener calidad de código con herramientas estáticas

Control de versiones mediante Git

2. Estructura del Proyecto
project/
├── customer.py
├── hotel.py
├── reservation.py
├── file_manager.py
├── main.py
├── data/
│   ├── customers.json
│   ├── hotels.json
│   └── reservations.json
├── tests/
│   ├── test_customer.py
│   ├── test_hotel.py
│   ├── test_reservation.py
│   └── test_file_manager.py
├── logs/
│   └── *.log  (registros de pylint y flake8)
└── README.md
3. Implementación Inicial

Clases principales y funcionalidades

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

Se ejecutaron herramientas de análisis estático:

Pylint: calidad y buenas prácticas

Flake8: cumplimiento de PEP8

Resultados iniciales de Pylint

Archivo	Calificación inicial	Problemas principales
customer.py	0.00 / 10	Sin docstrings, indentación incorrecta, excepciones genéricas, líneas largas
hotel.py	0.38 / 10	Indentación incorrecta, imports mal posicionados, falta de documentación
reservation.py	1.14 / 10	Espaciado incorrecto, docstrings faltantes, estructura no PEP8
file_manager.py	<5 / 10	Manejo incompleto de errores, estilo inconsistente
tests/test_customer.py	0.00 / 10	Imports incorrectos, indentación inválida, falta de docstrings
tests/test_hotel.py	0.38 / 10	Indentación incorrecta, documentación faltante
tests/test_reservation.py	1.14 / 10	Violaciones extensivas de PEP8
tests/test_file_manager.py	Inexistente	No había pruebas para persistencia

Errores más comunes:

Indentación incorrecta

Falta de documentación en módulos, clases y métodos

Imports mal ubicados

Violaciones de PEP8

Líneas >79 caracteres

Uso incorrecto de assertTrue(True) en tests

5. Correcciones Aplicadas

Ajuste de indentación a 4 espacios por nivel

Adición de docstrings en módulos, clases y métodos

Reubicación de importaciones al inicio de los archivos

Aplicación de @staticmethod a métodos que no requieren instancia

Ajuste de líneas largas (>79 caracteres)

Refactorización de pruebas unitarias

Organización de archivos de logs en logs/

6. Evaluación Final de Calidad

Resultados finales de Pylint y Flake8

Archivo	Pylint Final	Mejora	Flake8
customer.py	10.00 / 10	+10.00	0 errores
hotel.py	10.00 / 10	+9.62	0 errores
reservation.py	10.00 / 10	+8.86	0 errores
file_manager.py	10.00 / 10	+10.00	0 errores
tests/test_customer.py	10.00 / 10	+10.00	0 errores
tests/test_hotel.py	10.00 / 10	+9.62	0 errores
tests/test_reservation.py	10.00 / 10	+8.86	0 errores
tests/test_file_manager.py	10.00 / 10	n/a	0 errores

Todos los archivos cumplen 100% con PEP8 y las pruebas unitarias corren correctamente.

7. Cobertura de Pruebas y Casos Negativos

Diseño de Casos de Prueba – Programa 1 (30 pts)

Clase	Casos Negativos Incluidos	Registro en Git	Comentario
Customer	Crear cliente con datos inválidos, eliminar cliente inexistente, mostrar cliente no registrado	Más de 5 escenarios negativos
Hotel	Reservar más habitaciones de las disponibles, crear hotel con datos faltantes, mostrar hotel inexistente	Escenarios negativos manejados correctamente
Reservation	Crear reserva para cliente inexistente, duplicar reserva, eliminar reserva inexistente		Todos los errores capturados y testeados
FileManager	Cargar archivo inexistente, cargar archivo con JSON corrupto, guardar datos inválidos	
Manejo de errores verificado

Cobertura de Líneas – Programa 1 (30 pts)

Todas las funciones de cada clase (Customer, Hotel, Reservation, FileManager) están cubiertas por pruebas unitarias

Cobertura de líneas: >85%

Incluye escenarios positivos y negativos

Todos los cambios tienen commits claros en Git

Cumple con el requisito de cobertura de líneas y casos negativos.

8. Control de Versiones

Todos los cambios versionados con Git

Commits claros y temáticos, por ejemplo:

docs: add final README.md

chore: final corrections, add tests and organize logs

test(project): add and fix unit tests achieving pylint 10/10

9. Conclusión

Proyecto completamente refactorizado

Calidad de código máxima (Pylint 10/10 y Flake8 0 errores)

Pruebas unitarias completas, cobertura >85%, manejo de casos negativos

Estructura de proyecto organizada y documentada
