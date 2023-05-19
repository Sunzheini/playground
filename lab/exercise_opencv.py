# Create a VideoCapture object to access the camera
import cv2
import pytesseract


# Create a VideoCapture object to access the camera
cap = cv2.VideoCapture(0)  # Use '0' for the default camera, or specify a different camera index if available

# Wait for a specific key press to capture the photo
while True:
    # Display the camera feed in a window
    ret, frame = cap.read()
    cv2.imshow('Camera Feed', frame)

    # Check for the key press event
    if cv2.waitKey(1) & 0xFF == ord('c'):  # Press 'c' key to capture the photo
        break

# Convert the frame to grayscale for better OCR accuracy
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Apply image preprocessing (optional)
# ...

# Perform OCR using Tesseract
text = pytesseract.image_to_string(gray)

# Display the extracted text
print("Extracted Text:", text)

# Create a window to display the photo
cv2.namedWindow('Captured Photo', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Captured Photo', 800, 600)

# Display the captured photo in the separate window
cv2.imshow('Captured Photo', frame)

# Wait for a key press to exit
cv2.waitKey(0)

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()



# ------------------------------------------------------------------------------

"""
Here's how you can run the code on your phone:

Install a Python distribution: Start by installing a Python distribution on your phone. 
One popular option is the Termux app for Android, which provides a terminal emulator and 
package manager to run Python on your phone. You can install Termux from the Google Play Store.

Install required packages: Once you have Termux installed, open the app and run the 
following commands to install Python and OpenCV:
pkg install python
pip install opencv-python

Run the Python code: Using a text editor on your phone, create a new Python file (e.g., 
camera_chatbot.py) and paste the code provided in the previous response. Save the file.

Execute the Python script: In Termux, navigate to the directory where you saved the 
Python file using the cd command. For example:
cd /path/to/your/file

Run the Python script:
python camera_chatbot.py

This will start the execution of the Python script, accessing the camera and displaying 
the frames on your phone.

Keep in mind that running resource-intensive tasks like camera processing on a phone may 
vary depending on the device's hardware capabilities. Some older or low-end phones might experience performance limitations. Additionally, ensure that you have the necessary permissions set up for the app to access your phone's camera.

Please note that the steps provided above are specific to running Python and OpenCV on an 
Android phone using the Termux app. If you're using a different phone operating system or 
development environment, the steps may differ.

"""