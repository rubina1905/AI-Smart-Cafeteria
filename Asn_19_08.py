import os
import shutil
import chromadb
import gradio as gr
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from getpass import getpass
print("Libraries loaded successfully!")
GEMINI_API_KEY = getpass("Enter your Google AI Studio API key: ")
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY
from google import genai
gemini_client = genai.Client(
    api_key=GEMINI_API_KEY
)
print("Gemini API configured successfully!")