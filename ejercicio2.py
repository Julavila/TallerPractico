"""
Ejercicio 2: Procesador de Textos Inteligente
Restringido únicamente a tareas editoriales.
"""

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Cargar API Key
load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")


client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-2.5-flash"


def procesar_articulo(texto: str, tarea: str) -> str:
    """
    Procesa un texto únicamente si la tarea es editorial.
    """

    configuration = types.GenerateContentConfig(

        system_instruction="""
        Eres un Editor Editorial de prestigio.
        Solo realizas tareas editoriales como:
        resumir, traducir, mejorar redacción, profesionalizar,
        corregir estilo, adaptar tono o estructurar contenido.

        Si la solicitud no corresponde a una tarea editorial,
        responde exactamente:
        'Lo siento, solo puedo realizar tareas editoriales sobre textos proporcionados.'
        """,

        max_output_tokens=5000,
        temperature=0.5
    )

    prompt = f"""
    Tarea solicitada: {tarea}

    Texto:
    {texto}
    """

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=configuration
        )

        return response.text

    except Exception as e:
        return f"Error procesando el texto: {e}"


if __name__ == "__main__":

    texto_usuario = input("Ingrese el texto:\n")
    tarea_usuario = input("\n¿Qué desea hacer con el texto? (Ej: resumir, traducir al inglés, mejorar redacción, etc.):\n")

    resultado = procesar_articulo(texto_usuario, tarea_usuario)

    print("\n--- RESULTADO ---\n")
    print(resultado)
