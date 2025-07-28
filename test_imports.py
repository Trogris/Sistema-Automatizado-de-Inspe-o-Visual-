#!/usr/bin/env python3
"""
Script para testar as importações das bibliotecas necessárias
"""

print("Testando importações...")

try:
    import streamlit as st
    print("✓ Streamlit importado com sucesso")
except ImportError as e:
    print(f"✗ Erro ao importar Streamlit: {e}")

try:
    import cv2
    print("✓ OpenCV importado com sucesso")
except ImportError as e:
    print(f"✗ Erro ao importar OpenCV: {e}")

try:
    import pandas as pd
    print("✓ Pandas importado com sucesso")
except ImportError as e:
    print(f"✗ Erro ao importar Pandas: {e}")

try:
    from PIL import Image
    print("✓ Pillow importado com sucesso")
except ImportError as e:
    print(f"✗ Erro ao importar Pillow: {e}")

try:
    import qrcode
    print("✓ QRCode importado com sucesso")
except ImportError as e:
    print(f"✗ Erro ao importar QRCode: {e}")

try:
    import pyzbar
    print("✓ PyZBar importado com sucesso")
except ImportError as e:
    print(f"✗ Erro ao importar PyZBar: {e}")

try:
    import sqlite3
    print("✓ SQLite3 importado com sucesso")
except ImportError as e:
    print(f"✗ Erro ao importar SQLite3: {e}")

try:
    import numpy as np
    print("✓ NumPy importado com sucesso")
except ImportError as e:
    print(f"✗ Erro ao importar NumPy: {e}")

# Testando importações que podem não estar disponíveis ainda
try:
    import easyocr
    print("✓ EasyOCR importado com sucesso")
except ImportError as e:
    print(f"⚠ EasyOCR não disponível ainda: {e}")

try:
    from ultralytics import YOLO
    print("✓ Ultralytics YOLO importado com sucesso")
except ImportError as e:
    print(f"⚠ Ultralytics não disponível ainda: {e}")

print("\nTeste de importações concluído!")

