import cv2
import pyautogui
import time

# Activate the webcam and start preview
def activate_webcam():
    # Use the default webcam device
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame from camera")
            break
            
        cv2.imshow('Webcam Preview', frame)
        # Wait for a key press to stop the preview
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Run the webcam activation script when the link is opened
if __name__ == '__main__':
    print("Activating webcam...")
    activate_webcam()
