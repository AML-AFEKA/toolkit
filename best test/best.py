from ultralytics import YOLO
import glob

top10_predict = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
top10_image = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'] 

model = YOLO('best.pt')

images = glob.glob('*.jpg')
for image in images:
    result = model.predict(image)
    box = result[0].boxes
    
    if len(box.conf) < 1:
        continue
    
    predict = box.conf[0]
    
    for i in range(0, 10):
        if predict >= top10_predict[i]:
            top10_predict[i] = predict
            top10_image[i] = image
            
            print(f'({i})  {image} : {predict}')
            
            break
 
print("\n@@ result: @@\n")
for i in range(0, 10):
    print(f'({i})  {image} : {predict}')