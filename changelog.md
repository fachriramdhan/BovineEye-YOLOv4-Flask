# Changelog

All notable changes to **BovineEye AI** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] — 2025-06-01 (Initial Release)

### Added
- Single-page web application with Flask backend
- YOLOv4 object detection via Roboflow Cloud API (`deteksi-sapi/8`)
- OpenCV bounding box annotation on result images
- Dual-status classification: `POSITIF PINK-EYE` and `NEGATIF / SEHAT`
- Structured medical recommendations (4 points per status)
- Confidence score display with animated progress bar
- Dark Mode / Light Mode toggle with `localStorage` persistence
- Drag & drop image upload with UUID-based file naming
- Animated scan-line effect during inference
- Dynamic UI update without page reload (Fetch API)
- Railway deployment support with dynamic `PORT` environment variable
- Auto-creation of `static/results/` directory on startup

### Tech Stack (v1.0.0)
- Python 3.10+, Flask, inference-sdk, OpenCV
- Tailwind CSS (CDN), Font Awesome 6.4.2, Vanilla JavaScript

---

## [Unreleased] — Planned

### Planned — v1.1.0
- [ ] Auto-cleanup of result images older than 24 hours
- [ ] Environment variable support for `ROBOFLOW_API_KEY`
- [ ] Error handling UI (user-facing error messages)
- [ ] Mobile-responsive layout improvements

### Planned — v1.2.0
- [ ] User authentication (peternak login system)
- [ ] Detection history per user (SQLite)
- [ ] PDF report export per detection session

### Planned — v2.0.0
- [ ] Real-time camera / video stream support
- [ ] Offline mode with TFLite model
- [ ] Multi-disease classification (staging Pink Eye severity)
