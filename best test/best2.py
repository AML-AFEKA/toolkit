# נניח שיש לנו 3 רשימות בגודל 57:
# title – רשימת שמות קבצים (מחרוזות)
# data – רשימת מילונים כאשר לכל קובץ יש מילון שממפה ספים (למשל 5, 10, 15, ...) לדיוק (float)
# cls – רשימת רשימות, כאשר עבור כל קובץ יש רשימה של 57 מילונים עם זוג {expected: predicted}

# לדוגמה, הקוד יעבוד כך:
from _data import data, title, cls
top_results = []

for i in range(len(title)):
    file_title = title[i]
    # מיון הספים לפי סדר עולה – חשוב שהסדר יתאים לסדר בערכי cls[i]
    thresholds = sorted(data[i].keys())
    
    best_acc = -1  # מתחילים בערך נמוך יותר מכל דיוק אפשרי (כי גם 0 יכול להיות דיוק תקין)
    best_thr = None
    
    # לעבור על כל סף והבדיקה האם התוצאה נכונה
    for j, thr in enumerate(thresholds):
        acc = data[i][thr]
        # cls[i][j] הוא מילון עם זוג אחד: {expected: predicted}
        d = cls[i][j]
        expected = list(d.keys())[0]
        predicted = list(d.values())[0]
        
        if expected == predicted:
            # אם התוצאה נכונה, נבדוק אם הדיוק גבוה יותר מהקודם ששמרנו
            if acc > best_acc:
                best_acc = acc
                best_thr = thr
    
    # שומרים tuple עם שם הקובץ, הדיוק הטוב ביותר והסף שבו הושג
    top_results.append((file_title, best_acc, best_thr))

# ממיינים את הקבצים לפי הדיוק (best_acc) מהגבוה לנמוך
top_results.sort(key=lambda x: x[1], reverse=True)

# בוחרים את 10 הקבצים עם הדיוק הטוב ביותר
top10 = [result[0] for result in top_results[:10]]

print("Top 10 file names with best accuracy and correct result:")
for file in top10:
    print(file)
