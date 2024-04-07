import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image= cv2.imread('40x_bs_15sdecolorizer_aftersaf_endofvw.jpg')

# Perform white balancing
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_mean = image_rgb.astype(np.float32) * 1.0 / image_rgb.mean(axis=(0,1))
image_wb = np.clip(image_mean, 0, 1)  # Scale values to [0, 1] range

# Convert the image to grayscale for histogram calculation
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_wb_hsv = cv2.cvtColor((image_wb * 255).astype(np.uint8), cv2.COLOR_BGR2HSV)

# Calculate histogram
hist = cv2.calcHist([image_hsv], [0], None, [180], [0, 180])
hist_wb = cv2.calcHist([image_wb_hsv], [0], None, [180], [0, 180])

# Display original and white balanced images
plt.figure(figsize=(12, 6))

# Original image
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

# White balanced image
plt.subplot(2, 2, 2)
plt.imshow(image_wb)
plt.title('White Balanced Image')
plt.axis('off')

# Histogram of the original image
plt.subplot(2, 2, 3)
plt.plot(hist, color='black')
plt.title('Histogram (Original Image)')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Histogram of the white balanced image
plt.subplot(2, 2, 4)
plt.plot(hist_wb, color='black')
plt.title('Histogram (White Balanced Image)')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()