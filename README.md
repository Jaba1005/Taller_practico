Este repositorio contiene 3 ejercicios prácticos que muestran distintas formas de construir un chatbot con la librería google-genai (Gemini): un asistente de estudio, un editor de textos y un vendedor con memoria de conversación.

📁 Estructura del repositorio
Taller_practico/
|── .env       #clave de gemini
├── app_1.py   # Ejercicio 1: Chat de estudio de IA
├── app_2.py   # Ejercicio 2: Editorial (resumir / profesionalizar texto)
├── app_3.py   # Ejercicio 3: Vendedor con historial de conversación
└── README.md
✅ Requisitos previos
Python instalado.
Una cuenta de Google AI Studio con una API Key de Gemini. Puedes generarla en: https://aistudio.google.com/apikey

⚙️ Instalación paso a paso
1. Clonar el repositorio
bash
git clone https://github.com/Jaba1005/Taller_practico.git
cd Taller_practico
2. Crear y activar un entorno virtual (recomendado)
bash
python -m venv env

# En Windows
env\Scripts\activate

3. Instalar las dependencias

Este proyecto usa dos librerías principales: google-genai (SDK de Gemini) y python-dotenv (para leer variables de entorno). Instálalas con:

bash
pip install google-genai python-dotenv
4. Configurar la API Key

Crea un archivo llamado .env en la raíz del proyecto (mismo nivel que app_1.py) con el siguiente contenido:

GENAI_API_KEY=tu_api_key_aqui


🧪 Ejercicio 1 — Chat de estudio de IA (app_1.py)

¿Qué hace? Crea un asistente conversacional especializado en Inteligencia Artificial. Responde de forma concisa y educativa, orientado a un estudiante de Ingeniería de Sistemas, y rechaza preguntas fuera del tema de IA. Si la pregunta es sobre "Inferencia en IA", responde en menos de 50 palabras.

Cómo ejecutarlo:

bash
python app_1.py

Cómo usarlo:

Escribe tu pregunta relacionada con IA cuando el programa te lo pida (Estudiante: ).
El asistente responderá en la consola.
Escribe salir, exit o quit para terminar la conversación.

<img width="1310" height="966" alt="image" src="https://github.com/user-attachments/assets/c45a6800-f475-47f1-859d-7803a5b127e7" />

🧪 Ejercicio 2 — Editorial JABA (app_2.py)

¿Qué hace? Simula un editor de una editorial que puede realizar dos tareas sobre un texto que le entregues: resumir (genera un resumen ejecutivo) o profesionalizar (reescribe el texto en tono formal y técnico). Cualquier otra solicitud fuera de estas tareas es rechazada.

Cómo ejecutarlo:

bash
python app_2.py

Cómo usarlo:

Cuando el programa pregunte Usuario (Tarea: 'resumir' o 'profesionalizar'), escribe una de esas dos palabras.
Cuando pregunte Usuario (Texto a procesar), pega o escribe el texto que quieres resumir o profesionalizar.
El asistente mostrará el resultado en consola.
Escribe salir, exit o quit para terminar.

<img width="1326" height="970" alt="image" src="https://github.com/user-attachments/assets/563f7598-991b-4d1c-9d87-c68b443b24a8" />

🧪 Ejercicio 3 — Consulta de productos JABA (app_3.py)

¿Qué hace? Simula un vendedor amable que responde preguntas sobre productos (precio, disponibilidad y características). A diferencia de los ejercicios anteriores, este mantiene manualmente un historial de conversación (conversation_history) que incluye dos interacciones de ejemplo precargadas, de modo que el modelo "recuerda" el contexto de la tienda desde el inicio.

Cómo ejecutarlo:

bash
python app_3.py

Cómo usarlo:

Escribe tu pregunta sobre algún producto cuando el programa te lo pida (Cliente: ).
El asistente responderá incluyendo precio, disponibilidad y características principales.
Escribe salir, exit o quit para terminar.
<img width="1320" height="968" alt="image" src="https://github.com/user-attachments/assets/b3917a8a-cb68-4f75-84aa-517f3112f56f" />

