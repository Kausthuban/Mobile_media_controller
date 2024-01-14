import os
from tkinter import *
import subprocess
#Define the tkinter instance
root= Tk()
root.title("Rounded Button")
'''
#Define the size of the tkinter frame
win.geometry("700x300")

#Define the working of the button

def my_command():
   text.config(text= "You have clicked Me...")

#Import the image using PhotoImage function
prev= PhotoImage(file='prev.png')

#Let us create a label for button event
img_label= Label(image=prev)

#Let us create a dummy button and pass the image
button= Button(win, image=prev,command= my_command,
borderwidth=0)
button.pack(pady=30)

text= Label(win, text= "")
text.pack(pady=30)
'''
os.chdir('platform-tools')
result = subprocess.run(["adb","devices"], shell=True, capture_output=True, text=True)

if "device" in result.stdout:
    print("Device connected")
# print(result.stdout)
print(result.check_returncode())
print("\n\n",type(result))