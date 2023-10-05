import time
import keyboard
from PyQt5 import QtWidgets ,QtGui
import pyperclip
import platform

if platform.system() == 'Darwin':  # Check if the current OS is Mac
    ctrlKey = 'command'
else:  # For other operating systems (e.g., Windows)
    ctrlKey =  'ctrl'


# Function to send email
def send_email(subject, recipient,speed):
    # Simulate sending email
    time.sleep(speed)  # Simulate sending delay

    # Press the compose key
    keyboard.press('c')  # Press 'c' to compose a new email
    time.sleep(speed)  # Wait for the compose window to open
    keyboard.release('c')
    # Fill in recipient
    pyperclip.copy(recipient) 
    time.sleep(speed) 
    keyboard.press(ctrlKey+'+v')  # Press 'Ctrl + V' to paste
    keyboard.release(ctrlKey+'+v')
    time.sleep(speed) 
    keyboard.press('tab')  # Move to the recipient field
    keyboard.release('tab') 
    # Fill in subject
    pyperclip.copy(subject) 
    time.sleep(speed) 
    keyboard.press(ctrlKey+'+v')  # Press 'Ctrl + V' to paste
    keyboard.release(ctrlKey+'+v')
    keyboard.press('tab')
    keyboard.release('tab') 

    time.sleep(speed) 

    # Send email
    keyboard.press(ctrlKey)
    keyboard.press('enter')  # Press 'Ctrl + Enter' to send the email
    time.sleep(speed)  # Wait for the email to be sent
    keyboard.release('enter')
    keyboard.release(ctrlKey)
    time.sleep(speed * 3)
    
# Create a Qt application
app = QtWidgets.QApplication([])

# Create a main window
window = QtWidgets.QWidget()
window.setWindowTitle("MailSys--21")

# Create UI elements
subject_label = QtWidgets.QLabel("Subject:")
subject_entry = QtWidgets.QLineEdit()
recipient_label = QtWidgets.QLabel("Recipients (one per line):")
recipient_entry = QtWidgets.QTextEdit()
speed_label = QtWidgets.QLabel("Delay b/w email:")
speed_combo = QtWidgets.QComboBox()  # Add a QComboBox for selecting speed
speed_combo.addItems([str(i) for i in range(1, 21)])  # Add items from 1 to 20
send_button = QtWidgets.QPushButton("Send Email")
ok_button = QtWidgets.QPushButton("Close")  

# Function to handle button click event
def send_button_click():
    subject = subject_entry.text()
    recipients = recipient_entry.toPlainText().split('\n') 
    speed = int(speed_combo.currentText())  
    msg_box = QtWidgets.QMessageBox()
    msg_box.setIcon(QtWidgets.QMessageBox.Information)
    msg_box.setWindowTitle("Email Ready")
    msg_box.setText("Press Ok and open gmail and press z Key")
    msg_box.exec_()
    keyboard.wait('z')
    for recipient in recipients:
        send_email(subject, recipient.strip() ,speed/10)
    ok_button.show()

# Function to handle "OK" button click event
def ok_button_click():
    # Close the application
    app.quit()

# Connect the "OK" button click event to the handler function
ok_button.clicked.connect(ok_button_click)

# Connect the button click event to the handler function
send_button.clicked.connect(send_button_click)

# Create a layout and add the UI elements
layout = QtWidgets.QVBoxLayout()
layout.addWidget(subject_label)
layout.addWidget(subject_entry)
layout.addWidget(recipient_label)
layout.addWidget(recipient_entry)
layout.addWidget(speed_label)
layout.addWidget(speed_combo)
layout.addWidget(send_button)
layout.addWidget(ok_button)  # Add the "OK" button to the layout
ok_button.hide()
# Set the layout for the main window
window.setLayout(layout)

# Show the main window
window.show()

# Start the Qt event loop
app.exec_()