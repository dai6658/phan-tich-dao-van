
# 📚 Hệ thống Phát hiện Đạo văn Ngữ nghĩa Tiếng Việt

Đây là một hệ thống phát hiện đạo văn sử dụng **SBERT tiếng Việt** để so sánh **ngữ nghĩa** giữa các câu trong nhiều văn bản. Hệ thống hỗ trợ các định dạng file: `.txt`, `.docx`, `.pdf` và có giao diện thân thiện qua **Streamlit**.

---

## 🧠 Tính năng chính

- ✅ Tiền xử lý tiếng Việt: tách câu, xóa stopword, chuẩn hóa.
- ✅ So sánh đạo văn theo **câu** chứ không phải toàn văn bản.
- ✅ Phát hiện đạo văn từ nhiều nguồn (nhiều file khác nhau).
- ✅ Sử dụng mô hình **keepitreal/vietnamese-sbert** từ Hugging Face.
- ✅ Hỗ trợ nhiều định dạng: `.txt`, `.docx`, `.pdf`.
- ✅ Giao diện web đơn giản, dễ sử dụng qua **Streamlit**.

---

## 📁 Cấu trúc thư mục

```
📦phan-tich-dao-van/
├── app.py                   # Giao diện Streamlit chính
├── analyzer.py              # Xử lý đạo văn (so sánh từng câu)
├── file_utils.py            # Đọc và xử lý văn bản từ các file
├── model_utils.py           # Load model SBERT
├── vietnamese-stopwords.txt # Danh sách stopword tiếng Việt
```

---

## 🚀 Hướng dẫn chạy

### 1. Cài đặt thư viện
```bash
pip install -r requirements.txt
```

**Yêu cầu chính:**
- `sentence-transformers`
- `underthesea`
- `scikit-learn`
- `streamlit`
- `python-docx`
- `PyPDF2`

### 2. Chạy ứng dụng
```bash
streamlit run app.py
```

---

## 📂 Cách sử dụng

1. Đặt các file cần so sánh vào cùng thư mục (hỗ trợ `.txt`, `.docx`, `.pdf`).
2. Mở giao diện Streamlit và chọn **file nghi vấn**, **file nguồn**.
3. Hệ thống sẽ tự động so sánh từng câu với các câu trong các file khác.
4. Hiển thị các câu giống nhau về ngữ nghĩa kèm điểm tương đồng (cosine similarity).
5. Cho biết liệu văn bản có đạo văn hay không (dựa vào số lượng câu bị trùng ý).

---

## ⚙️ Cách hoạt động (pipeline)

1. Đọc tất cả file văn bản.
2. Tách từng câu.
3. Tiền xử lý câu: chuẩn hóa, xóa dấu, bỏ stopword.
4. Mã hóa câu bằng SBERT để tạo **embedding vector**.
5. Tính cosine similarity giữa các câu nghi vấn và câu trong các file khác.
6. In ra kết quả nếu độ tương đồng >= 0.8.

---

## 📌 Lưu ý

- Hệ thống hoạt động tốt với văn bản tiếng Việt.
- Không hiệu quả với PDF dạng scan ảnh (không có text).
- Có thể mở rộng thêm: POS, NER, hoặc phân đoạn đạo văn theo đoạn dài.

---

## 📄 Giấy phép

Dự án mang tính học thuật và nghiên cứu phi thương mại.

---

## 👤 Tác giả
Nhóm 10- Kì 2 xử lý ngôn ngữ tự nhiên nhóm 200  
Hệ thống sử dụng mã nguồn mở từ cộng đồng Hugging Face và Underthesea.
