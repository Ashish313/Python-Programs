import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from add_contact import AddContact
from update_contact import UpdateContact

# connect to our mysql server
mydb = mysql.connector.connect(host='localhost',database='phonebook', user='ashish',password='Gmale@22mysql')
mycursor = mydb.cursor()



class MyContacts(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x650')
        self.title('My Contacts')
        self.resizable(False,False)

        # frames
        self.top_frame=Frame(self, height=150,bg='white')
        self.top_frame.pack(fill=X)

        self.bottom_frame=Frame(self, height=500, bg='yellow')
        self.bottom_frame.pack(fill=X)

        # frame design

        # top frame
        self.top_image=ImageTk.PhotoImage(Image.open('images/phone.png'))
        self.top_image_label=Label(self.top_frame,image=self.top_image)
        self.top_image_label.place(x=130,y=20)

        self.heading=Label(self.top_frame,text='My Contacts', font='Arial 15 bold', bg='white')
        self.heading.place(x=300,y=50)

        # bottom frame
        self.v_scroll=Scrollbar(self.bottom_frame,orient=VERTICAL)
        self.h_scroll=Scrollbar(self.bottom_frame,orient=HORIZONTAL)
        

        self.listbox=Listbox(self.bottom_frame,width=55,height=27)
        self.listbox.grid(row=0,column=0,pady=0,sticky=N+S)

        # to move the listbox according to scroll
        self.v_scroll.config(command=self.listbox.yview)
        self.h_scroll.config(command=self.listbox.xview)

        self.listbox.config(yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set)


        self.v_scroll.grid(row=0, column=1, sticky=N+S)
        self.h_scroll.grid(row=1, column=0, sticky=W+E)

        
        # buttons
        # add contacts button
        self.add_contact=Button(self.bottom_frame, text='Add Contact',width=12, height=2,font='Arial 12', command=self.add_contact_func)
        self.add_contact.grid(row=0, column=2,padx=25, pady=50, sticky=N)

        # update contact button
        self.update_contact=Button(self.bottom_frame, text='Update Contact',width=12, height=2,font='Arial 12', command=self.update_contact_func)
        self.update_contact.grid(row=0, column=2,padx=25, pady=125, sticky=N)

        # delete contact button
        self.delete_contact=Button(self.bottom_frame, text='Delete Contact',width=12, height=2,font='Arial 12', command=self.delete_contact_func)
        self.delete_contact.grid(row=0, column=2,padx=25, pady=200, sticky=N)
        self.display_contacts()


    # inserting values to listbox
    def display_contacts(self):
        mycursor.execute('SELECT * FROM contactbook ORDER BY person_name')
        result = mycursor.fetchall()

        index = 0
        for record in result:
            output = str(record[0])+'.  '+record[1]+'  '+record[2]+'  '+record[3]
            self.listbox.insert(index, output)
            index += 1


    def add_contact_func(self):
        contact=AddContact()
        self.destroy()


    def update_contact_func(self):
        index = self.listbox.curselection() 
        person = self.listbox.get(index)
        person_id = person.split('.')[0] 

        contact = UpdateContact(person_id)
        self.destroy()
        

    def delete_contact_func(self):
        index = self.listbox.curselection() 
        person = self.listbox.get(index)
        person_id = person.split('.')[0]

        response = messagebox.askokcancel('Delete Contact','Are you sure you want to delete the contact?')
        if response:
            query="DELETE FROM contactbook WHERE person_id = "+str(person_id)
            mycursor.execute(query)
            mydb.commit()

            self.destroy()
        else:
            messagebox.showinfo('Warning','Please select the record you want to delete')

        
