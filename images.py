from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images")

# Select an image to be put into a label object and placed on the screen
my_img1 = ImageTk.PhotoImage(Image.open("c:/img/henry.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("c:/img/harry.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("c:/img/boris.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("c:/img/ronaldo.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("c:/img/rooney.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


# Go to the next image
def next_img(image_number):
    global my_label
    global next
    global prev

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1], height=500, width=500)
    next = Button(root, text="next", command=lambda: next_img(image_number+1))
    prev = Button(root, text="prev", command=lambda: prev_img(image_number-1))

    if image_number == 5:
        next = Button(root, text="next", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    next.grid(row=1, column=2)
    prev.grid(row=1, column=0)
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


# Go to the previous image
def prev_img(image_number):
    global my_label
    global next
    global prev
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1], height=500, width=500)
    next = Button(root, text="next", command=lambda: next_img(image_number + 1))
    prev = Button(root, text="prev", command=lambda: prev_img(image_number - 1))

    if image_number == 1:
        prev = Button(root, text="prev", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    next.grid(row=1, column=2)
    prev.grid(row=1, column=0)
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


next = Button(root, text="next", command=lambda:next_img(2))
prev = Button(root, text="prev", command=prev_img, state=DISABLED)
exit = Button(root, text="Exit Program", command=root.quit)
next.grid(row=1, column=2)
prev.grid(row=1, column=0)
exit.grid(row=1, column=1, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
root.mainloop()
