from ultralytics import YOLO
import glob

model = YOLO('best.pt')

images = glob.glob('*.jpg')
for image in images:
    result = model.predict(image)
    box = result[0].boxes
    
    if len(box.conf) < 1:
        continue
    
    print(f'{image} : {box.conf[0]}')