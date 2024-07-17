import matplotlib.pyplot as plt
import numpy as np

from _data import data, title, cls

SIZE = 515

def find_max(_pred, _cls):
    predict = 0.0
    clss = _cls[0]
    
    for i in range(14):
        if _pred[i] > predict:
            predict = _pred[i]
            clss = _cls[i]
    
    return (predict, clss)  

truePositive = 0.0
falsePositive = 0.0
undetectPositive = 0.0

trueNagative = 0.0
falseNagative = 0.0
undetectNagative = 0.0

for i in range(SIZE):
    brightness = list(data[i].keys())
    predicts = list(data[i].values())
    
    max_predict = max(predicts)
    
    # fig, axs = plt.subplots(1, 2, figsize=(15, 10),sharey=True)
    
    # axs[0].bar(brightness, predicts)
    # axs[1].plot(brightness, predicts)

    # axs[0].fill_betweenx(predicts, 50, 0, facecolor='#aaa', alpha=.3)
    # axs[1].fill_betweenx(predicts, 50, 0, facecolor='#aaa', alpha=.3)

    # axs[0].axvline(50, color='yellow')
    # axs[1].axvline(50, color='yellow')
    
    
    # axs[0].axhline(predicts[4], color='red')
    # axs[1].axhline(predicts[4], color='red')

    # axs[0].set_xlabel('brightness')
    # axs[0].set_ylabel('predicts')

    # axs[1].set_xlabel('brightness')
    # axs[1].set_ylabel('predicts')
    
    # axs[1].set_title(max_predict, loc='center')

    # fig.suptitle(f'image: {title[i]}')

    # plt.ylim(min(predicts), max(predicts))

    # plt.show()
    
    
    _pred, _cls = find_max(predicts, cls[i])
    original_cls = list(_cls.keys())[0]
    predict_cls = list(_cls.values())[0]

    
    truePositive += 1 if original_cls == 1 and predict_cls == 1 else 0
    falsePositive += 1 if original_cls == 1 and predict_cls == 0 else 0
    undetectPositive += 1 if original_cls == 1 and predict_cls == -1 else 0
    
    trueNagative += 1 if original_cls == 0 and predict_cls == 0 else 0
    falseNagative += 1 if original_cls == 0 and predict_cls == 1 else 0
    undetectNagative += 1 if original_cls == 0 and predict_cls == -1 else 0
    
    trueNotExist = 100
    
    
accuracy = (truePositive + trueNagative + trueNotExist) / (truePositive + falsePositive + undetectPositive + trueNagative + falseNagative + undetectNagative + trueNotExist)

print("accuracy: ", accuracy*100)

vegetables = ["Positive", "Negative", "Not Exist"]
farmers = ["Positive", "Negative", "Not Exist"]

harvest = np.array([[truePositive, falsePositive, undetectPositive],
                    [falseNagative, trueNagative, undetectNagative],
                    [0,0,trueNotExist]])


fig, ax = plt.subplots()
im = ax.imshow(harvest)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(farmers)), labels=farmers)
ax.set_yticks(np.arange(len(vegetables)), labels=vegetables)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(vegetables)):
    for j in range(len(farmers)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Heatmap")
fig.tight_layout()
plt.show()