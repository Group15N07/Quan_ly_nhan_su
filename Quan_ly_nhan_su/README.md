# 📘 Human Resource Management System

## 🚀 Mô tả dự án
Hệ thống quản lý nhân sự tích hợp chấm công bằng khuôn mặt và gameboard (thưởng điểm), phân quyền theo vai trò `Admin`, `Manager`, `Employee`. Backend sử dụng Flask, nhận diện khuôn mặt với + deeplearning.

---

## ⚙️ Yêu cầu hệ thống
- Python 3.9+
- Anaconda hoặc Miniconda
- Webcam (nếu sử dụng tính năng chấm công khuôn mặt)

---

## 🐍 1. Cài đặt Anaconda (nếu chưa có)

Tải và cài đặt tại:  
👉 https://www.anaconda.com/products/distribution

---

## 📦 2. Tạo môi trường ảo với Anaconda

```bash
# Tạo môi trường tên "hrms"
conda create -n hrms python=3.9

# Kích hoạt môi trường
conda activate hrms
```

---

## 📄 3. Cài các thư viện cần thiết từ requirements.txt

```bash
# Di chuyển đến thư mục chứa project
cd Quan_ly_nhan_su

# Cài thư viện
pip install -r requirements.txt
```

📌 Nếu gặp lỗi với OpenCV hoặc dlib, bạn có thể cài riêng:
```bash
pip install opencv-python
```

---

## 🏃‍♂️ 4. Chạy ứng dụng Flask

```bash
# Đặt biến môi trường (Windows)
set FLASK_APP=run.py
set FLASK_ENV=development

# Khởi chạy
flask run
```

⏱ Ứng dụng sẽ chạy tại:  
👉 http://127.0.0.1:5000

---

## 👤 Tài khoản mẫu để đăng nhập

| Role     | Username    | Password   |
|----------|-------------|------------|
| Admin    | admin       | admin123   |
| Manager  | manager     | manager123 |
| Employee | hoangnguyen | hoang123   |

---

## 📂 Cấu trúc thư mục chính

```
Quan_ly_nhan_su/
├── app/
│   ├── routes/                # Các route Flask theo từng chức năng
│   ├── models/                # Cấu trúc bảng và ORM
│   ├── templates/             # Giao diện Jinja2
│   ├── static/                # File CSS, JS, ảnh,...
│   ├── utils/                 # Hàm xử lý bổ trợ
│   ├── decorators/            # Phân quyền truy cập (role_required, login_required...)
│   └── services/              # Các lớp xử lý logic tách biệt của facemodel
├── run.py                     # File khởi chạy Flask
├── requirements.txt           # Thư viện cần cài
└── README.md
```

---

## 💬 Góp ý hoặc hỗ trợ

Liên hệ: 23010101@st.phenikaa-uni.edu.vn


---

## 🔗 Repository GitHub

Mã nguồn được lưu trữ tại:  
👉 [https://github.com/Group15N07/Quan_ly_nhan_su](https://github.com/Group15N07/Quan_ly_nhan_su)