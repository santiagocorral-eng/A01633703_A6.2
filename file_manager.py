"""Módulo FileManager.

Gestiona la lectura y escritura de archivos JSON
con manejo de errores.
"""

import json
import os


class FileManager:
    """Clase encargada de la persistencia de datos en archivos JSON."""

    @staticmethod
    def load_data(file_path):
        """
        Carga datos desde un archivo JSON.

        Args:
            file_path (str): Ruta del archivo.

        Returns:
            list: Datos cargados o lista vacía si ocurre un error.
        """
        if not os.path.exists(file_path):
            return []

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)

        except json.JSONDecodeError:
            print(f"Error: formato JSON inválido en {file_path}")
            return []

        except OSError as error:
            print(f"Error de lectura/escritura: {error}")
            return []

    @staticmethod
    def save_data(file_path, data):
        """
        Guarda datos en un archivo JSON.

        Args:
            file_path (str): Ruta del archivo.
            data (list): Datos a guardar.
        """
        try:
            # Crear carpeta si no existe (clave para tests)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

        except OSError as error:
            print(f"Error de escritura: {error}")
