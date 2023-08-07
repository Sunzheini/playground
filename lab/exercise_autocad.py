import win32com.client
import pythoncom
import time


# Start AutoCAD
Acad = win32com.client.Dispatch("AutoCAD.Application")

# Make the AutoCAD application visible
Acad.Visible = True

# Get the active document
doc = Acad.ActiveDocument

# Create a new circle
center = win32com\
    .client\
    .VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, [0, 0, 0])
radius = 10.0
circle = doc.ModelSpace.AddCircle(center, radius)

# Save the document to a file
doc.SaveAs("C:\\Users\\User\Desktop\\new.dwg")  # Replace with the desired file path

# Wait for 10 seconds
time.sleep(10)

# Close AutoCAD
Acad.Quit()
