import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from add_contact import AddContact

# connect to our mysql server
mydb = mysql.connector.connect(host='localhost',database='phonebook', user='ashish',password='Gmale@22mysql')
mycursor = mydb.cursor()



class UpdateContact(Toplevel):
    def __init__(self,person_id):
        Toplevel.__init__(self)
        self.geometry('650x650')
        self.title('Update Contact')
        self.resizable(False,False)

        self.person_id = person_id

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

        self.heading=Label(self.top_frame,text='Update Contact', font='Arial 15 bold', bg='white')
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


        self.get_person_details()
        # add contact button
        self.add_contact_btn=Button(self.bottom_frame,text='Update Contact',height=2,width=15,font='Arial 18',command=self.update_contact_func)
        self.add_contact_btn.place(x=200,y=380) 

    

    def get_person_details(self):

        mycursor.execute("SELECT * FROM contactbook WHERE person_id = "+str(self.person_id))
        result = mycursor.fetchall()
        result = result[0]

        self.name_entry.insert(0,result[1])
        self.phone_entry.insert(0,result[2])
        self.email_entry.insert(0,result[3])

        
    def update_contact_func(self):
        new_person_name=self.name_entry.get()
        new_person_phone=self.phone_entry.get()
        new_person_email=self.email_entry.get()

        if new_person_name and new_person_phone !="":
            query=("UPDATE contactbook SET person_name = %s, phone_number = %s, email = %s WHERE person_id = %s")

            mycursor.execute(query, (new_person_name, new_person_phone, new_person_email, self.person_id))
            mydb.commit()
            
            messagebox.showinfo('Success','Contact Updated')
            self.destroy()

        elif new_person_name =="":
            messagebox.showinfo('Warning','Please fill the name')
        else:
            messagebox.showinfo('Warning','Please fill the phone number')
