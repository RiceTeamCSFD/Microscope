import cv2
import numpy as np
import matplotlib.pyplot as plt

# Connect to USB camera
camera = cv2.VideoCapture(1)
ret, frame = camera.read()
print(ret)
# Continuously read frames until we close camera
while camera.isOpened():
    ret, frame = camera.read()
    
    # Create scale bar (based on calculations)
    #frame[30:32, 30:74, :] = 0
    '''
    # Add text
    font = cv2.FONT_HERSHEY_SIMPLEX 
    origin = (50, 50) 
    fontScale = 1 
    color = (0, 0, 0)
    thickness = 1
    image = cv2.putText(frame, '20 um', origin, font,  
                    fontScale, color, thickness, cv2.LINE_AA)
    '''
    # Show live image
    cv2.imshow('Microscope USB Camera', frame)

    # Check if 'q' is pressed to capture image
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Whitebalance image
        whitebalanced = (frame * 1.0 / frame.mean(axis=(0,1)))
        whitebalanced = whitebalanced.clip(0,1)

        # Save images
        plt.imsave('Microscope Image.jpg', frame)
        plt.imsave('WBed Microscope Image.jpg', whitebalanced)

        # Show image
        fig, ax = plt.subplots(1, 2, figsize=(10,6))
        ax[0].imshow(frame)
        ax[0].set_title('Microscope Image')
        ax[0].axis(False)
        ax[1].imshow(whitebalanced)
        ax[1].set_title('Whitebalanced Image')
        ax[1].axis(False)
        plt.show()
        break

# Release the camera
camera.release()

# Destroy all windows
cv2.destroyAllWindows()