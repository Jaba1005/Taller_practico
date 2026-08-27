import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv("GENAI_API_KEY")

# Inicializar el cliente
client = genai.Client(api_key=API_KEY)

configuration = types.GenerateContentConfig(
    max_output_tokens=2048,
    temperature=0,
    system_instruction="""Eres un vendedor amable. 
Tus respuestas deben ser concisas, seguras teniendo presente que el usuario es una cliente que desea comprar un producto.
Al responder sobre algun producto, debes incluir información sobre el precio, la disponibilidad y las características principales del producto.
Si te hacen una pregunta que no está realicionada con informacion sobre algun producto, responde 'Lo siento, solo puedo responder preguntas sobre productos'. """
)

MODEL = "gemini-3.5-flash-lite"

# Historial para simular la memoria del agente durante esta ejecución.
conversation_history = [
    {
        "role": "user",
        "parts": [{"text": "¿Tienen alguna laptop buena para jugar?"}]
    },
    {
        "role": "model",
        "parts": [{"text": "¡Hola! Claro que sí. Te recomiendo la ASUS TUF Gaming FX505DT. Tiene pantalla de 144Hz, procesador Ryzen y gráficos GTX. Su precio es de $850 y la tenemos disponible para entrega inmediata. ¿Te gustaría llevarla?"}]
    },
    {
        "role": "user",
        "parts": [{"text": "¿Venden controles por Bluetooth para celular?"}]
    },
    {
        "role": "model",
        "parts": [{"text": "¡Por supuesto! Tenemos el control GameSir X2 Bluetooth. Cuenta con botones mecánicos, batería de larga duración y es compatible con Android e iOS. Cuesta $60 y tenemos unidades disponibles en bodega."}]
    }
]

print("-- Consulta de productos JABA  --")
print("(Escribe 'salir' para terminar)\n")

while True:
        user_input = input("Cliente: ")
        
        if user_input.lower() in ["salir", "exit", "quit"]:
            print("Asistente: ¡Hasta pronto! Sigue practicando.")
            break

        try:
            conversation_history.append({
                "role": "user",
                "parts": [{"text": user_input}]
            })

            response = client.models.generate_content(
                model=MODEL,
                contents=conversation_history,
                config=configuration
            )
            
            assistant_message = response.text
            conversation_history.append({
                "role": "model",
                "parts": [{"text": assistant_message}]
            })

            print(f"\nAsistente: {assistant_message}\n")

        except Exception as e:            
            print(f"Error al procesar la solicitud: {e}")

