import random
import khengool
from tkinter import *

root = Tk()
root.title("Lipbir - Password Generator")
root.iconbitmap("icon.ico")
root.geometry("500x300")



# Define New Rand Function
def new_rand ():
    # Clear Entry Box
    password_entry.delete(0, END)
    
    # Get Password Length
    password_length = int(my_entry.get())
    
    my_password = ""
    
    for i in range(password_length):
        my_password += chr(random.randint(33, 126))
        
    # Output Password
    password_entry.insert(0, my_password)
     

# Define Clipper Function
def clipper ():
    root.clipboard_clear()
    
    root.clipboard_append(password_entry.get())


# Label Frame
my_labelframe = LabelFrame(root, text = "How Many Characters Do You Need?")
my_labelframe.pack(pady = 20)

# Entry Box
my_entry = Entry(my_labelframe, font = ("Comic Sans MS", 24))
my_entry.pack(pady = 20, padx = 30)

# Entry Box To Return Password
password_entry = Entry(root, text = "", font = ("Console", 24), bd = 0, bg = "systembuttonface")
password_entry.pack(pady = 20)


# Buttons Frames
my_frame = Frame(root)
my_frame.pack(pady = 20)

# Buttons
my_buttons = Button(my_frame, text = "Generate Strong Password", command = new_rand)
my_buttons.grid(row = 0, column = 0, padx = 10)

# Clip Board
clip_button = Button(my_frame, text = "Copy To Clipboard", command = clipper)
clip_button.grid(row = 0, column = 1, padx = 10 )




root.mainloop()
