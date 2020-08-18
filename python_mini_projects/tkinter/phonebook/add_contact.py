import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
# from main import Application
# from my_contacts import MyContacts

# connect to our mysql server
mydb = mysql.connector.connect(host='localhost',database='phonebook', user='ashish',password='Gmale@22mysql')
mycursor = mydb.cursor()



class AddContact(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x650')
        self.title('Add Contact')
        self.resizable(False,False)

        # frames
        self.top_frame=Frame(self, height=150,bg='white')
        self.top_frame.pack(fill=X)

        self.bottom_frame=Frame(self, height=500, bg='yellow')
        self.bottom_frame.pack(fill=BOTH,expand=1)

        # frame design

        # top frame
        self.top_image=ImageTk.PhotoImage(Image.open('images/phone.png'))
        self.top_image_label=Label(self.top_frame,image=self.top_image)
        self.top_image_label.place(x=130,y=20)

        self.heading=Label(self.top_frame,text='Add Contact', font='Arial 15 bold', bg='white')
        self.heading.place(x=300,y=50)

        # bottom frame
        # add name
        self.name_label=Label(self.bottom_frame,text='Name              ',font='Arial 15' ,bg='yellow')
        self.name_label.grid(row=0,column=0,padx=(30,10),pady=40)

        self.name_entry=Entry(self.bottom_frame,width=50)
        self.name_entry.grid(row=0,column=1,padx=0,pady=40,ipady=6)

        # add phone number
        self.phone_label=Label(self.bottom_frame,text='Phone Number',font='Arial 15',bg='yellow')
        self.phone_label.grid(row=1,column=0,padx=(30,10),pady=40)

        self.phone_entry=Entry(self.bottom_frame,width=50)
        self.phone_entry.grid(row=1,column=1,padx=0,pady=40,ipady=6)

        # add email address
        self.email_label=Label(self.bottom_frame,text='Email              ',font='Arial 15' ,bg='yellow')
        self.email_label.grid(row=2,column=0,padx=(30,10),pady=40)

        self.email_entry=Entry(self.bottom_frame,width=50)
        self.email_entry.grid(row=2,column=1,padx=0,pady=40,ipady=6)


        # add contact button
        self.add_contact_btn=Button(self.bottom_frame,text='Add Contact',height=2,width=15,font='Arial 18',command=self.add_contact_func)
        self.add_contact_btn.place(x=200,y=380)            


    # add contact function
    def add_contact_func(self):
               
        new_person_name=self.name_entry.get()
        new_person_phone=self.phone_entry.get()
        new_person_email=self.email_entry.get()

        if new_person_name and new_person_phone !="":
            query=("INSERT INTO contactbook (person_name, phone_number, email) VALUES (%s,%s,%s)")

            mycursor.execute(query, (new_person_name,new_person_phone,new_person_email))
            mydb.commit()
            
            messagebox.showinfo('Success','Contact Added')
            self.destroy()

        elif new_person_name =="":
            messagebox.showinfo('Warning','Please fill the name')
        else:
            messagebox.showinfo('Warning','Please fill the phone number')
