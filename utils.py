import cv2
import easyocr
import pandas as pd
from datetime import datetime
import os
import re
import json

reader = easyocr.Reader(['en'])

def clean_plate_text(text):
    return re.sub(r'[^A-Z0-9]', '', text.upper())

def check_authorization(plate_no):
    database_file = 'database.json'
    
    if not os.path.exists(database_file):
        print("database.json bulunamadı!")
        return "Bilinmeyen Araç (Veritabanı Yok)"

    with open(database_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        auth_list = data.get("authorized_vehicles", {})

    if plate_no in auth_list:
        return f"YETKİLİ: {auth_list[plate_no]}"
    else:
        return "YETKİSİZ ARAÇ"

def process_and_save(plate_roi):
    try:
        scale = 2
        plate_roi = cv2.resize(plate_roi, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
        gray = cv2.cvtColor(plate_roi, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        ocr_res = reader.readtext(thresh)
        if ocr_res:
            raw_text = ' '.join([res[1] for res in ocr_res])
            plate_no = clean_plate_text(raw_text)

            status = check_authorization(plate_no)
            print(f"--- OKUMA SONUCU ---")
            print(f"Plaka: {plate_no} | Durum: {status}")
            print(f"--------------------")

            file_name = 'cars_log.csv'
            time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            df = pd.DataFrame({'Plate': [plate_no], 'Status': [status], 'Time': [time_str]})
            df.to_csv(file_name, mode='a', header=not os.path.exists(file_name), index=False)
            
            return plate_no, status
    except Exception as e:
        print(f"Hata: {e}")
        return None, None