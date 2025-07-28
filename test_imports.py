import streamlit as st
import importlib
import platform

def verificar_modulo(nome_modulo, nome_pip=None):
    try:
        modulo = importlib.import_module(nome_modulo)
        versao = getattr(modulo, '__version__', 'instalado')
        return True, versao, ""
    except ImportError as e:
        comando = f"pip install {nome_pip or nome_modulo}"
        return False, None, comando

obrigatorias = {
    "streamlit": "streamlit",
    "cv2": "opencv-python",
    "pandas": "pandas",
    "PIL": "pillow",
    "qrcode": "qrcode",
    "pyzbar": "pyzbar",
    "sqlite3": None,
    "numpy": "numpy"
}

opcionais = {
    "easyocr": "easyocr",
    "ultralytics": "ultralytics",
    "torch": "torch"
}

st.title("🔍 Verificação de Ambiente para Visão Computacional")

st.header("📦 Dependências Obrigatórias")
for modulo, pip_nome in obrigatorias.items():
    ok, versao, comando = verificar_modulo(modulo, pip_nome)
    if ok:
        st.success(f"✓ {modulo} — versão: {versao}")
    else:
        st.error(f"✗ {modulo} não encontrado.")
        st.code(comando, language='bash')

st.header("🔧 Dependências Opcionais")
for modulo, pip_nome in opcionais.items():
    ok, versao, comando = verificar_modulo(modulo, pip_nome)
    if ok:
        st.success(f"✓ {modulo} — versão: {versao}")
    else:
        st.warning(f"⚠ {modulo} não encontrado.")
        st.code(comando, language='bash')

try:
    import torch
    st.header("⚙️ Verificação de Hardware")
    st.success("GPU disponível ✅" if torch.cuda.is_available() else "⚠ Apenas CPU disponível")
except:
    pass

st.header("🖥️ Informações do Sistema")
st.text(f"Sistema: {platform.system()} {platform.release()}")
st.text(f"Python: {platform.python_version()}")
