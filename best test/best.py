import os
from ultralytics import YOLO
import glob

top10_predict_0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
top10_image_0 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'] 

top10_predict_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
top10_image_1 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'] 

model = YOLO('best.pt')

images = glob.glob('*.jpg')
for image in images:
    conf = f'{image.split(".")[0]}.text'
    
    if os.path.getsize(conf) < 1:
        continue
    
    f = open(conf, "r")
    typ = f.read()[0]
    
    result = model.predict(image)
    box = result[0].boxes
    
    if len(box.conf) < 1:
        continue
    
    predict = box.conf[0]
    
    for i in range(0, 10):
        if typ == '0' and predict >= top10_predict_0[i]:
            for j in range(i + 1, 10):
                top10_predict_0[j] = top10_predict_0[j - 1]
                top10_image_0[j] = top10_image_0[j - 1]
                
            top10_predict_0[i] = predict
            top10_image_0[i] = image
            
            print(f'({i})  {image} : {predict}')
            
            break
        
    for i in range(0, 10):
        if typ == '1' and predict >= top10_predict_1[i]:
            for j in range(i + 1, 10):
                top10_predict_1[j] = top10_predict_1[j - 1]
                top10_image_1[j] = top10_image_1[j - 1]
                
            top10_predict_1[i] = predict
            top10_image_1[i] = image
            
            print(f'({i})  {image} : {predict}')
            
            break
 
print("\n@@ result: @@\n")
print("\n 0 - \n")
for i in range(0, 10):
    print(f'({i})  {top10_image_0[i]} : {top10_predict_0[i]}')
    
print("\n 1 - \n")
for i in range(0, 10):
    print(f'({i})  {top10_image_1[i]} : {top10_predict_1[i]}')