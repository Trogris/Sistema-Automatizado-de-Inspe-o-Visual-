#!/bin/bash

# Script de Instalação - Sistema de Verificação Visual Automatizada
# Autor: Manus AI
# Data: Julho 2025

echo "=================================="
echo "🔍 Sistema de Verificação Visual"
echo "    Instalação Automatizada"
echo "=================================="

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Por favor, instale Python 3.10 ou superior."
    exit 1
fi

# Verificar versão do Python
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
required_version="3.10"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" = "$required_version" ]; then
    echo "✅ Python $python_version detectado"
else
    echo "❌ Python $python_version detectado. Versão mínima requerida: $required_version"
    exit 1
fi

# Verificar se pip está instalado
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 não encontrado. Por favor, instale pip."
    exit 1
fi

echo "✅ pip3 detectado"

# Atualizar pip
echo "📦 Atualizando pip..."
pip3 install --upgrade pip

# Instalar dependências Python
echo "📦 Instalando dependências Python..."
pip3 install -r requirements.txt

# Detectar sistema operacional e instalar dependências do sistema
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "🐧 Sistema Linux detectado"
    echo "📦 Instalando dependências do sistema..."
    
    # Verificar se apt está disponível (Ubuntu/Debian)
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y libzbar0
        echo "✅ Dependências do sistema instaladas"
    else
        echo "⚠️  Sistema Linux sem apt detectado. Instale manualmente: libzbar0"
    fi
    
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "🍎 Sistema macOS detectado"
    
    # Verificar se brew está disponível
    if command -v brew &> /dev/null; then
        echo "📦 Instalando dependências via Homebrew..."
        brew install zbar
        echo "✅ Dependências do sistema instaladas"
    else
        echo "⚠️  Homebrew não encontrado. Instale manualmente: zbar"
    fi
    
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    echo "🪟 Sistema Windows detectado"
    echo "⚠️  No Windows, as dependências são instaladas automaticamente via pip"
    
else
    echo "❓ Sistema operacional desconhecido: $OSTYPE"
    echo "⚠️  Pode ser necessário instalar dependências manualmente"
fi

# Criar diretórios necessários
echo "📁 Criando estrutura de diretórios..."
mkdir -p data/{images/{originals,processed,thumbnails},reports}
mkdir -p logs

# Testar instalação
echo "🧪 Testando instalação..."
cd src

# Teste básico de importações
python3 -c "
import streamlit
import cv2
import pandas as pd
import numpy as np
print('✅ Importações básicas OK')
"

# Testar ultralytics (pode demorar na primeira vez)
echo "🧪 Testando Ultralytics YOLOv8..."
python3 -c "
try:
    from ultralytics import YOLO
    print('✅ Ultralytics OK')
except Exception as e:
    print(f'⚠️  Ultralytics: {e}')
"

# Testar EasyOCR (pode demorar na primeira vez)
echo "🧪 Testando EasyOCR..."
python3 -c "
try:
    import easyocr
    print('✅ EasyOCR OK')
except Exception as e:
    print(f'⚠️  EasyOCR: {e}')
"

echo ""
echo "=================================="
echo "🎉 INSTALAÇÃO CONCLUÍDA!"
echo "=================================="
echo ""
echo "Para executar o sistema:"
echo "1. cd src"
echo "2. streamlit run streamlit_app.py"
echo ""
echo "Para testar a integração:"
echo "1. cd src"
echo "2. python3 integration_test.py"
echo ""
echo "Interface será aberta em: http://localhost:8501"
echo ""
echo "📖 Consulte o README.md para mais informações"
echo "=================================="

