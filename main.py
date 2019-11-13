from tkinter import *
import tkinter
from tkinter.filedialog import askopenfilename
from tkinter import ttk, messagebox

from datetime import datetime as dt
from PIL import ImageTk, Image
import os

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
        file_path = str(askopenfilename(initialdir="/images", title="Select the image",
                                            filetypes=[("Image Files", "*.jpeg;*.jpg;*.png")]))
        self.secondW(file_path)
        # final_image(str(file_path))
        #messagebox.showerror("Error","Image was not selected")

    def mainW(self):
        #this is the first window which displays as soon as the program runs
        self.pictureB = ttk.Button(self.mainFrame, text="Select Picture", command=self.pictureSelect)
        self.pictureB.pack(padx=3,pady=3)
        
    def Dummy(self):
        print("Dummy called")
    
    def secondW(self,file_path):
        
        path_in = 'IMG20180826101431.jpg'
        path_out = 'IMG20180826101906.jpg'
        input_dir = 'images/Sample_Images/input/'
        output_dir = 'images/Sample_Images/output/'
        arr_in = os.listdir(input_dir)
        arr_out = os.listdir(output_dir)
        
        print("File path = ",file_path)
        self.processW=Toplevel()
        self.processW.title("GUI")
        self.processW.configure(background='grey')
        self.processW.geometry(WINDOW_SIZE)
        self.processW.resizable(10, 10)
        
        size = 350,350        
        img_in = Image.open(file_path)
        panel = Label(self.processW)
        panel.img=img_in
        print("img_in = ",img_in)
        # img_in.thumbnail(size)
        img_in = ImageTk.PhotoImage(img_in)
        
        print("img_in 2 = ",img_in)
        self.processB = Button(
            self.processW, text="Process", command=self.Dummy)
        # self.processB.grid(row=1, column=1,padx=3,pady=3)       
        
        canvas_inp = Canvas(self.processW, width = 350, height = 300) 
        canvas_out = Canvas(self.processW, width = 350, height = 300) 
        # self.canvas_thumb = Canvas(self.processW,width = 350, height = 350)
        # self.canvas_inp.grid(row=0,column=0,sticky="NW",padx=20)
        
        #self.canvas_out.grid(row=1,column=2,sticky="W",padx=20)
        
        canvas_inp.create_image(0, 0, anchor=NW, image=img_in)
        canvas_inp.pack(side="left")
        self.processB.pack(side="left")       
        self.processW.mainloop()
        
        
if __name__ == '__main__':
    MainClass()
