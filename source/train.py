from ultralytics import YOLO
import os

# 1. Modeli Yükle
# 'yolov8n.pt' (nano) hız için en iyisidir. 
# Eğer daha yüksek doğruluk istersen 'yolov8s.pt' (small) kullanabilirsin.
model = YOLO('yolov8n.pt') 

def train_model():
    # 2. Eğitimi Başlat
    # data: Roboflow'dan indirdiğin data.yaml dosyasının tam yolu
    # epochs: Modelin veriyi kaç kez baştan sona döneceği (100 idealdir)
    # imgsz: Giriş görüntü boyutu (640 standarttır)
    # device: Eğer ekran kartın varsa 0, yoksa 'cpu' yazabilirsin
    
    results = model.train(
        data='models/data.yaml',     # data.yaml dosyanın yolu
        epochs=100,                  # Eğitim tur sayısı
        imgsz=640,                   # Görüntü boyutu
        batch=16,                    # Her adımda işlenecek resim sayısı
        name='models',               # Kayıt klasörü adı
        device='cpu',                # Eğitim yapılacak donanım (cpu/0)
        patience=20,                 # 20 tur gelişme olmazsa eğitimi durdur (Early Stopping)
        optimizer='Adam'             # Öğrenme algoritması
    )

    print("Eğitim Tamamlandı!")

if __name__ == "__main__":
    train_model()