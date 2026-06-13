# Troubleshooting Guide — BovineEye AI

Panduan ini berisi daftar error umum yang mungkin ditemui saat menjalankan BovineEye AI, beserta penyebab dan solusinya.

---

## Table of Contents

1. [Error Instalasi & Setup](#1-error-instalasi--setup)
2. [Error Saat Menjalankan Aplikasi](#2-error-saat-menjalankan-aplikasi)
3. [Error Saat Upload & Deteksi](#3-error-saat-upload--deteksi)
4. [Error Koneksi Roboflow API](#4-error-koneksi-roboflow-api)
5. [Error di Browser (Frontend)](#5-error-di-browser-frontend)
6. [Error Deployment (Railway)](#6-error-deployment-railway)
7. [Tips Umum](#7-tips-umum)

---

## 1. Error Instalasi & Setup

---

### ❌ `pip: command not found`

**Penyebab:** pip tidak terinstal atau tidak ada di PATH sistem.

**Solusi:**
```bash
# Coba dengan pip3
pip3 install flask inference-sdk opencv-python numpy

# Atau install pip terlebih dahulu
python -m ensurepip --upgrade
```

---

### ❌ `ERROR: Could not find a version that satisfies the requirement opencv-python`

**Penyebab:** Versi Python tidak kompatibel atau pip perlu di-update.

**Solusi:**
```bash
python -m pip install --upgrade pip
pip install opencv-python
```

Jika di server Linux tanpa GUI (Railway, Ubuntu server):
```bash
pip install opencv-python-headless
```

---

### ❌ `ModuleNotFoundError: No module named 'inference_sdk'`

**Penyebab:** Package `inference-sdk` belum terinstal, atau virtual environment tidak aktif.

**Solusi:**
```bash
# Pastikan venv aktif
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows

# Install ulang
pip install inference-sdk
```

---

## 2. Error Saat Menjalankan Aplikasi

---

### ❌ `Address already in use` / `Port 5000 is in use`

**Penyebab:** Port 5000 sudah digunakan oleh proses lain (atau instance Flask sebelumnya).

**Solusi:**
```bash
# Linux/macOS — cari dan matikan proses di port 5000
lsof -i :5000
kill -9 <PID>

# Windows — cari PID yang menggunakan port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Atau jalankan di port berbeda
PORT=5001 python app.py
```

---

### ❌ `FileNotFoundError: [Errno 2] No such file or directory: 'templates/index.html'`

**Penyebab:** File `index.html` tidak berada di folder `templates/`, atau perintah dijalankan dari direktori yang salah.

**Solusi:**
```bash
# Pastikan struktur folder benar
ls templates/
# Harus menampilkan: index.html

# Jalankan dari root direktori proyek
cd /path/to/bovineeye-ai
python app.py
```

---

### ❌ `PermissionError: [Errno 13] Permission denied: 'static/results'`

**Penyebab:** Aplikasi tidak memiliki izin untuk membuat atau menulis ke folder `static/results/`.

**Solusi:**
```bash
# Buat folder secara manual dengan izin yang benar
mkdir -p static/results
chmod 755 static/results    # Linux/macOS
```

---

## 3. Error Saat Upload & Deteksi

---

### ❌ Halaman tidak merespons setelah upload gambar

**Penyebab:** Koneksi ke Roboflow API gagal, atau API Key tidak valid.

**Solusi:**
1. Periksa koneksi internet
2. Periksa API Key di `app.py`
3. Buka terminal yang menjalankan Flask — lihat error message di output log
4. Pastikan model ID `deteksi-sapi/8` benar dan masih aktif di akun Roboflow

---

### ❌ Gambar hasil muncul tanpa bounding box

**Penyebab:**
- Model tidak mendeteksi objek apa pun dalam gambar (confidence terlalu rendah)
- Gambar tidak mengandung objek yang relevan (bukan foto mata sapi)

**Solusi:**
- Gunakan foto mata sapi yang jelas, cukup cahaya, dan fokus pada area mata
- Pastikan kualitas gambar minimal 640×640 piksel
- Hindari foto buram, terlalu gelap, atau objek terlalu jauh

---

### ❌ `cv2.error: OpenCV(4.x) error` saat memproses gambar

**Penyebab:** File gambar corrupt atau format tidak didukung OpenCV.

**Solusi:**
- Pastikan file adalah JPEG atau PNG yang valid
- Coba konversi gambar ke JPEG terlebih dahulu menggunakan aplikasi foto
- Hindari format RAW (.cr2, .nef) atau WebP yang mungkin tidak didukung penuh

---

## 4. Error Koneksi Roboflow API

---

### ❌ `AuthenticationError` / `Invalid API Key`

**Penyebab:** API Key yang dikonfigurasi tidak valid atau sudah kedaluwarsa.

**Solusi:**
1. Login ke [app.roboflow.com](https://app.roboflow.com)
2. Buka **Settings → API Keys**
3. Salin API Key yang benar
4. Update di `app.py`:
```python
api_key="API_KEY_BARU_ANDA"
```

---

### ❌ `ModelNotFound` / `404` dari Roboflow

**Penyebab:** Model ID `deteksi-sapi/8` tidak ditemukan, mungkin versi berubah atau dihapus.

**Solusi:**
1. Login ke Roboflow → buka project `deteksi-sapi`
2. Lihat versi model yang tersedia di tab **Versions**
3. Update `MODEL_ID` di `app.py` sesuai versi yang aktif:
```python
MODEL_ID = "deteksi-sapi/8"   # Ganti angka versi jika perlu
```

---

### ❌ `ConnectionError` / `Timeout` ke Roboflow

**Penyebab:** Koneksi internet lambat atau Roboflow sedang maintenance.

**Solusi:**
- Cek status Roboflow di [status.roboflow.com](https://status.roboflow.com)
- Coba beberapa menit kemudian
- Pastikan tidak ada firewall/proxy yang memblokir koneksi ke `detect.roboflow.com`

---

## 5. Error di Browser (Frontend)

---

### ❌ Gambar hasil tidak muncul setelah deteksi berhasil

**Penyebab:** Cache browser menyimpan versi lama gambar dengan nama yang sama.

**Solusi:**
Kode sudah menggunakan cache-busting dengan timestamp:
```javascript
resImg.src = "/" + data.image_url + "?t=" + new Date().getTime();
```
Jika masih bermasalah, lakukan hard refresh: `Ctrl + Shift + R` (Windows/Linux) atau `Cmd + Shift + R` (macOS).

---

### ❌ Dark mode tidak tersimpan setelah refresh

**Penyebab:** Browser memblokir akses ke `localStorage` (mode Incognito/Private).

**Solusi:** Gunakan browser dalam mode normal (bukan Incognito).

---

### ❌ `fetch` error di console browser: `Failed to fetch`

**Penyebab:** Flask server tidak berjalan, atau URL yang diakses salah.

**Solusi:**
1. Pastikan Flask server berjalan: `python app.py`
2. Pastikan mengakses URL yang benar: `http://127.0.0.1:5000` (bukan port lain)
3. Periksa console browser (F12 → Console) untuk detail error

---

## 6. Error Deployment (Railway)

---

### ❌ Build gagal di Railway: `No module named 'cv2'`

**Penyebab:** `requirements.txt` menggunakan `opencv-python` yang membutuhkan GUI libraries yang tidak tersedia di server Linux Railway.

**Solusi:** Gunakan versi headless di `requirements.txt`:
```
opencv-python-headless>=4.8.0
```

---

### ❌ Aplikasi crash di Railway: `Port binding failed`

**Penyebab:** Aplikasi di-hardcode ke port tertentu, bukan menggunakan variabel `PORT` dari Railway.

**Solusi:** Pastikan kode berikut ada di `app.py`:
```python
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
```

---

### ❌ `static/results/` tidak ditemukan di Railway

**Penyebab:** Railway menggunakan filesystem ephemeral — folder yang dibuat saat runtime tidak persisten antar deploy.

**Solusi:** Pastikan kode membuat folder otomatis saat startup (sudah ada di `app.py`):
```python
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
```

---

## 7. Tips Umum

- **Selalu jalankan dari root direktori proyek** — bukan dari subfolder
- **Periksa terminal Flask** — semua error backend akan tercetak di sini
- **Buka DevTools browser (F12)** — tab Console dan Network sangat membantu debug masalah frontend
- **Gunakan gambar berkualitas baik** — minimal 640px, cahaya cukup, fokus pada mata sapi
- **Restart Flask server** setelah mengubah `app.py` — Flask tidak auto-reload kecuali `debug=True`

---

Masih mengalami masalah? Buka **GitHub Issue** di repository proyek ini dengan menyertakan:
1. Pesan error lengkap (screenshot atau copy-paste)
2. Langkah yang dilakukan sebelum error muncul
3. Versi Python dan OS yang digunakan
