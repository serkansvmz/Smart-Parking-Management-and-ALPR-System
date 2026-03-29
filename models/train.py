from ultralytics import YOLO

model = YOLO('best.pt') 

model.train(
    data='models/data.yaml',
    epochs=100, 
    imgsz=640, 
    plots=True
)
