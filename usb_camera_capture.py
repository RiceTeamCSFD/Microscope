import cv2
import numpy as np
import matplotlib.pyplot as plt

# Connect to USB camera (CAP_DSHOW opens camera instantly, won't work on Mac)
camera = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# Set resolution to 1280x1024
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 2592)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1944)

ret, frame = camera.read()
print(ret)

# Continuously read frames until we close camera
while camera.isOpened():
    ret, frame = camera.read()

    # Create scale bar (based on calculations)
    frame[50:55, 30:209, :] = 0
    frame[50:62, 30:33, :] = 0
    frame[50:62, 209:212, :] = 0
    frame[50:59, 118:121, :] = 0
    
    # Add text
    font = cv2.FONT_HERSHEY_SIMPLEX 
    origin = (40, 45) 
    fontScale = 1.6
    color = (0, 0, 0)
    thickness = 2
    image = cv2.putText(frame, '20 um', origin, font,  
                    fontScale, color, thickness, cv2.LINE_AA)
    
    # Show live image
    cv2.imshow('Microscope USB Camera', frame)

    # Check if 'q' is pressed to capture image
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Whitebalance image
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        whitebalanced = (frame * 1.0 / frame.mean(axis=(0,1)))
        whitebalanced = whitebalanced.clip(0,1)

        # Show image
        fig, ax = plt.subplots(1, 2, figsize=(15,7))
        ax[0].imshow(frame)
        ax[0].set_title('Microscope Image')
        ax[0].axis(False)
        ax[1].imshow(whitebalanced)
        ax[1].set_title('Whitebalanced Image')
        ax[1].axis(False)
        plt.show()

        # Release the camera
        camera.release()

        # Destroy all windows
        cv2.destroyAllWindows()

        # Prompt user for file name
        im_name = input("Input name of image (including .jpg), or type NA : ")
        if im_name != 'NA':
            # Save images
            plt.imsave(im_name, frame)
            plt.imsave('WBed' + im_name, whitebalanced)

        break