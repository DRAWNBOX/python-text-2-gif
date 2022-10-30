from tkinter import *
from tkinter import filedialog
from extraFunction import make_frames, openfile


def drawGui():
    global window
    root = Tk()
    root.geometry("400x200")
    root.title('Text2Gif')
    window = Entry(root)
    window.pack()
    window.focus_set()
    process_text_button = Button(root,text='Enter your Sentence!',command=printtext)
    process_text_button.pack(side='top')
    choose_file_button = Button(root,text='choose a file!',command=fileLocation)
    choose_file_button.pack(side='bottom')
    root.mainloop()

def printtext():
    file_name = "custom"
    textinput = str(window.get()).split()
    images = []
    make_frames(images, textinput, file_name)

def fileLocation():
    file_path = (filedialog.askopenfilename())
    images = []
    file_info = openfile(file_path)

    make_frames(images, file_info[0], file_info[1])