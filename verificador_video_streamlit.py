import streamlit as st
import cv2
import tempfile
from PIL import Image
import numpy as np

st.set_page_config(page_title="Verificação de Equipamento por Vídeo", layout="centered")

st.title("🎥 Verificação Final via Visão Computacional")
st.write("Faça o upload de um vídeo da montagem final para simular o checklist automático antes do lacre.")

# Upload do vídeo
video_file = st.file_uploader("📤 Envie o vídeo da verificação final", type=["mp4", "mov", "avi"])

if video_file:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())

    st.video(video_file)

    st.markdown("---")
    st.subheader("🔎 Simulação de Reconhecimento em Frames")

    cap = cv2.VideoCapture(tfile.name)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    interval = max(total_frames // 5, 1)  # Pega 5 frames distribuídos

    checklist = {
        "Etiqueta visível": False,
        "Tampa encaixada": False,
        "Parafusos presentes": False,
        "Conectores instalados": False
    }

    # Armazena imagens e resultados antes de exibir
    frames_info = []

    for i in range(5):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i * interval)
        ret, frame = cap.read()
        if not ret:
            continue

        # Simulação de detecção (exemplo simples)
        detected_items = []
        if i % 2 == 0:
            checklist["Etiqueta visível"] = True
            detected_items.append("Etiqueta")
        if i % 3 == 0:
            checklist["Tampa encaixada"] = True
            detected_items.append("Tampa")
        if i % 2 == 1:
            checklist["Parafusos presentes"] = True
            detected_items.append("Parafuso")
        if i % 4 == 0:
            checklist["Conectores instalados"] = True
            detected_items.append("Conector")

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame_rgb)

        frames_info.append({
            "image": pil_image,
            "caption": f"Frame {i+1}",
            "detected": detected_items
        })

    cap.release()

    # Agora exibimos fora do loop principal
    for item in frames_info:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(item["image"], caption=item["caption"], use_column_width=True)
        with col2:
            if item["detected"]:
                st.success("✔️ " + ", ".join(item["detected"]))
            else:
                st.error("❌ Nenhum item detectado")

    st.markdown("---")
    st.subheader("✅ Resultado Final do Checklist")

    all_ok = all(checklist.values())
    for item, ok in checklist.items():
        st.write(f"- {item}: {'✔️' if ok else '❌'}")

    if all_ok:
        st.success("✅ Equipamento verificado com sucesso. OK para lacre.")
    else:
        st.error("⚠️ Falta de itens. Verifique antes de lacrar.")


