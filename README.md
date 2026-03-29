# 📝 Smart Parking and License Plate Recognition System (ALPR)
Bu proje, YOLOv8 nesne tespit algoritması ve EasyOCR kütüphanesi kullanılarak geliştirilmiş, yerel bir veritabanı (JSON) üzerinden yetki kontrolü yapan bir Plaka Tanıma Sistemi'dir.

## 🚀 Özellikler
- **Plaka Tespiti:** YOLOv8 modeli ile araç üzerindeki plaka bölgesini yüksek doğrulukla bulur.

- **Karakter Tanıma (OCR):** EasyOCR ile plaka üzerindeki metni dijital veriye dönüştürür.

- **Görüntü İşleme:** Plaka bölgesini netleştirmek için Adaptive Thresholding ve boyutlandırma tekniklerini kullanır.

- **Yetki Kontrolü:** Okunan plakayı database.json dosyasındaki kayıtlarla karşılaştırır.

- **Loglama:** Tüm giriş çıkışları tarih ve saat bilgisiyle parking_log.csv dosyasına kaydeder.

- **Görsel Geri Bildirim:** Yetkili araçlar için Yeşil, yetkisiz araçlar için Kırmızı çerçeve ile ekranda gösterim sağlar.

## 🛠️ Kurulum
- **Depoyu Klonlayın:**

```
   git clone https://github.com/serkansvmz/Smart-Parking-and-License-Plate-Recognition-System--ALPR.git
   cd ALPR-System
```

- **Gerekli Kütüphaneleri Kurun:**
(Python 3.12+ önerilir)

```
   pip install -r requirements.txt
```
- **Model Ağırlıklarını Kontrol Edin:**
models/best.pt dosyasının yerinde olduğundan emin olun.

## 💻 Kullanım
- Sistemi çalıştırmak için terminale şu komutu yazın:

```
   python main.py
```
- database.json içeriğini şu şekilde düzenleyerek kendi araçlarınızı ekleyebilirsiniz:

JSON
```
  {
      "authorized_vehicles": {
          "34LY9771": "Serkan Sevmez - Anadol",
          "61HK325": "Misafir - Seat"
      }
  }
  ```
  
## 📊 Eğitim (Training)
Model, [Roboflow] üzerinden alınan veri seti ile YOLOv8 mimarisi kullanılarak eğitilmiştir. Eğitim süreciyle ilgili detaylara models/train.py dosyasından ulaşabilirsiniz.

## 📷 Örnek Çıktılar
