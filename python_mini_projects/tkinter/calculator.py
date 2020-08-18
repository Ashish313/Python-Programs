import tkinter as tk 

window=tk.Tk()

window.geometry("385x390")
window.title("calculator")
window.resizable(False, False)              # fix the height and width of the window


def btn_clicked(item):
    global expression
    expression+=str(item)
    text_input.set(expression)

#row 1
def clear_clicked():
    global expression
    expression=""
    text_input.set("")


def equal_clicked():
    global expression
    try:
        result=str(eval(expression))
        text_input.set(result)
        expression=""
        
    except:
        expression=""


expression=""
text_input=tk.StringVar()


input_field=tk.Entry(window,textvariable=text_input,width=47)
input_field.place(height=100)
input_field.grid(columnspan=4,ipady=20,column=0,row=1)

clear_btn=tk.Button(window,text="C",width=33,height=3,command=clear_clicked,activeforeground='yellow',activebackground='red')
clear_btn.grid(columnspan=3,column=0,row=2)

divide=tk.Button(window,text="/",width=8,height=3,command=lambda: btn_clicked("/"),activeforeground='red',activebackground='yellow')
divide.grid(column=3,row=2)


#row 2
seven=tk.Button(window,text="7",width=8,height=3,command=lambda: btn_clicked(7),activeforeground='white',activebackground='black').grid(column=0,row=3)
eight=tk.Button(window,text="8",width=8,height=3,command=lambda: btn_clicked(8),activeforeground='white',activebackground='black').grid(column=1,row=3)
nine=tk.Button(window,text="9",width=8,height=3,command=lambda: btn_clicked(9),activeforeground='white',activebackground='black').grid(column=2,row=3)
multiply=tk.Button(window,text="*",width=8,height=3,command=lambda: btn_clicked("*"),activeforeground='red',activebackground='yellow').grid(column=3,row=3)

#row 3
four=tk.Button(window,text="4",width=8,height=3,command=lambda: btn_clicked(4),activeforeground='white',activebackground='black').grid(column=0,row=4)
five=tk.Button(window,text="5",width=8,height=3,command=lambda: btn_clicked(5),activeforeground='white',activebackground='black').grid(column=1,row=4)
six=tk.Button(window,text="6",width=8,height=3,command=lambda: btn_clicked(6),activeforeground='white',activebackground='black').grid(column=2,row=4)
minus=tk.Button(window,text="-",width=8,height=3,command=lambda: btn_clicked("-"),activeforeground='red',activebackground='yellow').grid(column=3,row=4)

#row 4
one=tk.Button(window,text="1",width=8,height=3,command=lambda: btn_clicked(1),activeforeground='white',activebackground='black').grid(column=0,row=5)
two=tk.Button(window,text="2",width=8,height=3,command=lambda: btn_clicked(2),activeforeground='white',activebackground='black').grid(column=1,row=5)
three=tk.Button(window,text="3",width=8,height=3,command=lambda: btn_clicked(3),activeforeground='white',activebackground='black').grid(column=2,row=5)
add=tk.Button(window,text="+",width=8,height=3,command=lambda: btn_clicked("+"),activeforeground='red',activebackground='yellow').grid(column=3,row=5)

#row 5
zero=tk.Button(window,text="0",width=20,height=3,command=lambda: btn_clicked(0),activeforeground='white',activebackground='black').grid(columnspan=2,column=0,row=6)
decimal=tk.Button(window,text=".",width=8,height=3,command=lambda: btn_clicked("."),activeforeground='white',activebackground='black').grid(column=2,row=6)
equal_btn=tk.Button(window,text="=",width=8,height=3,command=equal_clicked,activeforeground='red',activebackground='yellow').grid(column=3,row=6)

window.mainloop()