"""
Ejercicio 1: Conexión y Petición Básica
Explica qué es la Inferencia en IA en menos de 50 palabras.
"""

import os
from google.genai import types
from google import genai
from dotenv import load_dotenv
 
# 1. Cargar configuración de variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")
 
# 2. Inicializar el Cliente
# Este cliente gestiona la conexión
client = genai.Client(api_key=clave_api)
 
MODEL_NAME = "gemini-2.5-flash"


def explicar_inferencia():

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents="Explica qué es la Inferencia en IA en menos de 50 palabras.",
            config=types.GenerateContentConfig(
                max_output_tokens=500,  # suficiente para ~50 palabras
                temperature=0.3        
            )
        )

        print("\nRespuesta del modelo:\n")
        print(response.text)

    except Exception as e:
        print(f"Error al conectar con la API: {e}")


if __name__ == "__main__":
    explicar_inferencia()