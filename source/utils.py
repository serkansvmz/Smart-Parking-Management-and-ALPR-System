import pandas as pd
from datetime import datetime
import os
import json
from fast_plate_ocr import LicensePlateRecognizer

# Model yükleme
ocr_model = LicensePlateRecognizer('cct-xs-v1-global-model')

DB_FILE = 'parked_cars.json'
LOG_FILE = 'cars_log.csv'
HOURLY_RATE = 50.0  # Saatlik ücret (50₺)

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_db(db):
    with open(DB_FILE, 'w') as f:
        json.dump(db, f, indent=4)

def process_plate_fast(plate_roi):
    try:
        # OCR çalıştırma
        result = ocr_model.run([plate_roi])
        if not result: return None
        
        plate = result[0].plate.replace(" ", "").upper()
        db = load_db()
        now = datetime.now()
        time_str = now.strftime('%Y-%m-%d %H:%M:%S')

        # DURUM 1: Araç Zaten İçeride (ÇIKIŞ İŞLEMİ)
        if plate in db:
            entry_time_str = db[plate]
            entry_time = datetime.strptime(entry_time_str, '%Y-%m-%d %H:%M:%S')
            
            # Süre hesaplama
            duration = now - entry_time
            duration_minutes = duration.total_seconds() / 60
            
            # Ücret hesaplama
            fee = round((duration_minutes / 60) * HOURLY_RATE, 2)
            if fee < 20.0: fee = 20.0 # Minimum açılış ücreti (20₺)
            
            print(f"--- ÇIKIŞ YAPILIYOR: {plate} ---")
            print(f"Süre: {round(duration_minutes, 1)} Dakika")
            print(f"Ücret: {fee} ₺")
            
            # Kayıtlardan silme (Otoparktan çıktı)
            del db[plate]
            save_db(db)
            
            # Log dosyasına (CSV) ÇIKIŞ olarak kaydet
            save_to_log(plate, entry_time_str, time_str, fee)
            return f"{plate} | CIKIS | {fee} TL"

        # 🚀 DURUM 2: Araç Yeni Geliyor (GİRİŞ İŞLEMİ)
        else:
            db[plate] = time_str
            save_db(db)
            print(f"--- GİRİŞ YAPILDI: {plate} ---")
            print(f"Saat: {time_str}")
            return f"{plate} | GIRIS"

    except Exception as e:
        print("OCR HATA:", e)
        return None

def save_to_log(plate, entry, exit, fee):
    # Bu kısım tüm bitmiş işlemleri kalıcı olarak saklar
    df = pd.DataFrame([[plate, entry, exit, fee]], 
                     columns=['Plate', 'EntryTime', 'ExitTime', 'Fee'])
    df.to_csv(LOG_FILE, mode='a', header=not os.path.exists(LOG_FILE), index=False)