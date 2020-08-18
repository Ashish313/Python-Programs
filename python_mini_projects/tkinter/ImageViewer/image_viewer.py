from tkinter import *
from PIL import ImageTk, Image
import os

window=Tk()

window.title('Pics')
window.resizable(False, False)
window.config(bg='lightblue')


my_images=[]
total_images = os.listdir('images/')
for i in total_images:
    img = ImageTk.PhotoImage(Image.open('images/'+i))
    my_images.append(img)



label=Label(window,image=my_images[0])
label.grid(column=0,row=0,columnspan=3,pady=50,padx=50)

status=Label(window,text=f"Image 1 of {len(my_images)}",bd=1,anchor=E,relief=SUNKEN)
status.grid(column=0,row=2,columnspan=3,sticky=W+E)

def back(img_number):
    global label
    global btn_forward
    global btn_back

    label.grid_forget()
    label=Label(window,image=my_images[img_number])
    btn_forward=Button(window,text=">>",width=6, height=2,bg='black',fg='white',command=lambda:forward(img_number+1))
    btn_back=Button(window,text="<<",width=6, height=2,bg='black',fg='white',command=lambda:back(img_number-1))

    if img_number==0:
        btn_back=Button(window,text="<<",width=6, height=2,bg='black',fg='white',state=DISABLED)

    status=Label(window,text=f"Image {img_number+1} of {len(my_images)}",bd=1,anchor=E,relief=SUNKEN)

    label.grid(column=0,row=0,columnspan=3,pady=50,padx=50)
    btn_back.grid(column=0,row=1)
    btn_forward.grid(column=2,row=1,pady=20)
    status.grid(column=0,row=2,columnspan=3,sticky=W+E)


def forward(img_number):
    global label
    global btn_forward
    global btn_back

    label.grid_forget()
    label=Label(window,image=my_images[img_number])
    btn_forward=Button(window,text=">>",width=6, height=2,bg='black',fg='white',command=lambda:forward(img_number+1))
    btn_back=Button(window,text="<<",width=6, height=2,bg='black',fg='white',command=lambda:back(img_number-1))

    if img_number==len(my_images)-1:
        btn_forward=Button(window,text=">>",width=6, height=2,bg='black',fg='white',state=DISABLED)

    status=Label(window,text=f"Image {img_number+1} of {len(my_images)}",bd=1,anchor=E,relief=SUNKEN)

    label.grid(column=0,row=0,columnspan=3,pady=50,padx=50)
    btn_back.grid(column=0,row=1)
    btn_forward.grid(column=2,row=1,pady=20)
    status.grid(column=0,row=2,columnspan=3,sticky=W+E)


btn_back=Button(window,text="<<",state=DISABLED,width=6, height=2,bg='black',fg='white',command=back)
btn_quit=Button(window,text='Quit',width=6, height=2,bg='black',fg='white',command=window.quit)
btn_forward=Button(window,text='>>',width=6, height=2,bg='black',fg='white',command=lambda: forward(1))

btn_back.grid(column=0,row=1)
btn_quit.grid(column=1,row=1)
btn_forward.grid(column=2,row=1,pady=20)

window.mainloop()