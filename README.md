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
```
```
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
Model, Roboflow üzerinden alınan veri seti ile YOLOv8 mimarisi kullanılarak eğitilmiştir. Modeli eğitmek için kullandığım veri setini aşağıdaki linkten inceleyebilirsiniz.
```
https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e
```

## 📷 Örnek Çıktılar

<img width="400" height="499" alt="image" src="https://github.com/user-attachments/assets/809f4b60-09d1-426e-855b-3a5ca1b619cb" />
<img width="350" height="785" alt="image" src="https://github.com/user-attachments/assets/4265bdcd-ff36-4c5a-b1de-ce0b27f65e84" />
               <img width="700" height="207" alt="image" src="https://github.com/user-attachments/assets/c5b22749-56ff-4a17-8fda-b94b0cfac6a2" />

# 📊 Proje Performans Analizi ve Çıktılar
Bu bölümde, modelin eğitim sürecindeki başarısı ve plaka tanıma sisteminin genel doğruluğu matematiksel verilerle sunulmuştur.

### 1. Nesne Tespit Performansı (YOLOv8)
**Modelin plaka yerini tespit etme başarısı aşağıdaki metriklerle ölçülmüştür:**

- mAP@50 (Mean Average Precision): 0.945 (%94.5)

Model, test verilerindeki plakaların %94.5'ini doğru kutu içine alabilmektedir.

- Precision (Kesinlik): 0.91

Modelin "bu bir plakadır" dediği durumların %91'i gerçekten plakadır.

- Recall (Duyarlılık): 0.89

Gerçek plakaların %89'u model tarafından yakalanmıştır.

### 2. Karakter Tanıma Başarısı (OCR)
**EasyOCR ve görüntü işleme (Thresholding/Cropping) sonrası elde edilen sonuçlar:**

- Karakter Bazlı Doğruluk (CWR): ~%88

- Tam Plaka Doğruluğu: ~%82

(Not: Gece çekimleri ve aşırı yansımalı plakalar bu oranı etkilemektedir.)

### 3. İşlem Süreleri (Latency)
**Sistemin CPU üzerindeki ortalama çalışma hızları (Intel i5/i7 İşlemci baz alınmıştır):**

- YOLOv8 Çıkarım (Inference): ~100ms - 150ms

- OCR İşleme Süresi: ~400ms - 600ms

- Toplam Tepki Süresi: < 1 Saniye

<img width="911" height="257" alt="image" src="https://github.com/user-attachments/assets/e50fe8ff-274a-4db6-a957-023631a2e624" />


- "Roboflow Health Check verilerine göre; veri setindeki sınıflar (License Plate) dengeli bir dağılım göstermektedir. Ortalama nesne boyutu 640x640 çözünürlükte optimize edilmiş olup, modelin küçük ve orta ölçekli plakaları yakalama kabiliyeti mAP değerleriyle desteklenmiştir."

<img width="456" height="814" alt="image" src="https://github.com/user-attachments/assets/cebe510f-9557-4001-ac80-966a7d8672a2" />
<img width="431" height="586" alt="image" src="https://github.com/user-attachments/assets/710cd7aa-17ff-41df-844e-81e4a113dfb9" />


