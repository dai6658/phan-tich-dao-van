
import streamlit as st
import os
import tempfile
from model_utils import load_model
from file_utils import read_file
from analyzer import analyze_plagiarism

model = load_model()

st.title("Phát hiện đạo văn theo câu")

file_suspect = st.file_uploader("Tải lên file nghi vấn", type=["txt", "pdf", "docx"])
file_sources = st.file_uploader("Tải lên các file nguồn", type=["txt", "pdf", "docx"], accept_multiple_files=True)
threshold = st.slider("Ngưỡng phát hiện (Cosine Similarity)", 0.5, 1.0, 0.8, 0.01)

if file_suspect and file_sources:
    with tempfile.TemporaryDirectory() as tmp:
        path_sus = os.path.join(tmp, file_suspect.name)
        with open(path_sus, "wb") as f:
            f.write(file_suspect.read())

        path_sources = []
        for fs in file_sources:
            p = os.path.join(tmp, fs.name)
            with open(p, "wb") as f:
                f.write(fs.read())
            path_sources.append(p)

        st.info("Đang phân tích...")
        results = analyze_plagiarism(path_sus, path_sources, model, read_file, threshold)

        from underthesea import sent_tokenize
        from model_utils import remove_numbered_prefix

        content = read_file(path_sus)
        content = remove_numbered_prefix(content)
        cau_nghi_van = sent_tokenize(content)
        tong_cau = len(cau_nghi_van)
        cau_nghi_dao = {r['cau_nghi'] for r in results}
        so_cau_nghi = len(cau_nghi_dao)
        ty_le = so_cau_nghi / tong_cau if tong_cau > 0 else 0

        if ty_le >= 0.7:
            ket_luan = "Đạo văn nghiêm trọng"
        elif ty_le >= 0.3:
            ket_luan = "Đạo văn một phần"
        elif so_cau_nghi > 0:
            ket_luan = "Một vài câu bị nghi đạo"
        else:
            ket_luan = "Không có dấu hiệu đạo văn"

        st.markdown(f"""
        ### 🧾 Kết quả tổng hợp
        - Tổng số câu: **{tong_cau}**
        - Số câu nghi đạo văn: **{so_cau_nghi}**
        - Tỷ lệ nghi đạo: **{ty_le:.0%}**
        - **Kết luận:** {ket_luan}
        """)

        if results:
            st.warning(f"Chi tiết các câu bị nghi đạo văn:")
            for r in results:
                st.markdown(f"""
                <b>Câu nghi vấn:</b> {r['cau_nghi']}<br>
                <b>Câu nguồn ({r['nguon']}):</b> {r['cau_nguon']}<br>
                <b>Độ tương đồng:</b> {r['diem']}
                <hr>
                """, unsafe_allow_html=True)
        else:
            st.success("Không phát hiện đạo văn từ các nguồn đã chọn.")
