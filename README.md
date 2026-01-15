# 🐄 BovineEye-AI

<div align="center">
  <img src="screenshoot.png" alt="BovineEye-AI Banner" width="800" style="border-radius: 15px shadow: 10px">
  
  <p align="center">
    <strong>APLIKASI DETEKSI DINI PENYAKIT MATA PINK-EYE PADA SAPI BERBASIS CITRA MENGGUNAKAN MODEL DEEP LEARNING ALGORITMA YOLOv4</strong>
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
    <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind">
    <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
  </p>
</div>

---

## 📖 Ringkasan Proyek

**BovineEye-AI** adalah solusi berbasis kecerdasan buatan (AI) yang dirancang untuk membantu peternak mendeteksi penyakit _Infectious Bovine Keratoconjunctivitis_ (Pink Eye) secara mandiri. Dengan memanfaatkan algoritma **YOLOv4**, sistem ini mampu mengenali gejala klinis pada mata sapi melalui pemindaian foto digital dengan tingkat akurasi yang dioptimalkan.

---

## 🚀 Fitur Unggulan

- **Deep Scan Analysis**: Pemindaian gambar menggunakan arsitektur YOLOv4 yang efisien.
- **Dual-Theme Dashboard**: Antarmuka modern dengan dukungan _Dark Mode_ dan _Light Mode_.
- **Automated Medical Recommendations**: Memberikan saran tindakan medis praktis (Isolasi, Pembersihan, Pengobatan).
- **Visual Bounding Box**: Menampilkan kotak deteksi berwarna (Hijau: Sehat | Pink: Positif) langsung pada objek.
- **Dynamic UX**: Transisi antar halaman tanpa reload menggunakan **Fetch API**.

---

## 🛠️ Stack Teknologi (Tech Stack)

<table width="100%" aligth="center">
  <tr>
    <th width="50%">💻 Frontend (Client Side)</th>
    <th width="50%">⚙️ Backend & AI Engine (Server Side)</th>
  </tr>
  <tr>
    <td valign="top">
      <table width="100%">
        <tr><td><b>HTML5</b></td><td>Struktur</td><td><img src="https://img.shields.io/badge/-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"></td></tr>
        <tr><td><b>Tailwind</b></td><td>Styling</td><td><img src="https://img.shields.io/badge/-TailwindCSS-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white"></td></tr>
        <tr><td><b>JS</b></td><td>Interaksi</td><td><img src="https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"></td></tr>
        <tr><td><b>Icon</b></td><td>Visual</td><td><img src="https://img.shields.io/badge/-FontAwesome-339AF0?style=flat-square&logo=font-awesome&logoColor=white"></td></tr>
      </table>
    </td>
    <td valign="top">
      <table width="100%">
        <tr><td><b>Python</b></td><td>Logic</td><td><img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white"></td></tr>
        <tr><td><b>Flask</b></td><td>Framework</td><td><img src="https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white"></td></tr>
        <tr><td><b>OpenCV</b></td><td>Citra</td><td><img src="https://img.shields.io/badge/-OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white"></td></tr>
        <tr><td><b>YOLOv4</b></td><td>Deteksi</td><td><img src="https://img.shields.io/badge/-YOLOv4-00FFFF?style=flat-square&logo=ai&logoColor=black"></td></tr>
      </table>
    </td>
  </tr>
</table>

---

## 📐 Arsitektur Sistem

Sistem ini menggunakan alur kerja terintegrasi sebagai berikut:

1.  **Unggah Citra**: User mengunggah foto mata sapi melalui dashboard.
2.  **Inference**: Server Flask meneruskan gambar ke Cloud API Roboflow (YOLOv4).
3.  **Anatomi Deteksi**: Backend menerima koordinat objek, kemudian OpenCV merender bounding box secara lokal.
4.  **Diagnosa**: Sistem memvalidasi label "Sehat" vs "Pink Eye" dan menentukan stadium penyakit.
5.  **Output**: Hasil visual dan saran medis ditampilkan secara real-time.

---

## 📦 Panduan Instalasi

1. **Persyaratan Sistem**:

   - Python 3.10+
   - Koneksi Internet

2. **Instalasi Library**:

   ```bash
   pip install flask inference-sdk opencv-python numpy

   ```

3. **Konfigurasi Folder:** Pastikan folder static/results dan templates sudah tersedia di direktori utama.

4. **Menjalankan Aplikasi:**
   ```bash
   python app.py
   ```
   Akses aplikasi melalui browser di alamat `http://127.0.0.1:5001`.

---

**Peneliti:** Fachri Ramdhan  
**Fokus Penelitian:** Deteksi Dini Penyakit Mata Pink-Eye pada Sapi berbasis citra
**Universitas Darma Persada**
