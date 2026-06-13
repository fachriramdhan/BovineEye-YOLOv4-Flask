# Dataset Documentation — BovineEye AI

> Dokumen ini mendeskripsikan dataset yang digunakan untuk melatih model YOLOv4 pada proyek deteksi Pink Eye pada sapi.

---

## Table of Contents

1. [Deskripsi Dataset](#1-deskripsi-dataset)
2. [Sumber Data](#2-sumber-data)
3. [Kelas (Label) Dataset](#3-kelas-label-dataset)
4. [Distribusi Dataset](#4-distribusi-dataset)
5. [Preprocessing & Augmentasi](#5-preprocessing--augmentasi)
6. [Format Anotasi](#6-format-anotasi)
7. [Dataset Split](#7-dataset-split)
8. [Contoh Sampel Data](#8-contoh-sampel-data)
9. [Catatan & Keterbatasan Dataset](#9-catatan--keterbatasan-dataset)

---

## 1. Deskripsi Dataset

| Properti | Detail |
|---|---|
| **Nama Dataset** | Deteksi Sapi — Pink Eye (IBK) |
| **Tugas** | Object Detection |
| **Domain** | Veteriner / Peternakan Sapi |
| **Platform Manajemen** | [Roboflow](https://app.roboflow.com) |
| **Versi Model Aktif** | v8 (`deteksi-sapi/8`) |
| **Total Gambar (sebelum augmentasi)** | *(diisi)* gambar |
| **Total Gambar (setelah augmentasi)** | *(diisi)* gambar |
| **Jumlah Kelas** | 2 kelas |

---

## 2. Sumber Data

### Metode Pengumpulan Data

| Sumber | Keterangan |
|---|---|
| Dokumentasi lapangan | Foto diambil langsung dari peternakan sapi dengan kondisi pencahayaan alami |
| Dataset publik | *(sebutkan jika ada, misal: dataset Kaggle, Google Open Images, dll.)* |
| Kolaborasi dokter hewan | Foto mata sapi yang sudah didiagnosa oleh dokter hewan setempat |

### Kondisi Pengambilan Foto

| Parameter | Keterangan |
|---|---|
| Jarak kamera ke objek | 20–50 cm dari mata sapi |
| Kondisi cahaya | Alami (outdoor) dan buatan (indoor kandang) |
| Sudut pengambilan | Frontal (lurus ke depan), ±15° lateral |
| Perangkat | Smartphone kamera minimal 12MP |
| Format file | JPEG (.jpg) |
| Resolusi rata-rata | 1280×720 – 4032×3024 piksel |

---

## 3. Kelas (Label) Dataset

| ID Kelas | Nama Kelas | Deskripsi | Warna Bbox |
|---|---|---|---|
| 0 | `sehat` | Mata sapi dalam kondisi normal, tidak ada tanda infeksi | Hijau `(0, 255, 0)` |
| 1 | `pink_eye` *(atau nama class yang digunakan)* | Mata sapi menunjukkan gejala Infectious Bovine Keratoconjunctivitis (IBK) | Ungu `(153, 72, 236)` |

### Karakteristik Visual per Kelas

**Kelas `sehat`:**
- Kornea mata jernih dan transparan
- Tidak ada kemerahan berlebih di sekitar mata
- Tidak ada eksudat (cairan/nanah) di sudut mata
- Bulu mata bersih

**Kelas Pink Eye (positif):**
- Kornea keruh / putih keabu-abuan (opasitas kornea)
- Kemerahan signifikan pada konjungtiva (iritasi)
- Keluar air mata berlebih (epifora)
- Mata tampak terpejam (fotofobia)
- Kemungkinan terlihat eksudat di sudut mata

---

## 4. Distribusi Dataset

### Jumlah Gambar per Kelas

| Kelas | Jumlah Gambar (Raw) | Persentase |
|---|---|---|
| `sehat` | *(diisi)* | *(diisi)*% |
| `pink_eye` | *(diisi)* | *(diisi)*% |
| **Total** | *(diisi)* | 100% |

> **Catatan keseimbangan data:** Jika distribusi tidak seimbang (imbalanced), jelaskan strategi yang diambil (oversampling kelas minoritas via augmentasi, undersampling, dll.)

### Jumlah Gambar per Split

| Split | Jumlah Gambar | Persentase |
|---|---|---|
| Training | *(diisi)* | ~70% |
| Validation | *(diisi)* | ~20% |
| Test | *(diisi)* | ~10% |
| **Total** | *(diisi)* | 100% |

---

## 5. Preprocessing & Augmentasi

Preprocessing dan augmentasi dilakukan menggunakan platform **Roboflow** sebelum training.

### Preprocessing

| Tahap | Parameter | Keterangan |
|---|---|---|
| Auto-Orient | Aktif | Memperbaiki orientasi gambar berdasarkan metadata EXIF |
| Resize | 416×416 piksel | Sesuai input size YOLOv4 standar |
| *(tambahkan jika ada)* | | |

### Augmentasi

Augmentasi diterapkan untuk memperbanyak variasi data training dan meningkatkan robustness model.

| Jenis Augmentasi | Parameter | Tujuan |
|---|---|---|
| Flip Horizontal | 50% probabilitas | Simulasi sapi dari sisi berlawanan |
| Rotasi | ±15° | Variasi sudut pengambilan foto |
| Brightness | ±25% | Variasi kondisi pencahayaan kandang |
| Blur | Max 1.5px | Simulasi foto sedikit buram |
| Noise | Up to 1% | Meningkatkan robustness terhadap noise kamera |
| *(tambahkan jika ada)* | | |

> Konfigurasi augmentasi lengkap dapat dilihat di dashboard Roboflow project `deteksi-sapi`.

---

## 6. Format Anotasi

Dataset menggunakan format anotasi **YOLOv4 (Darknet)** yang dihasilkan oleh Roboflow.

### Struktur File Anotasi

```
dataset/
├── train/
│   ├── images/
│   │   ├── img_001.jpg
│   │   └── ...
│   └── labels/
│       ├── img_001.txt    ← file anotasi per gambar
│       └── ...
├── valid/
│   ├── images/
│   └── labels/
├── test/
│   ├── images/
│   └── labels/
├── obj.data
├── obj.names
└── train.txt
```

### Format File Label (.txt)

Setiap baris dalam file `.txt` merepresentasikan satu bounding box:

```
<class_id> <x_center> <y_center> <width> <height>
```

Semua nilai dinormalisasi ke rentang 0–1 relatif terhadap dimensi gambar.

**Contoh isi file `img_001.txt`:**
```
0 0.512 0.483 0.321 0.287
1 0.748 0.612 0.198 0.175
```

### File `obj.names`
```
sehat
pink_eye
```

---

## 7. Dataset Split

Pembagian dataset dilakukan secara **stratified** (proporsional per kelas) untuk memastikan setiap split merepresentasikan distribusi kelas yang sama.

### Rasio Split

```
Total Dataset
├── 70% → Training Set   (digunakan untuk melatih bobot model)
├── 20% → Validation Set (digunakan untuk memantau overfitting selama training)
└── 10% → Test Set       (digunakan HANYA untuk evaluasi akhir model)
```

### Prinsip Pemisahan

- Gambar dari individu sapi yang sama tidak boleh tersebar di dua split berbeda (untuk menghindari data leakage)
- Test set tidak pernah digunakan selama proses training maupun tuning hyperparameter

---

## 8. Contoh Sampel Data

### Gambar Kelas `sehat`

*(Tambahkan screenshot atau deskripsi visual sampel gambar mata sapi sehat dari dataset)*

Karakteristik visual yang tampak:
- Kornea jernih, memantulkan cahaya
- Konjungtiva berwarna merah muda normal
- Tidak ada eksudat

### Gambar Kelas `pink_eye`

*(Tambahkan screenshot atau deskripsi visual sampel gambar mata sapi positif dari dataset)*

Karakteristik visual yang tampak:
- Kornea terlihat keruh / berwarna putih
- Mata terlihat merah dan berair
- Dalam kasus lanjut: terdapat ulkus kornea

---

## 9. Catatan & Keterbatasan Dataset

| Keterbatasan | Dampak | Mitigasi |
|---|---|---|
| Variasi ras sapi terbatas | Model mungkin kurang akurat pada ras sapi yang jarang ada di dataset | Perbanyak sampel dari berbagai ras |
| Kondisi cahaya didominasi outdoor | Akurasi menurun pada foto dengan cahaya sangat rendah (malam/dalam kandang gelap) | Tambahkan augmentasi brightness ekstrem |
| Ukuran dataset relatif kecil | Potensi overfitting pada kelas dengan sedikit sampel | Augmentasi agresif + transfer learning |
| Single angle (frontal) | Model kurang robust terhadap foto dari sudut ekstrem | Tambahkan sampel multi-angle |

---

*Dokumen ini merupakan bagian dari laporan skripsi penelitian BovineEye AI.*
*Universitas Darma Persada (UNSADA) — Program Studi S1 Teknologi Informasi*
*Peneliti: Fachri Ramdhan Al Mubaroq*
