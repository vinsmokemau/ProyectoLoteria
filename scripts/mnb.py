"""Number Recognizer."""
import cv2
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from skimage import io
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

webcam = cv2.VideoCapture(0)
check, frame = webcam.read()
cv2.imwrite(filename='saved_img.jpg', img=frame)
webcam.release()
cv2.destroyAllWindows()

image_saved = io.imread('saved_img.jpg')
gray_saved = rgb2gray(image_saved)
gray_saved = (gray_saved * 255) // 1
[rows_saved, columns_saved] = gray_saved.shape
for row in range(rows_saved):
    for column in range(columns_saved):
        if gray_saved[row, column] > 100:
            gray_saved[row, column] = 0
        else:
            gray_saved[row, column] = 255

number1 = gray_saved[20:65, 200:240]
number2 = gray_saved[20:65, 245:285]

plt.figure(2)
plt.imshow(number1, cmap='gray')
plt.figure(3)
plt.imshow(number2, cmap='gray')

data = []
labels = []

for i in range(12):
    for j in '0123456789':
        image_name = 'data/{}-{}.jpg'.format(i, j)
        image = io.imread(image_name)
        gray = rgb2gray(image)
        gray = (gray * 255) // 1
        [rows, columns] = gray.shape

        for row in range(rows):
            for column in range(columns):
                if gray[row, column] > 100:
                    gray[row, column] = 0
                else:
                    gray[row, column] = 255

        for k in range(100):
            data.append(gray.reshape(1800))
            labels.append(j)

data = np.array(data)
labels = np.array(labels)

clf = DecisionTreeClassifier()
clf.fit(data, labels)

test = np.array([number1.reshape(1800), number2.reshape(1800)])
predictions = clf.predict(test)

number = int(str(predictions[0]) + str(predictions[1]))

print(number)

plt.show()
