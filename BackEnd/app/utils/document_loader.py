from dotenv import load_dotenv
load_dotenv()

import os
import json
from langchain_google_genai import ChatGoogleGenerativeAI

# Usa el modelo correcto para Google AI Studio API Key gratuita
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

def load_documents(cliente_id):
    docs = []
    ruta = f"documents/{cliente_id}"
    if not os.path.exists(ruta):
        raise Exception(f"No se encontraron documentos para el cliente {cliente_id}")
    for archivo in os.listdir(ruta):
        path = os.path.join(ruta, archivo)
        if archivo.endswith('.txt'):
            with open(path, 'r', encoding='utf-8') as f:
                docs.append(f.read())
        elif archivo.endswith('.json'):
            with open(path, 'r', encoding='utf-8') as f:
                docs.append(json.dumps(json.load(f), ensure_ascii=False))
    return docs

def retrieve_relevant_context(docs, pregunta, max_fragments=3):
    # Recupera los fragmentos más relevantes (búsqueda simple por coincidencia de palabras)
    pregunta_lower = pregunta.lower()
    relevancia = []
    for doc in docs:
        score = sum(1 for palabra in pregunta_lower.split() if palabra in doc.lower())
        if score > 0:
            relevancia.append((score, doc))
    relevancia.sort(reverse=True)
    # Devuelve los fragmentos más relevantes
    return '\n'.join([frag for _, frag in relevancia[:max_fragments]])

def consulta_gemini_studio(cliente_id, pregunta):
    docs = load_documents(cliente_id)
    contexto = retrieve_relevant_context(docs, pregunta)
    prompt = f"Contexto:\n{contexto}\n\nPregunta: {pregunta}\n\nResponde de forma precisa y profesional."
    respuesta = llm.invoke(prompt)
    return respuesta
