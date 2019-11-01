from datetime import datetime as dt

from tkinter import *
import tkinter
from tkinter.filedialog import askopenfilename
from tkinter import ttk, messagebox

WINDOW_SIZE="850x600"

class MainClass:
    def __init__(self):
        self.buttonHeight=20
        self.buttonWidth=50
        self.root = tkinter.Tk()
        self.root.title("Image Segmenter")
        self.root.geometry(WINDOW_SIZE)
        self.root.resizable(10,10)
        self.mainFrame=Frame(self.root,bg="#F5F5F5")
        self.mainFrame.pack_propagate(0)
        self.mainFrame.pack(fill="both",expand=1)
        self.mainW()
        self.root.mainloop()

    def pictureSelect(self):
        file_path = str(askopenfilename(initialdir="images/", title="Select the image",
                                            filetypes=[("Image Files", "*.jpeg;*.jpg;*.png")]))
        final_image(str(file_path))
        #messagebox.showerror("Error","Image was not selected")

    def mainW(self):
        #this is the first window which displays as soon as the program runs
        self.pictureB = ttk.Button(self.mainFrame, text="Select Picture", command=self.pictureSelect)
        self.pictureB.pack(padx=3,pady=3)


if __name__ == '__main__':
    MainClass()
