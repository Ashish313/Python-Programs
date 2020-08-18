import mysql.connector
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
from my_contacts import MyContacts
from add_contact import AddContact

date=datetime.now().date()
date= str(date)

class Application:
    def __init__(self,master):
        self.master=master

        # frames
        self.top_frame=Frame(self.master, height=150,bg='white')
        self.top_frame.pack(fill=X)

        self.bottom_frame=Frame(self.master, height=500, bg='lightblue')
        self.bottom_frame.pack(fill=X)

        # frame design

        # top frame
        self.top_image=ImageTk.PhotoImage(Image.open('images/phone.png'))
        self.top_image_label=Label(self.master,image=self.top_image)
        self.top_image_label.place(x=130,y=20)

        self.heading=Label(self.top_frame,text='My Phonebook', font='Arial 15 bold', bg='white')
        self.heading.place(x=300,y=50)

        self.date_label=Label(self.top_frame,text='Date: '+date, font='arial 11',bg='white')
        self.date_label.place(x=510,y=10)


        # bottom frame

        # view contacts
        self.view_contacts=Button(self.bottom_frame,text='Contacts',font='Arial 14', width=25,height=5,command=self.my_contacts)
        self.view_contacts.place(x=200,y=50)

        # add contact
        self.add_contact=Button(self.bottom_frame,text='Add Contact',font='Arial 14', width=25,height=5,command=self.add_contact)
        self.add_contact.place(x=200,y=220)
        
        

    def my_contacts(self):
        contacts=MyContacts()
        

    def add_contact(self):
        new_contact=AddContact()



def main():
    root=Tk()
    app=Application(root)
    root.title('Phonebook')
    root.geometry('650x650')
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()