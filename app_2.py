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
    system_instruction="""Eres un Editor de una Editorial de prestigio. 
Tus respuestas deben ser concisas, teniendo presente que eres un Editor de una Editorial de prestigio.

Si la tarea es "resumir", debe devolver un resumen ejecutivo.
Si la tarea es "profesionalizar", debe editar el texto para que suene formal y técnico.
Si te hacen una pregunta que no está realicionada con temas de la editorial, hacer resumenes o editar el texto para que suene formal y técnico, responde 'Lo siento, solo puedo responder preguntas relacionadas con temas relacionados a la editorial.'"""
)

# Inicialización del chat
chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config=configuration
)

# INCORPORACIÓN DE LA FUNCIÓN SOLICITADA 
def procesar_articulo(texto, tarea):
    prompt = f"Realiza la siguiente tarea: '{tarea}'.\n\nTexto: {texto}"
    
    response = chat.send_message(prompt)
    return response.text


print("-- Editorial JABA  --")
print("(Escribe 'salir' para terminar)\n")

while True:
        tarea_input = input("Usuario (Tarea: 'resumir' o 'profesionalizar'): ")
        
        if tarea_input.lower() in ["salir", "exit", "quit"]:
            print("Asistente: ¡Hasta pronto! Sigue practicando.")
            break
            
        texto_input = input("Usuario (Texto a procesar): ")

        try:
            # 3. Envío del mensaje a través de la función requerida            
            resultado = procesar_articulo(texto_input, tarea_input)
            
            # En el nuevo SDK, el acceso al texto es response.text (ya manejado en la función)
            print(f"\nAsistente: {resultado}\n")

        except Exception as e:
            # Es recomendable implementar reintentos con backoff exponencial en producción
            print(f"Error al procesar la solicitud: {e}")