from tkinter import *  
from PIL import ImageTk,Image  
import os

root = Tk()

path_in = 'IMG20180826101431.jpg'
path_out = 'IMG20180826101906.jpg'
input_dir='input_dir/'
output_dir='output_dir/'
arr_in = os.listdir(input_dir)
arr_out = os.listdir(output_dir)
print(arr_in)
print(arr_out)


def next_btn():
	for nxt_img_in,nxt_img_out in arr_in,arr_out:
		path_in = nxt_img_in
		path_out = nxt_img_out


canvas_inp = Canvas(root, width = 350, height = 300)  
canvas_out = Canvas(root, width = 350, height = 300) 
canvas_thumb = Canvas(root,width = 350, height = 350)

btn1 = Button(root,text=">",command = next_btn)

in_label = Label(root,text = path_in)
out_label = Label(root,text  =path_out)





		

root.title("GUI")
root.geometry("900x500")
root.configure(background='grey')
# canvas_inp.pack(side="left")
# canvas_out.pack(side = "right")
size = 350,350
img_in = Image.open(path_in)
img_in.thumbnail(size)
# img_in = img_in.resize((250, 250), Image.ANTIALIAS) ## The (250, 250) is (height, width)
img_in = ImageTk.PhotoImage(img_in)
img_out = Image.open(path_out)
img_out.thumbnail(size)
# img_out = img_out.resize((250, 250), Image.ANTIALIAS) ## The (250, 250) is (height, width)
img_out= ImageTk.PhotoImage(img_out)


# canvas_inp.pack(side="left")
# canvas_thumb.pack(side="left")
# canvas_out.pack(side="left")
# btn1.pack(side="left")

canvas_inp.grid(row=1,column=0,sticky="W",padx=20)
#canvas_thumb.grid(row=0,column=1,columnspan=1)
canvas_out.grid(row=1,column=2,sticky="W",padx=20)
in_label.grid(row=0,column=0,pady = 10)
out_label.grid(row=0,column=2, pady =10)
btn1.grid(row=2,column=1)

canvas_inp.create_image(0, 0, anchor=NW, image=img_in) 
# canvas_thumb.create_image(50, 50, anchor=N, image=img_out)
canvas_out.create_image(0, 0, anchor=NW, image=img_out)

root.mainloop()