from flask import Flask, render_template, request, jsonify
from inference_sdk import InferenceHTTPClient
import cv2
import os
import uuid

app = Flask(__name__)

# ========================== KONFIGURASI ROBOFLOW SDK ==========================
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com", 
    api_key="IRGgjMXYUfluWDGC9raS"          
)
MODEL_ID = "deteksi-sapi/8"                

UPLOAD_FOLDER = 'static/results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    f = request.files.get("image")
    if not f:
        return jsonify({"error": "File tidak ditemukan"}), 400

    unique_filename = str(uuid.uuid4()) + ".jpg"
    input_path = os.path.join(UPLOAD_FOLDER, "in_" + unique_filename)
    f.save(input_path)

    try:
        result = CLIENT.infer(input_path, model_id=MODEL_ID)
        predictions = result.get('predictions', [])
        
        image = cv2.imread(input_path)
        max_score = 0
        is_positive = False
        info_list = [] # List untuk menampung poin-poin informasi tambahan

        # Analisis Prediksi
        if len(predictions) > 0:
            for pred in predictions:
                label = pred['class'].lower()
                conf = pred['confidence']
                
                x = int(pred['x'] - pred['width'] / 2)
                y = int(pred['y'] - pred['height'] / 2)
                w = int(pred['width'])
                h = int(pred['height'])

                if conf > max_score: max_score = conf
                
                # Cek Penyakit (Pastikan kata 'sehat' adalah nama class normal Anda)
                if "sehat" not in label:
                    is_positive = True
                
                color = (153, 72, 236) if "sehat" not in label else (0, 255, 0)
                cv2.rectangle(image, (x, y), (x + w, y + h), color, 3)
                cv2.putText(image, f"{label} {conf:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        # Logika Informasi Tambahan Berdasarkan Hasil
    # Logika Informasi Tambahan yang Lebih General
        if is_positive:
            status = "POSITIF PINK-EYE"
            stadium = "Terdeteksi Gejala Pink Eye"
            info_list = [
                {"label": "Status Diagnosa", "text": "Terdeteksi infeksi bakteri pada area mata sapi."},
                {"label": "Tindakan Pertama", "text": "Segera pisahkan (isolasi) sapi dari kawanan untuk mencegah penularan lewat lalat."},
                {"label": "Penyembuhan", "text": "Berikan salep mata antibiotik (seperti Oxytetracycline) dan bersihkan area mata dengan air hangat/larutan salin."},
                {"label": "Saran Lingkungan", "text": "Semprot area kandang dengan disinfektan untuk mengurangi populasi lalat pembawa bakteri."}
            ]
        else:
            status = "NEGATIF / SEHAT"
            stadium = "Kondisi Mata Normal"
            info_list = [
                {"label": "Status Diagnosa", "text": "Tidak ditemukan tanda-tanda infeksi bakteri Pink Eye."},
                {"label": "Tindakan Pencegahan", "text": "Jaga kebersihan sanitasi kandang secara rutin untuk mencegah timbulnya penyakit."},
                {"label": "Nutrisi Sapi", "text": "Pastikan sapi mendapatkan asupan Vitamin A yang cukup untuk menjaga ketahanan selaput mata."},
                {"label": "Monitoring", "text": "Lakukan pengecekan mata secara berkala terutama pada musim kemarau atau saat populasi lalat meningkat."}
            ]

        # Simpan Gambar
        result_filename = "res_" + unique_filename
        cv2.imwrite(os.path.join(UPLOAD_FOLDER, result_filename), image)

        return jsonify({
            "image_url": f"static/results/{result_filename}",
            "status": status,
            "confidence": f"{max_score * 100:.1f}%",
            "stadium": stadium,
            "info_tambahan": info_list # Mengirimkan array object
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)