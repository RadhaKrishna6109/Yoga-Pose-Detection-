import os
from django.conf import settings
from pathlib import Path
import numpy as np
import skimage
from skimage.transform import resize
from sklearn.utils import Bunch
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,classification_report


def load_image_files(container_path, dimension=(104, 104,3)):
    image_dir = Path(container_path)
    folders = [directory for directory in image_dir.iterdir() if directory.is_dir()]
    categories = [fo.name for fo in folders]
    descr = "Yoga-Pose Detection"
    images = []
    flat_data = []
    target = []
    for i, direc in enumerate(folders):
        for file in direc.iterdir():
            print('file ----- ',file)
            # img = imageio.imread(file)
            img = skimage.io.imread(file)


            img_resized = resize(img, dimension, anti_aliasing=True, mode='reflect')
            flat_data.append(img_resized.flatten())
            images.append(img_resized)
            target.append(i)

    flat_data = np.array(flat_data)
    target = np.array(target)
    images = np.array(images)
    return Bunch(data=flat_data,
                target=target,
                target_names=categories,
                images=images,
                DESCR=descr)

path = settings.MEDIA_ROOT + "//" + "dataset_old"

image_dataset = load_image_files(path)  # Load here dataset
print(image_dataset.target_names)

X_train, X_test, y_train, y_test = train_test_split(image_dataset.data, image_dataset.target, test_size=0.3,
                                                random_state=109)
param_grid = [
    {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
    {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
]

print('X-Train')
print(X_train)


def RandomForest():
    
    from sklearn.ensemble import RandomForestClassifier
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)  

    rf_acc = accuracy_score(y_test,y_pred)
    rf_precision = precision_score(y_test,y_pred,average='weighted')
    rf_recall = recall_score(y_test,y_pred,average='weighted')
    rf_f1 = f1_score(y_test,y_pred,average='weighted')
    print('precision : ',rf_precision,'acc : ',rf_acc,'recall : ',rf_recall,'f1 : ',rf_f1)

    return rf_acc,rf_precision,rf_recall,rf_f1

def LogisticRegression():
    from sklearn.linear_model import LogisticRegression
    clf = LogisticRegression()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)  

    lr_acc = accuracy_score(y_test,y_pred)
    lr_precision = precision_score(y_test,y_pred,average='weighted')
    lr_recall = recall_score(y_test,y_pred,average='weighted')
    lr_f1 = f1_score(y_test,y_pred,average='weighted')
    print('precision : ',lr_precision,'acc : ',lr_acc,'recall : ',lr_recall,'f1 : ',lr_f1)

    return lr_acc,lr_precision,lr_recall,lr_f1

def SVM():
    from sklearn.svm import SVC
    clf = SVC()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)  

    svm_acc = accuracy_score(y_test,y_pred)
    svm_precision = precision_score(y_test,y_pred,average='weighted')
    svm_recall = recall_score(y_test,y_pred,average='weighted')
    svm_f1 = f1_score(y_test,y_pred,average='weighted')

    return svm_acc,svm_precision,svm_recall,svm_f1


def KNN():
    from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
    from matplotlib import pyplot as plt
    from sklearn.neighbors import KNeighborsClassifier  
    clf= KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2 ) 
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)  

    cm = confusion_matrix(y_test, y_pred)

# Plot confusion matrix
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Confusion matrix')
    plt.colorbar()
    tick_marks = np.arange(2)
    plt.xticks(tick_marks, ['Negative', 'Positive'], rotation=45)
    plt.yticks(tick_marks, ['Negative', 'Positive'])

    # Add text annotations
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, format(cm[i, j], 'd'),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
    knn_acc = accuracy_score(y_test,y_pred)
    knn_precision = precision_score(y_test,y_pred,average='weighted')
    knn_recall = recall_score(y_test,y_pred,average='weighted')
    knn_f1 = f1_score(y_test,y_pred,average='weighted')

    return knn_acc,knn_precision,knn_recall,knn_f1