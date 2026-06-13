# BovineEye AI — Portfolio Case Study

**Deteksi Dini Penyakit Mata Sapi dengan Kecerdasan Buatan**

---

## Sekilas Proyek

| | |
|---|---|
| **Nama Proyek** | BovineEye AI |
| **Kategori** | AI Web Application · Computer Vision · Healthcare Tech |
| **Teknologi** | Python, Flask, YOLOv4, OpenCV, Tailwind CSS |
| **Tahun** | 2025 |
| **Status** | Selesai & Deployed |
| **Live Demo** | [Link Demo](#) |
| **Repository** | [GitHub](#) |

---

## Latar Belakang — Masalah yang Diselesaikan

Penyakit *Pink Eye* (IBK) adalah ancaman nyata bagi peternak sapi Indonesia. Jika tidak tertangani dalam 24–48 jam pertama, bakteri *Moraxella bovis* bisa menyebabkan kebutaan permanen pada sapi — yang berarti kerugian ekonomi langsung bagi peternak.

**Masalah utamanya sederhana tapi kritis:** sebagian besar peternak tidak bisa membedakan mata sapi yang "sedikit merah biasa" dengan yang sudah terinfeksi. Dan dokter hewan tidak selalu bisa dipanggil ke lapangan dengan cepat.

> *"Butuh tools yang bisa dipakai peternak sendiri, tanpa perlu latar belakang medis."*

BovineEye AI menjawab tantangan ini — sebuah aplikasi web yang memungkinkan siapa pun mendeteksi Pink Eye cukup dengan mengunggah foto mata sapi dari smartphone mereka.

---

## Solusi yang Dibangun

Aplikasi web satu halaman yang mengintegrasikan model *deep learning* YOLOv4 dengan antarmuka yang bersih dan mudah digunakan — bahkan oleh pengguna tanpa latar belakang teknologi sekalipun.

### Yang bisa dilakukan pengguna:

1. Buka aplikasi di browser (desktop atau mobile)
2. Upload atau drag & drop foto mata sapi
3. Dalam hitungan detik, sistem menganalisis gambar dan menampilkan:
   - **Status diagnosis** — Sehat atau Positif Pink Eye
   - **Tingkat keyakinan model** (confidence score)
   - **Bounding box** yang menunjukkan area yang terdeteksi
   - **Panduan tindakan medis** yang spesifik dan praktis

Tidak perlu install apapun. Tidak perlu pengetahuan teknis.

---

## Proses & Pendekatan

### 1. Riset & Pemahaman Domain

Sebelum menulis satu baris kode pun, saya terlebih dahulu mempelajari karakteristik klinis Pink Eye pada sapi — bagaimana perbedaan visual antara mata sehat dan yang terinfeksi, dan apa yang dokter hewan lihat ketika mendiagnosis.

Ini penting agar dataset yang dikumpulkan dan label yang dibuat benar-benar merepresentasikan kondisi nyata di lapangan.

### 2. Pembangunan Dataset & Training Model

Dataset dibangun dari foto mata sapi asli, lalu dikelola menggunakan platform **Roboflow** untuk anotasi, augmentasi, dan training. Model YOLOv4 dipilih karena keunggulannya dalam kecepatan inferensi tanpa mengorbankan akurasi — krusial untuk pengalaman pengguna yang responsif.

Proses augmentasi mencakup flip horizontal, variasi brightness, dan rotasi untuk membuat model robust terhadap variasi kondisi foto di lapangan (pencahayaan berbeda, sudut foto berbeda, kualitas kamera berbeda).

### 3. Backend — Flask + OpenCV

Backend Flask bertugas sebagai jembatan antara antarmuka pengguna dan model AI di cloud. Setiap gambar yang diunggah diberi nama unik (UUID) untuk menghindari konflik, dikirim ke Roboflow API untuk diproses, dan hasilnya dianotasi secara lokal menggunakan OpenCV sebelum dikembalikan ke pengguna.

Logika klasifikasi dibuat sesederhana mungkin: jika ada prediksi dengan label bukan "sehat", sistem langsung menandai sebagai positif.

### 4. Frontend — UX yang Diprioritaskan

Desain antarmuka sengaja dibuat bersih dan minimalis. Prioritas utama adalah **kemudahan penggunaan** — dropzone yang intuitif, feedback visual yang jelas (loading spinner + animasi scan), dan hasil yang ditampilkan dalam format kartu yang mudah dibaca.

Dark mode diimplementasikan dengan Tailwind CSS dan preferensi disimpan di localStorage agar pengalaman pengguna tetap konsisten antar sesi.

---

## Hasil & Dampak

- ✅ Model berhasil membedakan kondisi mata sapi sehat dan positif Pink Eye
- ✅ Waktu respons rata-rata di bawah 5 detik dalam kondisi koneksi normal
- ✅ Antarmuka berhasil digunakan oleh responden non-teknis dalam sesi UAT
- ✅ Aplikasi berhasil di-deploy ke Railway dan dapat diakses secara online
- ✅ Penelitian selesai dan terdaftar di repository skripsi UNSADA

---

## Tantangan & Cara Mengatasinya

**Tantangan 1 — Kualitas foto lapangan sangat bervariasi**

Foto yang diambil peternak di lapangan jauh berbeda dari foto dataset yang terkontrol: cahaya tidak merata, kamera goyang, jarak tidak konsisten. Solusinya adalah augmentasi dataset yang agresif dan pemilihan YOLOv4 yang secara arsitektur lebih robust terhadap variasi input.

**Tantangan 2 — Menampilkan gambar hasil tanpa cache browser**

Karena nama file gambar hasil bisa saja identik lintas sesi, browser terkadang menampilkan gambar lama dari cache. Solusinya: menambahkan timestamp sebagai query string pada URL gambar (`?t=<timestamp>`), memaksa browser selalu mengambil versi terbaru.

**Tantangan 3 — Deployment di server Linux tanpa GUI**

Package `opencv-python` memerlukan library GUI yang tidak tersedia di server Railway. Solusinya: mengganti dengan `opencv-python-headless` di `requirements.txt` untuk environment produksi.

---

## Cuplikan Kode Kunci

### Logika Klasifikasi & Anotasi (app.py)

```python
for pred in predictions:
    label = pred['class'].lower()
    conf  = pred['confidence']

    # Konversi format koordinat Roboflow (center) ke OpenCV (corner)
    x = int(pred['x'] - pred['width'] / 2)
    y = int(pred['y'] - pred['height'] / 2)

    if "sehat" not in label:
        is_positive = True

    # Warna bbox: ungu untuk positif, hijau untuk sehat
    color = (153, 72, 236) if "sehat" not in label else (0, 255, 0)
    cv2.rectangle(image, (x, y), (x + w, y + h), color, 3)
```

### Dynamic UI Update tanpa Reload (index.html)

```javascript
const response = await fetch("/detect", { method: "POST", body: formData });
const data = await response.json();

// Update gambar dengan cache-busting
resImg.src = "/" + data.image_url + "?t=" + new Date().getTime();

// Update status dengan warna kondisional
statusText.className = data.status.includes("POSITIF")
  ? "text-xl font-black italic text-primary uppercase"   // merah/pink
  : "text-xl font-black italic text-emerald-500 uppercase"; // hijau
```

---

## Pelajaran yang Didapat

Proyek ini mengajarkan saya bahwa membangun aplikasi AI bukan hanya soal memilih model terbaik — tapi juga soal **merancang pengalaman pengguna yang membuat teknologi tersebut benar-benar bisa digunakan** oleh orang yang membutuhkannya.

Peternak tidak peduli dengan angka mAP atau arsitektur CSPDarknet53. Yang mereka pedulikan adalah: *apakah sapi saya sakit? apa yang harus saya lakukan sekarang?* — dan itulah yang BovineEye AI jawab.

---

## Stack Teknologi Lengkap

```
Backend          Frontend           AI & Cloud          DevOps
────────────     ────────────────   ─────────────────   ────────────
Python 3.10+     HTML5              YOLOv4              Railway
Flask 2.3+       Tailwind CSS       Roboflow Cloud      Git / GitHub
OpenCV 4.8+      Vanilla JS         Model: v8
inference-sdk    Font Awesome       Dataset: Custom
uuid, os         Fetch API
```

---

## Tentang Pengembang

Proyek ini dikerjakan sebagai bagian dari penelitian skripsi S1 Teknologi Informasi di Universitas Darma Persada (UNSADA).

Saya tertarik pada pengembangan aplikasi yang memiliki dampak nyata — menggabungkan kemampuan teknis (web development, computer vision) dengan pemahaman kebutuhan pengguna di lapangan.

📬 Tertarik berdiskusi atau berkolaborasi? Hubungi saya di [LinkedIn](#) atau [Email](#).

---

*© 2025 Fachri Ramdhan Al Mubaroq · Universitas Darma Persada (UNSADA)*
*Repository Skripsi: http://repository.unsada.ac.id/5030/*
