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

<center>

## 🛠️ Stack Teknologi (Tech Stack)

<table width="100%" style="max-width: 900px;">
  <thead>
    <tr>
      <th width="50%">💻 Frontend (Client Side)</th>
      <th width="50%">⚙️ Backend & AI Engine (Server Side)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td valign="top">
        <table width="100%">
          <tr>
            <td width="30%"><img src="https://img.shields.io/badge/-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"></td>
            <td><small>Struktur antarmuka web yang responsif dan semantik.</small></td>
          </tr>
          <tr>
            <td><img src="https://img.shields.io/badge/-TailwindCSS-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white"></td>
            <td><small>Desain UI modern dengan pendekatan <i>utility-first</i>.</small></td>
          </tr>
          <tr>
            <td><img src="https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"></td>
            <td><small>Logika sisi klien dan interaktivitas DOM.</small></td>
          </tr>
          <tr>
            <td><img src="https://img.shields.io/badge/-FontAwesome-339AF0?style=flat-square&logo=font-awesome&logoColor=white"></td>
            <td><small>Ikon vektor untuk visualisasi navigasi sistem.</small></td>
          </tr>
        </table>
      </td>
      <td valign="top">
        <table width="100%">
          <tr>
            <td width="35%"><img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white"></td>
            <td><small>Bahasa utama pengolahan data dan algoritma AI.</small></td>
          </tr>
          <tr>
            <td><img src="https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white"></td>
            <td><small>Micro-framework integrasi model AI ke web.</small></td>
          </tr>
          <tr>
            <td><img src="https://img.shields.io/badge/-Roboflow-6706CE?style=flat-square&logo=roboflow&logoColor=white"></td>
            <td><small>Manajemen dataset dan <i>cloud inference</i> YOLOv4.</small></td>
          </tr>
          <tr>
            <td><img src="https://img.shields.io/badge/-OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white"></td>
            <td><small>Pra-pemrosesan citra digital sebelum deteksi.</small></td>
          </tr>
          <tr>
            <td><img src="https://img.shields.io/badge/-YOLOv4-00FFFF?style=flat-square&logo=ai&logoColor=black"></td>
            <td><small><i>Deep Learning</i> inti untuk deteksi objek (IBK).</small></td>
          </tr>
        </table>
      </td>
    </tr>
  </tbody>
</table>

</center>

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
