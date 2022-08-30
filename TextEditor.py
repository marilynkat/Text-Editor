#___________              __    ___________    .___.__  __                
#\__    ___/___ ___  ____/  |_  \_   _____/  __| _/|__|/  |_  ___________ 
#  |    |_/ __ \\  \/  /\   __\  |    __)_  / __ | |  \   __\/  _ \_  __ \
#  |    |\  ___/ >    <  |  |    |        \/ /_/ | |  ||  | (  <_> )  | \/
#  |____| \___  >__/\_ \ |__|   /_______  /\____ | |__||__|  \____/|__|    
                             
import tkinter
from tkinter.filedialog import askopenfilename
import os

#Set up GUI
text_editor = tkinter.Tk()
text_editor.title('Text Editor')

#GUI window dimensions
text_editor.geometry("350x350")

#Open file and display it's path and contents
def open_function():
    #Clear GUI for clean continuous use
    textbox.delete('1.0', tkinter.END)
    textbox2.delete('1.0', tkinter.END)

    #Pop up window to select file
    filename = askopenfilename()

    #Open, read, and save file contents
    file = open(filename)
    contents = file.read()

    #Display file name in top textbox
    textbox.insert(tkinter.END, filename)
    textbox.see(tkinter.END)

    #Display file contents in bottom textbox
    textbox2.insert(tkinter.END, contents)
    textbox2.see(tkinter.END)

#Overwrite old contents of file with new contents that are input in bottom textbox before 
#clicking save button
def save():
    #Save input from textbox to overwrite contents later
    input = textbox2.get("1.0","end-1c")

    #Save contents of top textbox to know file being edited
    filename = textbox.get("1.0","end-1c")

    #Open file in write mode
    file = open(filename, 'w+')

    #Set cursor to zeroth bytes
    file.seek(0, os.SEEK_SET)

    #Write input to file
    file.write(input)

#Close GUI window    
def close():
    text_editor.destroy()

#GUI components    
button = tkinter.Button(text_editor, text="Open", width=2, height=2, command=open_function)
textbox = tkinter.Text(height=3,width=21)
textbox2 = tkinter.Text(height=10,width=30)
button2 = tkinter.Button(text_editor, text="Save", width=5, height=2, command=save)
button3 = tkinter.Button(text_editor, text="Close", width=5, height=2, command=close)

#Placement of components in GUI
button.place(x=72,y=40)
textbox.place(x=130,y=40)
textbox2.place(x=72,y=100)
button2.place(x=90,y=250)
button3.place(x=180,y=250)

text_editor.mainloop()