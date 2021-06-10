import tkinter as tk
from tkinter import ttk

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar=tk.Frame(bg='#d7d8e0',bd=2)
        toolbar.pack(side=tk.TOP,fill=tk.X)

        self.add_img=tk.PhotoImage(file='C:\Users\Faza\Desktop\python\register of new users and tkinter\hii.png')
        btn_open_dialog=tk.Button(toolbar,text='Whant go to Registration form? Click Here!',command=self.open_dialog,bg='#d7d8e0',bd=100,compound=tk.TOP,image=self.add_img)
        btn_open_dialog.pack(side=tk.BOTTOM)

        self.tree=ttk.Treeview(self,columns=('Full name','Passport ID','Types of hotel room','Status','Cost per day'),height=25,show='headings')
        self.tree.column('Full name',width=250,anchor=tk.CENTER)
        self.tree.column('Passport ID',width=200,anchor=tk.CENTER)
        self.tree.column('Types of hotel room',width=200,anchor=tk.CENTER)
        self.tree.column('Status',width=100,anchor=tk.CENTER)
        self.tree.column('Cost per day',width=200,anchor=tk.CENTER)
        
        self.tree.heading('Full name',text='Full name')
        self.tree.heading('Passport ID',text='Passport ID')
        self.tree.heading('Types of hotel room',text='Types of hotel room')
        self.tree.heading('Status',text='Status')
        self.tree.heading('Cost per day',text='Cost per day')
        self.tree.pack()

    def open_dialog(self):
        Child()

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Registration form')
        self.geometry('500x300+500+400')
        self.resizable(False,False)

        label_description=tk.Label(self,text='Full name')
        label_description.place(x=100,y=20)
        label_description1=tk.Label(self,text='Gender')
        label_description1.place(x=100,y=80)   
        label_description2=tk.Label(self,text='Passport ID')
        label_description2.place(x=100,y=50)      
        label_select=tk.Label(self,text='Types of room')
        label_select.place(x=100,y=110)
        label_sum=tk.Label(self,text='Floor number')
        label_sum.place(x=100,y=140)
        label_sum=tk.Label(self,text='With view to the')
        label_sum.place(x=100,y=170)
        label_sum=tk.Label(self,text='Available options')
        label_sum.place(x=100,y=200) 

        self.entry_description=ttk.Entry(self)
        self.entry_description.place(x=200,y=20)

        self.entry_description=ttk.Entry(self)
        self.entry_description.place(x=200,y=50)

        self.entry_money=ttk.Entry(self)
        self.entry_money.place(x=200,y=110)
        self.entry_money=ttk.Entry(self)
        self.entry_money.place(x=200,y=200)
        

        

        self.combobox=ttk.Combobox(self,values=[u'1',u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9',u'10'])
        self.combobox.current(0)
        self.combobox.place(x=200,y=140)

        self.combobox=ttk.Combobox(self,values=[u'male',u'female'])
        self.combobox.current(0)
        self.combobox.place(x=200,y=80)
        
        self.combobox=ttk.Combobox(self,values=[u'Single',u'Double ',u'Triple',u'Extra Bed',u'Child (Infant)'])
        self.combobox.current(0)
        self.combobox.place(x=200,y=110)

        self.combobox=ttk.Combobox(self,values=[u'Ocean',u'City',u'Gren-Garden park',u'none of above'])
        self.combobox.current(0)
        self.combobox.place(x=200,y=170)

        btn_cancel=ttk.Button(self,text='Cancel',command=self.destroy)
        btn_cancel.place(x=300,y=230)

        btn_select=ttk.Button(self,text='OK')
        btn_select.place(x=220,y=230)
        btn_select.bind('<Button-1>')

        self.grab_set()
        self.focus_set()

if __name__=="__main__":
    root=tk.Tk()
    app=Main(root)
    app.pack()
    root.title("Hi-tech Hotel")
    root.geometry("1000x750+600+500")
    root.resizable(False,False)
    root.mainloop()