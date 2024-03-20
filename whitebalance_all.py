import os
import cv2
import matplotlib.pyplot as plt

folderPath = 'C:/Users/12546/Rice/Coding/Image Processing/Images for WB' # Edit to your path
imageFiles = [file for file in os.listdir(folderPath) if file.endswith('.png') or file.endswith('.jpg')] # Creates file
for i in range(len(imageFiles)):
    # Loops through each photo in the file and displays them
    filePath = os.path.join(folderPath, imageFiles[i])
    fileName = os.path.basename(filePath)

    img = cv2.imread(filePath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    whitebalanced = (img * 1.0 / img.mean(axis=(0,1)))
    #print(img.mean(axis=(0,1)))
    #whitebalanced = (img * 1.0 / (140.558, 131.065, 142.683))
    output_image = whitebalanced.clip(0,1)

    plt.imsave('WB' + fileName + '.jpg', output_image)