# Model Card — BovineEye AI (YOLOv4)

> Dokumen ini mengikuti standar **Model Card** (Mitchell et al., 2019) yang umum digunakan dalam publikasi AI/ML untuk transparansi dan akuntabilitas model.

---

## Table of Contents

1. [Identitas Model](#1-identitas-model)
2. [Intended Use](#2-intended-use)
3. [Arsitektur Model](#3-arsitektur-model)
4. [Training Details](#4-training-details)
5. [Evaluation Metrics](#5-evaluation-metrics)
6. [Performance Results](#6-performance-results)
7. [Confusion Matrix](#7-confusion-matrix)
8. [Per-Class Performance](#8-per-class-performance)
9. [Limitations & Bias](#9-limitations--bias)
10. [Ethical Considerations](#10-ethical-considerations)

---

## 1. Identitas Model

| Properti | Detail |
|---|---|
| **Nama Model** | BovineEye — Pink Eye Detector |
| **Versi** | v8 |
| **Algoritma** | YOLOv4 (You Only Look Once version 4) |
| **Task** | Object Detection (2-class) |
| **Platform Training** | Roboflow Cloud |
| **Model ID (Roboflow)** | `deteksi-sapi/8` |
| **Inference Endpoint** | `https://detect.roboflow.com` |
| **Tanggal Rilis** | *(diisi)* |
| **Peneliti** | Fachri Ramdhan Al Mubaroq |
| **Institusi** | Universitas Darma Persada (UNSADA) |

---

## 2. Intended Use

### Penggunaan yang Dimaksud

Model ini dirancang untuk **membantu deteksi dini** penyakit mata *Infectious Bovine Keratoconjunctivitis* (IBK / Pink Eye) pada sapi melalui analisis foto digital mata sapi.

**Target pengguna:** Peternak sapi, petugas kesehatan hewan, mahasiswa peternakan, dan tenaga medis hewan di lapangan.

**Use case utama:**
- Skrining awal kondisi mata sapi sebelum pemeriksaan dokter hewan
- Monitoring berkala kondisi kawanan sapi di peternakan
- Media edukasi visual tentang gejala Pink Eye

### Penggunaan yang BUKAN Dimaksud

- **Bukan pengganti diagnosis resmi dokter hewan** — output model adalah alat bantu, bukan keputusan medis final
- Tidak dirancang untuk mendeteksi penyakit mata sapi selain Pink Eye
- Tidak cocok untuk foto hewan selain sapi (tidak ada validasi lintas spesies)
- Tidak untuk keperluan medis kritis tanpa konfirmasi profesional

---

## 3. Arsitektur Model

### YOLOv4 Overview

YOLOv4 adalah arsitektur *single-stage object detector* yang memproses seluruh gambar dalam sekali *forward pass*, menghasilkan kecepatan inferensi tinggi dengan akurasi yang kompetitif.

```
Input Image (416×416×3)
        ↓
  CSPDarknet53 (Backbone)
  — Feature extraction menggunakan 53 layer conv
  — Cross Stage Partial connections untuk efisiensi
        ↓
  SPP + PAN (Neck)
  — Spatial Pyramid Pooling untuk multi-scale features
  — Path Aggregation Network untuk feature fusion
        ↓
  YOLOv4 Head (3 skala deteksi)
  — Large objects  : 13×13 grid
  — Medium objects : 26×26 grid
  — Small objects  : 52×52 grid
        ↓
  Output: Bounding Boxes + Class Scores + Confidence
```

### Komponen Utama YOLOv4

| Komponen | Detail |
|---|---|
| Backbone | CSPDarknet53 |
| Neck | SPP + PAN (Path Aggregation Network) |
| Head | YOLOv4 Detection Head |
| Activation | Mish (backbone), Leaky ReLU (neck/head) |
| Input Size | 416×416 piksel |
| Anchor Boxes | 9 anchor (3 per skala) |
| Loss Function | CIoU Loss (localization) + BCE (classification + objectness) |

### Keunggulan YOLOv4 untuk Kasus Ini

- **Kecepatan tinggi:** Cocok untuk inferensi *near real-time* di aplikasi web
- **Akurasi kompetitif:** mAP yang tinggi dibanding YOLO versi sebelumnya pada dataset kecil
- **Data augmentation terintegrasi:** Mosaic augmentation membantu performa pada dataset dengan jumlah gambar terbatas
- **Tersedia di Roboflow:** Memudahkan training dan deployment tanpa infrastruktur GPU lokal

---

## 4. Training Details

| Parameter | Nilai |
|---|---|
| Platform | Roboflow Cloud Training |
| Input Size | 416×416 piksel |
| Batch Size | *(diisi)* |
| Learning Rate | *(diisi)* |
| Epochs | *(diisi)* |
| Optimizer | SGD dengan momentum |
| Pretrained Weights | YOLOv4 COCO (transfer learning) |
| Training Duration | *(diisi jam/menit)* |
| Hardware (Roboflow) | GPU Cloud (spesifikasi dikelola Roboflow) |

### Transfer Learning

Model diinisialisasi dengan bobot pre-trained pada dataset **COCO** (Common Objects in Context) yang berisi 80 kelas umum. Transfer learning dari COCO membantu model lebih cepat konvergen meskipun dataset sapi relatif kecil, karena model sudah memiliki kemampuan ekstraksi fitur dasar (tepi, tekstur, bentuk).

---

## 5. Evaluation Metrics

### Definisi Metrik

**Precision (Presisi)**
```
Precision = TP / (TP + FP)
```
Dari semua prediksi positif model, berapa banyak yang benar-benar positif.

**Recall (Sensitivitas)**
```
Recall = TP / (TP + FN)
```
Dari semua kasus positif sebenarnya, berapa banyak yang berhasil terdeteksi model.

**mAP (mean Average Precision)**
```
mAP = rata-rata AP di semua kelas
AP  = area di bawah kurva Precision-Recall
```
Metrik utama untuk evaluasi model object detection. Dihitung pada threshold IoU = 0.50.

**IoU (Intersection over Union)**
```
IoU = Luas (Prediksi ∩ Ground Truth) / Luas (Prediksi ∪ Ground Truth)
```
Mengukur seberapa baik posisi bounding box prediksi dibandingkan anotasi sebenarnya.

**F1-Score**
```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```
Harmonic mean antara precision dan recall.

---

## 6. Performance Results

### Hasil Evaluasi pada Test Set

| Metrik | Nilai | Interpretasi |
|---|---|---|
| **mAP@0.50** | *(diisi)*% | Metrik utama — akurasi deteksi keseluruhan |
| **Precision** | *(diisi)*% | Tingkat ketepatan prediksi positif |
| **Recall** | *(diisi)*% | Tingkat kelengkapan deteksi kasus positif |
| **F1-Score** | *(diisi)*% | Keseimbangan precision dan recall |
| **Inference Speed** | *(diisi)* ms/gambar | Kecepatan inferensi per gambar |

### Interpretasi Nilai mAP

| Rentang mAP | Interpretasi |
|---|---|
| > 90% | Sangat Baik (Excellent) |
| 75% – 90% | Baik (Good) |
| 50% – 75% | Cukup (Acceptable) |
| < 50% | Kurang (Poor) |

### Training & Validation Loss Curve

*(Tambahkan grafik loss curve dari Roboflow atau tool training Anda)*

```
Loss
 │
 │\
 │ \
 │  \──────
 │         \────────────────
 │                           (konvergen)
 └────────────────────────── Epoch
   Training Loss ——
   Validation Loss - -
```

---

## 7. Confusion Matrix

*(Diisi setelah evaluasi selesai)*

```
                  Prediksi
                  Sehat    Pink Eye
Aktual  Sehat  [  TN  ] [  FP  ]
        Pink   [  FN  ] [  TP  ]
```

| | Prediksi: Sehat | Prediksi: Pink Eye |
|---|---|---|
| **Aktual: Sehat** | *(TN — diisi)* | *(FP — diisi)* |
| **Aktual: Pink Eye** | *(FN — diisi)* | *(TP — diisi)* |

### Analisis Confusion Matrix

**True Positive (TP):** Sapi positif Pink Eye yang berhasil terdeteksi → **Kritis, harus tinggi**

**False Negative (FN):** Sapi positif Pink Eye yang TIDAK terdeteksi → **Berbahaya** — sapi sakit tidak tertangani, risiko penularan

**False Positive (FP):** Sapi sehat yang salah terdeteksi sebagai positif → **Kurang ideal** — menyebabkan penanganan tidak perlu, tapi tidak berbahaya

**True Negative (TN):** Sapi sehat yang benar teridentifikasi sehat → baik

> Dalam konteks medis, **meminimalkan False Negative (FN) lebih diprioritaskan** daripada False Positive (FP), karena kegagalan mendeteksi penyakit lebih merugikan daripada over-diagnosis.

---

## 8. Per-Class Performance

| Kelas | Precision | Recall | F1-Score | AP@0.50 | Jumlah Sampel Test |
|---|---|---|---|---|---|
| `sehat` | *(diisi)*% | *(diisi)*% | *(diisi)*% | *(diisi)*% | *(diisi)* |
| `pink_eye` | *(diisi)*% | *(diisi)*% | *(diisi)*% | *(diisi)*% | *(diisi)* |
| **mAP (rata-rata)** | | | | *(diisi)*% | |

---

## 9. Limitations & Bias

### Keterbatasan Teknis

| Keterbatasan | Dampak |
|---|---|
| Model hanya mengenali 2 kelas | Tidak dapat membedakan stadium/tingkat keparahan Pink Eye |
| Performa menurun pada foto buram | Foto dengan motion blur atau out-of-focus menghasilkan confidence rendah |
| Bergantung pada koneksi internet | Tidak dapat beroperasi offline karena inferensi di Roboflow Cloud |
| Belum divalidasi lintas ras sapi | Performa mungkin berbeda pada ras sapi yang tidak ada di dataset training |

### Potensi Bias Dataset

| Jenis Bias | Keterangan |
|---|---|
| Geographic bias | Dataset mungkin didominasi sapi dari satu wilayah geografis |
| Lighting bias | Foto mayoritas diambil dalam kondisi cahaya tertentu |
| Angle bias | Dataset didominasi foto frontal; kurang foto dari sudut samping |
| Severity bias | Jika dataset lebih banyak mengandung kasus Pink Eye stadium lanjut, model mungkin kurang peka pada gejala awal |

---

## 10. Ethical Considerations

### Penggunaan Bertanggung Jawab

1. **Bukan pengganti dokter hewan** — Aplikasi ini adalah alat bantu skrining awal. Diagnosis akhir dan keputusan pengobatan harus tetap dilakukan oleh tenaga medis hewan berlisensi.

2. **Transparansi kepada pengguna** — Pengguna harus diberitahu bahwa sistem berbasis AI ini memiliki kemungkinan kesalahan (False Positive dan False Negative).

3. **Tidak untuk keputusan ekonomi besar** — Keputusan seperti penjualan atau penyembelihan sapi tidak boleh didasarkan semata-mata pada output aplikasi ini.

4. **Privasi data** — Gambar yang diunggah diproses di server dan disimpan sementara di folder `static/results/`. Tidak ada data yang dikirimkan ke pihak ketiga selain Roboflow untuk keperluan inferensi.

### Referensi

- Redmon, J., & Farhadi, A. (2018). YOLOv3: An Incremental Improvement. *arXiv:1804.02767*
- Bochkovskiy, A., Wang, C. Y., & Liao, H. Y. M. (2020). YOLOv4: Optimal Speed and Accuracy of Object Detection. *arXiv:2004.10934*
- Mitchell, M., et al. (2019). Model Cards for Model Reporting. *ACM FAT* Conference.

---

*Model Card ini merupakan bagian dari dokumentasi skripsi BovineEye AI.*
*Universitas Darma Persada (UNSADA) — Program Studi S1 Teknologi Informasi*
*Peneliti: Fachri Ramdhan Al Mubaroq*
