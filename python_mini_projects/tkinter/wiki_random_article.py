from tkinter import *
from tkinter import messagebox
import wikipedia
import requests
import json,time


class wikiRandom:
    def __init__(self,master):
        self.master=master

        self.master.config(bg='yellow')

        self.label=Label(self.master,text='Want to read a random article ?',font='Arial 24',width=40,height=5,bg='yellow')
        self.label.pack()

        self.btn=Button(self.master, text="Random Article", font='Arial 18',width=15, height=3,command=self.func)
        self.btn.pack()


    def func(self):
        obj=Article()


        


class Article(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        wiki_page=wikipedia.random(1)
        self.title(wiki_page)
        self.geometry("550x550")
        self.resizable(False, False)
        self.config(bg='brown')

        
        # wiki_page=wikipedia.random(1)
        wiki_load=wikipedia.page(wiki_page)
        self.scroll=Scrollbar(self,orient=VERTICAL)

        self.article=Text(self, width=50,height=25,)
        self.article.insert(END,wikipedia.summary(wiki_page))
        self.article.grid(row=0,column=0,padx=(40,0),pady=20, ipadx=20,sticky=N+S)

        self.scroll.config(command=self.article.yview)
        self.article.config(yscrollcommand=self.scroll.set)

        self.scroll.grid(row=0,column=1,pady=20,sticky=N+S)

        self.btn=Button(self, text='Exit',width=12,height=2, command=self.exit_func)
        self.btn.grid(row=1,column=0)


    def exit_func(self):
        self.destroy()

                



def main():
    root = Tk()
    app = wikiRandom(root)
    root.title("Wikipedia")
    root.geometry("550x550")
    root.resizable(False, False)
    root.mainloop()



if __name__ == '__main__':
    main()
    
