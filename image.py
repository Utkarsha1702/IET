import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk
root=tk.Tk()
root.geometry("1000x600")
root.title("Image Editing Tool")
root.config(bg="white")

pen_color="black"
pen_size= 5
file_path= ""

def add_image():
    global file_path
    file_path=filedialog.askopenfilename(
        initialdir="D:\tkinter_image_editor")
    image= Image.open(file_path)
    width,height=int(image.width / 2),int(image.height / 2)
    image=image.resize((width,height), Image.ANTIALIAS)
    canvas.config(width=image.width,height=image.width)
    image=ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0,0,image=image,anchor="nw")


def draw(event):
    x1, y1 = (event.x - pen_size), (event.y-pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1,y1,x2,y2,fill=pen_color,outline='')

def change_color():
    global pen_color
    pen_color= colorchooser.askcolor(title="Select Pen Color")[1]

def change_size(size):
    global pen_size
    pen_size=size


def clear_canvas():
    canvas.delete("all")
    canvas.create_image(0,0, image=canvas.image, anchor="nw")

def apply_filter(filter):
    image=Image.open(file_path)
    width,height = int(image.width /2), int(image.height/2)
    image= image.resize((width,height),Image.ANTIALIAS)
    if filter== "black and White":
        image=ImageOps.grayscale(image)
    elif filter =="Blur":
        image= image.filter(ImageFilter.BLUR)
    elif filter =="Sharpen":
        image= image.filter(ImageFilter.SHARPEN)
    elif filter =="Smooth":
        image= image.filter(ImageFilter.SMOOTH)

    elif filter == "Emboss":
        image = image.filter(ImageFilter.EMBOSS)

    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")


left_frame= tk.Frame(root, width=400, height=600, bg="purple")
left_frame.pack(side="left",fill="y")

canvas=tk.Canvas(root, width=650, height=600)
canvas.pack()




image_button=tk.Button(left_frame,text="Add Image", command=add_image, bg="orange")
image_button.pack(pady=20)

color_button= tk.Button(left_frame,text="change pen color", command=change_color,bg="orange")
color_button.pack(pady=5)

pen_size_frame=tk.Frame(left_frame, bg="orange")
pen_size_frame.pack(pady=5)

pen_size_1 =tk.Radiobutton(
    pen_size_frame, text="Small", value=3,command=lambda: change_size(3),bg="orange")
pen_size_1.pack(side="left")

pen_size_2 =tk.Radiobutton(
    pen_size_frame, text="Medium", value=5,command=lambda: change_size(5), bg="orange")
pen_size_2.pack(side="left")
pen_size_2.select()

pen_size_3 =tk.Radiobutton(
    pen_size_frame, text="Large", value=7,command=lambda: change_size(7), bg="orange")
pen_size_3.pack(side="left")

clear_button =tk.Button(left_frame,text="clear", command=clear_canvas, bg="#FF9797")
clear_button.pack(pady=10)

filter_label=tk.Label(left_frame,text="Select Filter", bg="orange")
filter_label.pack()
filter_combobox= ttk.Combobox(left_frame, values=["black and White","blur","Emboss","Sharpen","Smooth"])
filter_combobox.pack()

filter_combobox.bind("<<ComboboxSelected>>", lambda event:apply_filter(filter_combobox.get()))


canvas.bind("<B1-Motion>",draw)

root.mainloop()