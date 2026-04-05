import cv2
from ultralytics import YOLO
from utils import process_plate_fast

#YOLO model
model = YOLO('models/best.pt')


def run(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("❌ Image not found")
        return

    results = model(img, conf=0.4)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            #crop
            h, w = img.shape[:2]
            x1, y1 = max(0, x1), max(0, y1)
            x2, y2 = min(w, x2), min(h, y2)

            plate_crop = img[y1:y2, x1:x2]

            if plate_crop.size == 0:
                continue

            # OCR
            plate_text = process_plate_fast(plate_crop)

            if plate_text:
            # Gelen metin: "50SB787 | GIRIS" veya "50SB787 | CIKIS | 15.5 ₺"
                color = (0, 255, 0) if "GIRIŞ" in plate_text else (0, 165, 255) # Giriş Yeşil, Çıkış Turuncu
    
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
                cv2.putText(img, plate_text, (x1, y1 - 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    cv2.imshow("Sonuç", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run("images/car11.jpg")