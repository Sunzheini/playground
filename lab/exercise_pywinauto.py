from time import sleep

from pywinauto.application import Application
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard
import pyautogui


# exe_path = r"C:\Program Files\Notepad++\notepad++.exe"
exe_path = r"D:\Study\PLC\CODESYS 3.5.17.20\CODESYS\Common\CODESYS.exe"

app = Application(backend="uia")

try:
    app.start(exe_path)
except Exception as e:
    print("Error starting:", e)

main_window = app.top_window()
main_window.wait('visible', timeout=30)

# Print the control identifiers of the main window
main_window.print_control_identifiers()

"""
   |    | MenuItem - 'File'    (L0, T23, R32, B42)
   |    | ['FileMenuItem', 'MenuItem2', 'File']
   |    | child_window(title="File", control_type="MenuItem")
"""

sleep(1)
# puts the app window to focus (foreground)
main_window.set_focus()

# ---------------------------------------------------------------------------

# pyautogui.hotkey('alt', 'f')

# ---------------------------------------------------------------------------

# Click the "File" menu (assuming you have already defined 'main_window')
# file_menu = main_window.child_window(title="File", control_type="MenuItem")
# file_menu.click_input()

# ---------------------------------------------------------------------------

sleep(1)
# Click the "New" menu item (assuming you have already defined 'main_window')
main_window.type_keys("^n")
