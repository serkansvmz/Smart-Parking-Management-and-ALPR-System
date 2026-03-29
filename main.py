import cv2
from ultralytics import YOLO
from utils import process_and_save

model = YOLO('models/best.pt')

def read_plate_from_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Hata: {image_path} bulunamadı!")
        return

    results = model(img, conf=0.5)
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            plate_crop = img[y1:y2, x1:x2]
            plate_text, status = process_and_save(plate_crop)

            if plate_text:
                #print(f"OKUNAN PLAKA: {plate_text} | DURUM: {status}")
                color = (0, 255, 0) if "YETKİLİ" in status else (0, 0, 255)
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
                cv2.putText(img, plate_text, (x1, y1-15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow('Plaka Tanima Sonucu', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    read_plate_from_image('car3.jpg')