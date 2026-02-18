"""
Ejercicio 3: Chat de soporte con restricción temática.
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


def iniciar_chat():

    configuration = types.GenerateContentConfig(

        system_instruction="""
        Eres un vendedor amable y experto en una tienda de tecnología.

        Solo respondes preguntas relacionadas con:
        productos tecnológicos, especificaciones técnicas,
        recomendaciones de compra y precios aproximados.

        Si el usuario pregunta algo fuera del ámbito tecnológico,
        responde exactamente:
        'Lo siento, solo puedo ayudar con consultas relacionadas con productos tecnológicos.'
        """,

        max_output_tokens=1024,
        temperature=0.6
    )

    history = [

        types.Content(
            role="user",
            parts=[types.Part(text="¿Qué características tiene el iPhone 15?")]
        ),

        types.Content(
            role="model",
            parts=[types.Part(text="""
            El iPhone 15 incluye chip A16 Bionic, pantalla OLED de 6.1 pulgadas
            y cámara de 48 MP. Es ideal para alto rendimiento y fotografía.
            """)]
        ),

        types.Content(
            role="user",
            parts=[types.Part(text="¿Qué laptop recomiendas para programación?")]
        ),

        types.Content(
            role="model",
            parts=[types.Part(text="""
            Recomiendo laptops con 16GB RAM, SSD 512GB y procesador i7 o Ryzen 7.
            Son ideales para desarrollo profesional.
            """)]
        )
    ]

    chat = client.chats.create(
        model=MODEL_NAME,
        config=configuration,
        history=history
    )

    print("\n--- CHAT TIENDA TECNOLÓGICA ---")
    print("Escribe 'finalizar' para salir.\n")

    while True:

        user_input = input("Cliente: ")

        if user_input.lower() == "finalizar":
            print("Vendedor: ¡Gracias por visitarnos!")
            break

        try:
            response = chat.send_message(user_input)
            print(f"\nVendedor: {response.text}\n")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    iniciar_chat()
