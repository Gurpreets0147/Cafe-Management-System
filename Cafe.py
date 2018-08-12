

# This project is based upon 'cafe management system'
# Made by 'Gurpreet Singh'
# For any suggestion or help please contact on ' Gurpreets0147@gmail.com '



from tkinter import *
from datetime import *
dt=datetime.now()
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item
from pyinvoice.templates import SimpleInvoice
import webbrowser
import sqlite3
import pyqrcode
import os
curdir=os.getcwd()
os.chdir('{}{}\code\logo'.format(curdir[:3],curdir[3:]))
cur=os.getcwd()

class cafe:

    def __init__(self):

        self.root = Tk()
        self.root.title('Nieve Cafe')
        self.root.geometry('1300x730+40+10')
        self.root.wm_iconbitmap('nieve.ico')
        self.root.resizable(0, 0)
        self.home = ttk.Frame(self.root)
        self.pageone = ttk.Frame(self.root)
        self.pagetwo = ttk.Frame(self.root)
        self.pagethree = ttk.Frame(self.root)
        self.pagefour = ttk.Frame(self.root)
        self.pagefive = ttk.Frame(self.root)
        self.pagesix = ttk.Frame(self.root)
        self.pageseven = ttk.Frame(self.root)
        self.pageeight = ttk.Frame(self.root)
        self.pagenine = ttk.Frame(self.root)
        self.pageten = ttk.Frame(self.root)
        self.pageeleven = ttk.Frame(self.root)
        self.pagetwelve = ttk.Frame(self.root)
        self.pagethirteen = ttk.Frame(self.root)
        self.pagefourteen = ttk.Frame(self.root)
        self.pagefifteen = ttk.Frame(self.root)

        for self.frame in (self.home, self.pageone, self.pagetwo):
            self.frame.place(x=0, y=0)

        for self.mframe in (self.pagethree, self.pagefour,self.pagefive,
                            self.pagesix, self.pageseven, self.pageeight,
                            self.pagenine, self.pageten, self.pageeleven,
                            self.pagetwelve, self.pagethirteen ,self.pagefourteen ,self.pagefifteen):
            self.mframe.place(x=320, y=144)
        self.style = ttk.Style()
        self.login_screen()
        self.create_table()

    def create_table(self):

        conn = sqlite3.connect('cafe.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS NEW_USER (first_name TEXT NOT NULL ,'
                  ' last_name TEXT NOT NULL, username TEXT PRIMARY KEY NOT NULL, email TEXT NOT NULL,'
                  ' password TEXT NOT NULL, address TEXT NOT NULL, mobile_number INTEGER NOT NULL)')
        c.execute('CREATE TABLE IF NOT EXISTS ORDER_DETAILS (order_number INTEGER PRIMARY KEY ,'
                  ' items INTEGER , sub_total INTEGER , vat_tax INTEGER , total INTEGER)')
        c.execute('CREATE TABLE IF NOT EXISTS ORDER_ITEMS (order_number INTEGER , food_name TEXT,'
                  'food_type TEXT , food_price INTEGER , quantity INTEGER ,total INTEGER)')
        c.execute('CREATE TABLE IF NOT EXISTS FOOD_ITEMS (food_name TEXT NOT NULL,food_type TEXT NOT NULL,'
                  'food_price INTEGER NOT NULL )')


        c.close()
        conn.close()

############################################## LOGIN WINDOW ############################################################

    def login_screen(self):

        # page home
        self.home.tkraise()
        self.load = Image.open('login.png')
        self.logo = ImageTk.PhotoImage(self.load)
        self.label = Label(self.home, image=self.logo)
        self.label.image = self.logo
        self.label.pack()
        self.style.configure('TEntry', background='#bdbcbc')

        self.login_screen_user = ttk.Entry(self.home, width=37, font=('Arial', 9))
        self.login_screen_password = ttk.Entry(self.home, width=37, show='*', font=('Arial', 9))
        self.login_screen_user.place(x=514, y=435,height=24)
        self.login_screen_password.place(x=514, y=495,height=24)

        Button(self.home, text='Login', font=('Arial', 11),
               background='#00b3d5',foreground='black', relief=GROOVE, command=self.login).place(x=514, y=550,width=267,height=26)

    def login(self):

        if self.login_screen_user.get() == 'n':
            if self.login_screen_password.get() == 'n':
                self.login_screen_user.delete(0, 'end')
                self.login_screen_password.delete(0, 'end')
                self.admin_options()
            else:
                messagebox.showwarning('NIEVE CAFE', 'Invalid Username or Password')
                self.login_screen_user.delete(0, 'end')
                self.login_screen_password.delete(0, 'end')
        else:
            dbpassword = self.dbid()
            if self.login_screen_password.get() == dbpassword:
                self.user_options()
            elif self.error_message == 1 :
                messagebox.showwarning('NIEVE CAFE', 'Invalid Username or Password')
                self.login_screen_user.delete(0, 'end')
                self.login_screen_password.delete(0, 'end')

    def dbid(self):

        try:
            conn = sqlite3.connect('cafe.db')
            c = conn.cursor()
            c.execute("SELECT password FROM NEW_USER WHERE username= ? ", (self.login_screen_user.get(),))
            data = c.fetchone()
            c.close()
            conn.close()
            for i in data:
                password = i


        except:
            messagebox.showwarning('NIEVE CAFE', 'Invalid Username or Password')
            self.login_screen_user.delete(0, 'end')
            self.login_screen_password.delete(0, 'end')
            self.error_message = 0

        else:
            self.error_message = 1
            return password

############################################## ADMIN WINDOW ############################################################

    def admin_options(self):
        # page one
        self.pageone.tkraise()
        self.load1 = Image.open('admin.png')
        self.logo1 = ImageTk.PhotoImage(self.load1)
        self.label1 = Label(self.pageone, image=self.logo1)
        self.label1.image = self.logo1
        self.label1.pack()

        Button(self.pageone, width=18, text='Add Food Items',font=('Arial',12),foreground='white',
               background='black',relief=GROOVE,command=self.add_food_items).place(x=50,y=250)
        Button(self.pageone, width=18, text='Update Food Items', font=('Arial', 12), foreground='white',
               background='black', relief=GROOVE,command=self.update_food_items).place(x=50, y=300)
        Button(self.pageone, width=18, text='Remove Food Items', font=('Arial', 12), foreground='white',
               background='black', relief=GROOVE,command=self.remove_food_items).place(x=50, y=350)
        Button(self.pageone, width=18, text='Add New User', font=('Arial', 12), foreground='white',
               background='black', relief=GROOVE,command=self.add_new_user).place(x=50, y=400)
        Button(self.pageone, width=18, text='Remove User', font=('Arial', 12), foreground='white',
               background='black', relief=GROOVE,command=self.remove_user).place(x=50, y=450)
        Button(self.pageone, width=18, text='Total Sales', font=('Arial', 12), foreground='white',
               background='black', relief=GROOVE,command=self.total_sales).place(x=50, y=500)
        Button(self.pageone, width=20, text='Logout', font=('Arial', 10), foreground='black',
               background='white', relief=GROOVE,command=self.login_screen).place(x=50, y=650)

        #page three
        self.pagethree.tkraise()
        self.load1 = Image.open('welcome.png')
        self.logo1 = ImageTk.PhotoImage(self.load1)
        self.label1 = Label(self.pagethree, image=self.logo1)
        self.label1.image = self.logo1
        self.label1.grid(row=0,column=0)

    ################################################################################

    def add_food_items(self):
        # page four
        self.pagefour.tkraise()
        self.load1 = Image.open('add food items.png')
        self.logo1 = ImageTk.PhotoImage(self.load1)
        self.label1 = Label(self.pagefour, image=self.logo1)
        self.label1.image = self.logo1
        self.label1.grid(row=0,column=0)

        self.staff_var_type = StringVar()
        self.add_food_items_name=Entry(self.pagefour,font=('Arial',15),width=25)
        self.add_food_items_type = ttk.Combobox(self.pagefour,font=('Arial',15),
                                                textvariable=self.staff_var_type,
                                                values=('Veg', 'Non-Veg'))
        self.add_food_items_price = Entry(self.pagefour,font=('Arial',15),width=25)
        self.add_food_items_name.place(x=220,y=205)
        self.add_food_items_type.place(x=220, y=255,width=280)
        self.add_food_items_price.place(x=220, y=305)

        Button(self.pagefour, width=14, text='Submit', font=('Arial', 10), foreground='black',
               background='white', relief=GROOVE, command=self.add_food_items_submit).place(x=300, y=400)
        Button(self.pagefour, width=14, text='Clean', font=('Arial', 10), foreground='black',
               background='white', relief=GROOVE, command=self.add_food_items).place(x=440, y=400)

    def add_food_items_submit(self):
        try:
            name=self.add_food_items_name.get()
            type=self.add_food_items_type.get()
            if name=='':
                raise sqlite3.IntegrityError
            if type=='':
                raise sqlite3.IntegrityError
            price=int(self.add_food_items_price.get())
            conn = sqlite3.connect('cafe.db')
            c = conn.cursor()
            c.execute(" INSERT INTO FOOD_ITEMS (food_name,food_type,food_price) values(?,?,?)",
                      (name,type,price))
            conn.commit()
            c.close()
            conn.close()

            messagebox.showinfo(title='NIEVE CAFE', message='Food Added Submitted!')
            self.add_food_items()
        except sqlite3.IntegrityError:
            messagebox.showwarning('NIEVE CAFE', 'Invalid Input')
            self.add_food_items()

        except ValueError:
            messagebox.showwarning('NIEVE CAFE', 'Invalid Price')
            self.add_food_items()

    #################################################################################

    def update_food_items(self):
        # page five
        self.pagefive.tkraise()
        self.load1 = Image.open('update food items.png')
        self.logo1 = ImageTk.PhotoImage(self.load1)
        self.label1 = Label(self.pagefive, image=self.logo1)
        self.label1.image = self.logo1
        self.label1.grid(row=0,column=0)

        Button(self.pagefive,width=14, text='Submit', font=('Arial', 10), foreground='black',
               background='white', relief=GROOVE, command=self.update_food_items_submit).place(x=250, y=127)
        Button(self.pagefive, width=14, text='Reset', font=('Arial', 8), foreground='black',
               background='white', relief=GROOVE, command=self.update_food_items).place(x=453, y=410)
        Button(self.pagefive, width=14, text='Update', font=('Arial', 8), foreground='black',
               background='white', relief=GROOVE, command=self.update_food_items_update).place(x=340, y=410)


        self.update_food_items_name = ttk.Entry(self.pagefive, width=20, font=('Arial', 12))
        self.update_food_items_type = ttk.Entry(self.pagefive, width=20, font=('Arial', 12))
        self.update_food_items_price = ttk.Entry(self.pagefive, width=20, font=('Arial', 12))
        self.update_food_items_new_price = Entry(self.pagefive, width=20, font=('Arial', 12))
        self.update_food_items_name.place(x=350,y=225)
        self.update_food_items_type.place(x=350,y=266)
        self.update_food_items_price.place(x=350,y=306)
        self.update_food_items_new_price.place(x=350, y=348)

        self.update_food_items_temp=Entry(self.pagefive,width=17,font=('Arial',12))
        self.update_food_items_temp.place(x=50,y=130)
        self.update_food_items_list = Listbox(self.pagefive, selectmode=SINGLE, height=20, width=25)
        self.update_food_items_list.place(x=50, y=170)
        self.update_food_items_scroll = Scrollbar(self.pagefive, orient=VERTICAL)
        self.update_food_items_list.configure(yscrollcommand=self.update_food_items_scroll.set)
        self.update_food_items_scroll.configure(command=self.update_food_items_list.yview)
        self.update_food_items_scroll.place(x=190, y=170, height=324)

        conn = sqlite3.connect('cafe.db')
        c = conn.cursor()
        c.execute("SELECT food_name FROM FOOD_ITEMS")
        data = c.fetchall()
        for i in data:
            self.update_food_items_list.insert(END, '{}'.format(i[0]))

        c.close()
        conn.close()

        self.update_food_items_list.bind('<<ListboxSelect>>', self.update_food_items_click)

    def update_food_items_click(self, event):
        self.update_food_items_temp.delete(0, END)
        index = self.update_food_items_list.curselection()
        self.update_food_items_temp.insert(0, self.update_food_items_list.get(index))

    def update_food_items_submit(self):
        self.update_food_items_name.insert(END,self.update_food_items_temp.get())
        self.update_food_items_name.state(['disabled'])
        conn = sqlite3.connect('cafe.db')
        c = conn.cursor()
        c.execute('SELECT food_type FROM FOOD_ITEMS WHERE food_name = ?', (self.update_food_items_temp.get(),))
        data = c.fetchone()
        for i in data:
            self.update_food_items_type.insert(END, '{}'.format(i))
        self.update_food_items_type.state(['disabled'])

        c.execute('SELECT food_price FROM FOOD_ITEMS WHERE food_name = ?', (self.update_food_items_temp.get(),))
        data = c.fetchone()
        for i in data:
            self.update_food_items_price.insert(END, '{}'.format(i))
        self.update_food_items_price.state(['disabled'])
        c.close()
        conn.close()

    def update_food_items_update(self):
        try:
            new_price=int(self.update_food_items_new_price.get())
            conn = sqlite3.connect('cafe.db')
            c = conn.cursor()
            c.execute(" UPDATE FOOD_ITEMS SET food_price = ? WHERE food_name = ?", (new_price,self.update_food_items_temp.get(),))

            conn.commit()
            c.close()
            conn.close()
            messagebox.showinfo(title='NIEVE CAFE', message='Price Updated Submitted!')
            self.update_food_items()
        except:
            messagebox.showwarning('NIEVE CAFE', 'Invalid Price')
            self.update_food_items()

    ##################################################################################

    def remove_food_items(self):
        # page six
        self.pagesix.tkraise()
        self.load1 = Image.open('remove food items.png')
        self.logo1 = ImageTk.PhotoImage(self.load1)
        self.label1 = Label(self.pagesix, image=self.logo1)
        self.label1.image = self.logo1
        self.label1.grid(row=0,column=0)

        Button(self.pagesix, width=14, text='Submit', font=('Arial', 10), foreground='black',
               background='white', relief=GROOVE, command=self.remove_food_items_submit).place(x=250, y=127)
        Button(self.pagesix, width=14, text='Reset', font=('Arial', 8), foreground='black',
               background='white', relief=GROOVE, command=self.remove_food_items).place(x=453, y=380)
        Button(self.pagesix, width=14, text='Remove', font=('Arial', 8), foreground='black',
               background='white', relief=GROOVE, command=self.remove_food_items_remove).place(x=340, y=380)

        self.remove_food_items_name = ttk.Entry(self.pagesix, width=20, font=('Arial', 12))
        self.remove_food_items_type = ttk.Entry(self.pagesix, width=20, font=('Arial', 12))
        self.remove_food_items_price = ttk.Entry(self.pagesix, width=20, font=('Arial', 12))
        self.remove_food_items_name.place(x=350, y=225)
        self.remove_food_items_type.place(x=350, y=266)
        self.remove_food_items_price.place(x=350, y=306)

        self.remove_food_items_temp = Entry(self.pagesix, width=17, font=('Arial', 12))
        self.remove_food_items_temp.place(x=50, y=130)
        self.remove_food_items_list = Listbox(self.pagesix, selectmode=SINGLE, height=20, width=25)
        self.remove_food_items_list.place(x=50, y=170)
        self.remove_food_items_scroll = Scrollbar(self.pagesix, orient=VERTICAL)
        self.remove_food_items_list.configure(yscrollcommand=self.remove_food_items_scroll.set)
        self.remove_food_items_scroll.configure(command=self.remove_food_items_list.yview)
        self.remove_food_items_scroll.place(x=190, y=170, height=324)

        conn = sqlite3.connect('cafe.db')
        c = conn.cursor()
        c.execute("SELECT food_name FROM FOOD_ITEMS")
        data = c.fetchall()
        for i in data:
            self.remove_food_items_list.insert(END, '{}'.format(i[0]))

        c.close()
        conn.close()

        self.remove_food_items_list.bind('<<ListboxSelect>>', self.remove_food_items_click)

    def remove_food_items_click(self, event):
        self.remove_food_items_temp.delete(0, END)
        index = self.remove_food_items_list.curselection()

        self.remove_food_items_temp.insert(0, self.remove_food_items_list.get(index))

    def remove_food_items_submit(self):
        self.remove_food_items_name.insert(END, self.remove_food_items_temp.get())
        self.remove_food_items_name.state(['disabled'])
        conn = sqlite3.connect('cafe.db')
        c = conn.cursor()
        c.execute('SELECT food_type FROM FOOD_ITEMS WHERE food_name = ?', (self.remove_food_items_temp.get(),))
        data = c.fetchone()
        for i in data:
            self.remove_food_items_type.insert(END, '{}'.format(i))
        self.remove_food_items_type.state(['disabled'])

        c.execute('SELECT food_price FROM FOOD_ITEMS WHERE food_name = ?', (self.remove_food_items_temp.get(),))
        data = c.fetchone()
        for i in data:
            self.remove_food_items_price.insert(END, '{}'.format(i))
        self.remove_food_items_price.state(['disabled'])
        c.close()
        conn.close()

    def remove_food_items_remove(self):
        conn = sqlite3.connect('cafe.db')
        c = conn.cursor()
        c.execute("DELETE FROM FOOD_ITEMS WHERE food_name = ? ",(self.remove_food_items_temp.get(),))
        conn.commit()
        c.close()
        conn.close()
        messagebox.showinfo(title='NIEVE CAFE', message='Food Remove Submitted!')
        self.remove_food_items()

    ###################################################################################

    def add_new_user(self):
        # page seven
        self.pageseven.tkraise()
        self.load1 = Image.open('add new user.png')
        self.logo1 = ImageTk.PhotoImage(self.load1)
        self.label1 = Label(self.pageseven, image=self.logo1)
        self.label1.image = self.logo1
        self.label1.grid(row=0,column=0)

        self.add_new_user_first_name = ttk.Entry(self.pageseven, width=26, font=('Arial', 14), foreground='#181817')
        self.add_new_user_last_name = ttk.Entry(self.pageseven, width=26, font=('Arial', 14), foreground='#181817')
        self.add_new_user_username = ttk.Entry(self.pageseven, width=26, font=('Arial', 14), foreground='#181817')
        self.add_new_user_email = ttk.Entry(self.pageseven, width=26, font=('Arial', 14), foreground='#181817')
        self.add_new_user_password = ttk.Entry(self.pageseven, width=26, font=('Arial', 14), show='*', foreground='#181817')
        self.add_new_user_address = ttk.Entry(self.pageseven, width=26, font=('Arial', 14), foreground='#181817')
        self.add_new_user_mobileno = ttk.Entry(self.pageseven, width=26, font=('Arial', 14), foreground='#181817')

        self.add_new_user_first_name.place(x=290, y=132)
        self.add_new_user_last_name.place(x=290, y=172)
        self.add_new_user_username.place(x=290, y=212)
        self.add_new_user_email.place(x=290, y=252)
        self.add_new_user_password.place(x=290, y=292)
        self.add_new_user_address.place(x=290, y=332)
        self.add_new_user_mobileno.place(x=290, y=372)

        Button(self.pageseven, width=14, text='Submit', relief=GROOVE, font=('Arial', 10),
               command=self.add_new_use_submit).place(x=300, y=440)
        Button(self.pageseven, width=14, text='Clean', relief=GROOVE, font=('Arial', 10),
               command=self.add_new_user).place(x=450, y=440)

    def add_new_use_submit(self):
        try:
            conn = sqlite3.connect('cafe.db')
            c = conn.cursor()
            first_name = self.add_new_user_first_name.get()
            last_name = self.add_new_user_last_name.get()
            username = self.add_new_user_username.get()
            email = self.add_new_user_email.get()
            password = self.add_new_user_password.get()
            address = self.add_new_user_address.get()
            mobile_number = int(self.add_new_user_mobileno.get())

            c.execute(
                " INSERT INTO NEW_USER (first_name,last_name,username,email,password,address,mobile_number) VALUES (?,?,?,?,?,?,?)",
                (first_name, last_name, username, email, password, address, mobile_number,))
            conn.commit()
            c.close()
            conn.close()

            messagebox.showinfo(title='New User', message='User Create Submitted!')


        except sqlite3.IntegrityError:

            messagebox.showwarning('ERROR', 'Username is already created')

            self.add_new_user_first_name.delete(0, 'end')
            self.add_new_user_last_name.delete(0, 'end')
            self.add_new_user_username.delete(0, 'end')
            self.add_new_user_email.delete(0, 'end')
            self.add_new_user_password.delete(0, 'end')
            self.add_new_user_address.delete(0, 'end')
            self.add_new_user_mobileno.delete(0, 'end')

        except:

            messagebox.showwarning('ERROR', 'Invalid Input')

            self.add_new_user_first_name.delete(0, 'end')
            self.add_new_user_last_name.delete(0, 'end')
            self.add_new_user_username.delete(0, 'end')
            self.add_new_user_email.delete(0, 'end')
            self.add_new_user_password.delete(0, 'end')
            self.add_new_user_address.delete(0, 'end')
            self.add_new_user_mobileno.delete(0, 'end')

        else:

            self.add_new_user_first_name.delete(0, 'end')
            self.add_new_user_last_name.delete(0, 'end')
            self.add_new_user_username.delete(0, 'end')
            self.add_new_user_email.delete(0, 'end')
            self.add_new_user_password.delete(0, 'end')
            self.add_new_user_address.delete(0, 'end')
            self.add_new_user_mobileno.delete(0, 'end')

    ####################################################################################

    def remove_user(self):
        # page eight
        self.pageeight.tkraise()
        self.load1 = Image.open('remove user.png')
        self.logo1 = ImageTk.PhotoImage(self.load1)
        self.label1 = Label(self.pageeight, image=self.logo1)
        self.label1.image = self.logo1
        self.label1.grid(row=0,column=0)

        Button(self.pageeight, width=14, text='Submit', font=('Arial', 9), foreground='black',
               background='white', relief=GROOVE, command=self.remove_user_submit).place(x=230, y=128)
        Button(self.pageeight, width=14, text='Reset', font=('Arial', 9), foreground='black',
               background='white', relief=GROOVE, command=self.remove_user).place(x=350, y=460)
        Button(self.pageeight, width=14, text='Remove', font=('Arial', 9), foreground='black',
               background='white', relief=GROOVE, command=self.remove_user_remove).place(x=480, y=460)

        self.remove_user_first_name = ttk.Entry(self.pageeight, width=26, font=('Arial', 12), foreground='#181817')
        self.remove_user_last_name = ttk.Entry(self.pageeight, width=26, font=('Arial', 12), foreground='#181817')
        self.remove_user_username = ttk.Entry(self.pageeight, width=26, font=('Arial', 12), foreground='#181817')
        self.remove_user_email = ttk.Entry(self.pageeight, width=26, font=('Arial', 12), foreground='#181817')
        self.remove_user_password = ttk.Entry(self.pageeight, width=26, font=('Arial', 12), foreground='#181817')
        self.remove_user_address = ttk.Entry(self.pageeight, width=26, font=('Arial', 12), foreground='#181817')
        self.remove_user_mobileno = ttk.Entry(self.pageeight, width=26, font=('Arial', 12), foreground='#181817')

        self.remove_user_first_name.place(x=350, y=172)
        self.remove_user_last_name.place(x=350, y=212)
        self.remove_user_username.place(x=350, y=252)
        self.remove_user_email.place(x=350, y=292)
        self.remove_user_password.place(x=350, y=332)
        self.remove_user_address.place(x=350, y=372)
        self.remove_user_mobileno.place(x=350, y=412)

        self.remove_user_temp = Entry(self.pageeight, width=17, font=('Arial', 12))
        self.remove_user_temp.place(x=50, y=130)
        self.remove_user_list = Listbox(self.pageeight, selectmode=SINGLE, height=20, width=25)
        self.remove_user_list.place(x=50, y=170)
        self.remove_user_scroll = Scrollbar(self.pageeight, orient=VERTICAL)
        self.remove_user_list.configure(yscrollcommand=self.remove_user_scroll.set)
        self.remove_user_scroll.configure(command=self.remove_user_list.yview)
        self.remove_user_scroll.place(x=190, y=170, height=324)

        conn = sqlite3.connect('cafe.db')
        c = conn.cursor()
        c.execute("SELECT username FROM NEW_USER")
        data = c.fetchall()
        for i in data:
            self.remove_user_list.insert(END, '{}'.format(i[0]))

        c.close()
        conn.close()

        self.remove_user_list.bind('<<ListboxSelect>>', self.remove_user_click)

    def remove_user_click(self, event):
        self.remove_user_temp.delete(0, END)
        index = self.remove_user_list.curselection()

        self.remove_user_temp.insert(0, self.remove_user_list.get(index))

    def remove_user_submit(self):
        self.remove_user_username.insert(END, self.remove_user_temp.get())
        self.remove_user_username.state(['disabled'])
        conn = sqlite3.connect('cafe.db')
        c = conn.cursor()

        c.execute('SELECT first_name FROM NEW_USER WHERE username = ?', (self.remove_user_temp.get(),))
        data = c.fetchone()
        for i in data:
            self.remove_user_first_name.insert(END, '{}'.format(i))
            self.remove_user_first_name.state(['disabled'])

        c.execute('SELECT last_name FROM NEW_USER WHERE username = ?', (self.remove_user_temp.get(),))
        data = c.fetchone()
        for i in data:
            self.remove_user_last_name.insert(END, '{}'.format(i))
            self.remove_user_last_name.state(['disabled'])


        c.execute('SELECT email FROM NEW_USER WHERE username = ?', (self.remove_user_temp.get(),))
        data = c.fetchone()
        for i in data:
            self.remove_user_email.insert(END, '{}'.format(i))
            self.remove_user_email.state(['disabled'])

        c.execute('SELECT password FROM NEW_USER WHERE username = ?', (self.remove_user_temp.get(),))
        data = c.fetchone()
        for i in data:
            self.remove_user_password.insert(END, '{}'.format(i))
            self.remove_user_password.state(['disabled'])

        c.execute('SELECT address FROM NEW_USER WHERE username = ?', (self.remove_user_temp.get(),))
        data = c.fetchone()
        for i in data:
            self.remove_user_address.insert(END, '{}'.format(i))
            self.remove_user_address.state(['disabled'])

        c.execute('SELECT mobile_number FROM NEW_USER WHERE username = ?', (self.remove_user_temp.get(),))
        data = c.fetchone()
        for i in data:
            self.remove_user_mobileno.insert(END, '{}'.format(i))
            self.remove_user_mobileno.state(['disabled'])

        c.close()
        conn.close()

    def remove_user_remove(self):
        conn = sqlite3.connect('cafe.db')
        c = conn.cursor()
        c.execute("DELETE FROM NEW_USER WHERE  username = ?", (self.remove_user_temp.get(),))
        conn.commit()
        c.close()
        conn.close()
        messagebox.showinfo(title='NIEVE CAFE', message='User Remove Submitted!')
        self.remove_user()

    #####################################################################################

    def total_sales(self):
        # page nine
        self.pagenine.tkraise()
        self.load1 = Image.open('total sales.png')
        self.logo1 = ImageTk.PhotoImage(self.load1)
        self.label1 = Label(self.pagenine, image=self.logo1)
        self.label1.image = self.logo1
        self.label1.grid(row=0,column=0)

        try:
            self.total_sales_order_number=ttk.Entry(self.pagenine, width=26, font=('Arial', 12))
            self.total_sales_sold_items = ttk.Entry(self.pagenine, width=26, font=('Arial', 12))
            self.total_sales_total_price = ttk.Entry(self.pagenine, width=26, font=('Arial', 12))
            self.total_sales_order_number.place(y=198,x=205)
            self.total_sales_sold_items.place(y=248,x=205)
            self.total_sales_total_price.place(y=298,x=205)
            conn = sqlite3.connect('cafe.db')
            c = conn.cursor()
            c.execute("SELECT * FROM ORDER_DETAILS")
            data = c.fetchall()
            order_number=[]
            sold_items=0
            total_price=0
            for i in data:
                order_number.append(int(i[0]))
                sold_items+= int(i[1])
                total_price+=int(i[4])
            c.close()
            conn.close()

            self.total_sales_order_number.insert(END,max(order_number))
            self.total_sales_sold_items.insert(END,sold_items)
            self.total_sales_total_price.insert(END,total_price)
            self.total_sales_order_number.state(['disabled'])
            self.total_sales_sold_items.state(['disabled'])
            self.total_sales_total_price.state(['disabled'])
        except:
            self.total_sales_order_number.insert(END, 0)
            self.total_sales_sold_items.insert(END, 0)
            self.total_sales_total_price.insert(END, 0)
            self.total_sales_order_number.state(['disabled'])
            self.total_sales_sold_items.state(['disabled'])
            self.total_sales_total_price.state(['disabled'])


############################################## USER WINDOW #############################################################

    def user_options(self):
        #page two
        self.pagetwo.tkraise()
        self.load1 = Image.open('admin.png')
        self.logo1 = ImageTk.PhotoImage(self.load1)
        self.label1 = Label(self.pagetwo, image=self.logo1)
        self.label1.image = self.logo1
        self.label1.pack()

        Button(self.pagetwo, width=18, text='Food Menu',font=('Arial',12),foreground='white',
               background='black',relief=GROOVE,command=self.food_menu).place(x=50,y=250)
        Button(self.pagetwo, width=18, text='Order Food', font=('Arial', 12), foreground='white',
               background='black', relief=GROOVE,command=self.order_food).place(x=50, y=300)
        Button(self.pagetwo, width=18, text='Print Invoice', font=('Arial', 12), foreground='white',
               background='black', relief=GROOVE,command=self.print_invoice).place(x=50, y=350)
        Button(self.pagetwo, width=18, text='About', font=('Arial', 12), foreground='white',
               background='black', relief=GROOVE,command=self.about).place(x=50, y=400)
        Button(self.pagetwo, width=20, text='Logout', font=('Arial', 10), foreground='black',
               background='white', relief=GROOVE,command=self.login_screen).place(x=50, y=650)

        #page three
        self.pagethree.tkraise()
        self.load1 = Image.open('welcome.png')
        self.logo1 = ImageTk.PhotoImage(self.load1)
        self.label1 = Label(self.pagethree, image=self.logo1)
        self.label1.image = self.logo1
        self.label1.grid(row=0,column=0)

    ######################################################################################

    def food_menu(self):
        #page ten
        self.pageten.tkraise()
        self.load1 = Image.open('food menu.png')
        self.logo1 = ImageTk.PhotoImage(self.load1)
        self.label1 = Label(self.pageten, image=self.logo1)
        self.label1.image = self.logo1
        self.label1.grid(row=0, column=0)

        Button(self.pageten, width=14, text='Submit', font=('Arial', 9), foreground='black',
               background='white', relief=GROOVE, command=self.food_menu_submit).place(x=230, y=128)
        Button(self.pageten, width=14, text='Reset', font=('Arial', 9), foreground='black',
               background='white', relief=GROOVE, command=self.food_menu).place(x=400, y=370)

        self.food_menu_name = ttk.Entry(self.pageten, width=22, font=('Arial', 12))
        self.food_menu_type = ttk.Entry(self.pageten, width=22, font=('Arial', 12))
        self.food_menu_price = ttk.Entry(self.pageten, width=22, font=('Arial', 12))
        self.food_menu_name.place(x=350, y=225)
        self.food_menu_type.place(x=350, y=266)
        self.food_menu_price.place(x=350, y=306)

        self.food_menu_temp = Entry(self.pageten, width=17, font=('Arial', 12))
        self.food_menu_temp.place(x=50, y=130)
        self.food_menu_list = Listbox(self.pageten, selectmode=SINGLE, height=20, width=25)
        self.food_menu_list.place(x=50, y=170)
        self.food_menu_scroll = Scrollbar(self.pageten, orient=VERTICAL)
        self.food_menu_list.configure(yscrollcommand=self.food_menu_scroll.set)
        self.food_menu_scroll.configure(command=self.food_menu_list.yview)
        self.food_menu_scroll.place(x=190, y=170, height=324)

        conn = sqlite3.connect('cafe.db')
        c = conn.cursor()
        c.execute("SELECT food_name FROM FOOD_ITEMS")
        data = c.fetchall()
        for i in data:
            self.food_menu_list.insert(END, '{}'.format(i[0]))

        c.close()
        conn.close()

        self.food_menu_list.bind('<<ListboxSelect>>', self.food_menu_click)

    def food_menu_click(self, event):
        self.food_menu_temp.delete(0, END)
        index = self.food_menu_list.curselection()
        self.food_menu_temp.insert(0, self.food_menu_list.get(index))

    def food_menu_submit(self):
        self.food_menu_name.insert(END, self.food_menu_temp.get())
        self.food_menu_name.state(['disabled'])
        conn = sqlite3.connect('cafe.db')
        c = conn.cursor()
        c.execute('SELECT food_type FROM FOOD_ITEMS WHERE food_name = ?', (self.food_menu_temp.get(),))
        data = c.fetchone()
        for i in data:
            self.food_menu_type.insert(END, '{}'.format(i))
        self.food_menu_type.state(['disabled'])

        c.execute('SELECT food_price FROM FOOD_ITEMS WHERE food_name = ?', (self.food_menu_temp.get(),))
        data = c.fetchone()
        for i in data:
            self.food_menu_price.insert(END, '{}'.format(i))
        self.food_menu_price.state(['disabled'])
        c.close()
        conn.close()

    #######################################################################################

    def order_food(self):
        # page eleven
        self.order_items=0
        self.pageeleven.tkraise()
        self.load1 = Image.open('order food.png')
        self.logo1 = ImageTk.PhotoImage(self.load1)
        self.label1 = Label(self.pageeleven, image=self.logo1)
        self.label1.image = self.logo1
        self.label1.grid(row=0, column=0)

        Button(self.pageeleven, width=14, text='Submit', font=('Arial', 9), foreground='black',
               background='white', relief=GROOVE, command=self.order_food_submit).place(x=230, y=128)
        Button(self.pageeleven, width=14, text='Reset', font=('Arial', 9), foreground='black',
               background='white', relief=GROOVE, command=self.order_food_reset).place(x=270, y=400)
        Button(self.pageeleven, width=14, text='Add', font=('Arial', 9), foreground='black',
               background='white', relief=GROOVE, command=self.order_food_add).place(x=400, y=400)
        Button(self.pageeleven, width=14, text='Total', font=('Arial', 9), foreground='black',
               background='white', relief=GROOVE, command=self.order_food_total).place(x=530, y=400)

        self.order_food_var_invoice_number = StringVar()
        self.order_food_invoice_number = ttk.Entry(self.pageeleven,textvariable=self.order_food_var_invoice_number,
                                                   width=17, font=('Arial', 12))
        self.order_food_invoice_number.place(x=655, y=129)

        self.order_food_quantity=IntVar()
        self.order_food_items = ttk.Entry(self.pageeleven, width=22, font=('Arial', 12))
        self.order_food_items.insert(END, '{}'.format(self.order_items))
        self.order_food_items.state(['disabled'])
        self.order_food_name = ttk.Entry(self.pageeleven, width=22, font=('Arial', 12))
        self.order_food_type = ttk.Entry(self.pageeleven, width=22, font=('Arial', 12))
        self.order_food_price = ttk.Entry(self.pageeleven, width=22, font=('Arial', 12))
        self.order_quantity = Spinbox(self.pageeleven ,from_=1 , to=100 , textvariable=self.order_food_quantity ,
                                      font=('Arial', 12))
        self.order_food_items.place(x=350, y=185)
        self.order_food_name.place(x=350, y=225)
        self.order_food_type.place(x=350, y=266)
        self.order_food_price.place(x=350, y=306)
        self.order_quantity.place(x=350, y=346 , width=205)

        self.order_food_temp = ttk.Entry(self.pageeleven, width=17, font=('Arial', 12))
        self.order_food_temp.place(x=50, y=130)
        self.order_food_list = Listbox(self.pageeleven, selectmode=SINGLE, height=20, width=25)
        self.order_food_list.place(x=50, y=170)
        self.order_food_scroll = Scrollbar(self.pageeleven, orient=VERTICAL)
        self.order_food_list.configure(yscrollcommand=self.order_food_scroll.set)
        self.order_food_scroll.configure(command=self.order_food_list.yview)
        self.order_food_scroll.place(x=190, y=170, height=324)

        try:
            conn = sqlite3.connect('cafe.db')
            c = conn.cursor()
            c.execute('select order_number FROM ORDER_DETAILS')
            data = c.fetchall()
            c.close()
            conn.close()
            temp=[]
            for i in data:
                i = int(i[0])
                temp.append(i+1)
            self.invoice_number=max(temp)

        except Exception:

            self.invoice_number = 1

        self.order_food_invoice_number.state(['disabled'])
        self.order_food_var_invoice_number.set(self.invoice_number)


        conn = sqlite3.connect('cafe.db')
        c = conn.cursor()
        c.execute("SELECT food_name FROM FOOD_ITEMS")
        data = c.fetchall()
        for i in data:
            self.order_food_list.insert(END, '{}'.format(i[0]))

        c.close()
        conn.close()

        self.order_food_list.bind('<<ListboxSelect>>', self.order_food_click)

    def order_food_click(self, event):
        self.order_food_temp.delete(0, END)
        index = self.order_food_list.curselection()
        self.order_food_temp.insert(0, self.order_food_list.get(index))
        self.order_food_temp.state(['disabled'])

    def order_food_submit(self):
        self.order_food_name.insert(END, self.order_food_temp.get())
        self.order_food_name.state(['disabled'])
        conn = sqlite3.connect('cafe.db')
        c = conn.cursor()
        c.execute('SELECT food_type FROM FOOD_ITEMS WHERE food_name = ?', (self.order_food_temp.get(),))
        data = c.fetchone()
        for i in data:
            self.order_food_type.insert(END, '{}'.format(i))
        self.order_food_type.state(['disabled'])

        c.execute('SELECT food_price FROM FOOD_ITEMS WHERE food_name = ?', (self.order_food_temp.get(),))
        data = c.fetchone()
        for i in data:
            self.order_food_price.insert(END, '{}'.format(i))
        self.order_food_price.state(['disabled'])
        c.close()
        conn.close()

    def order_food_reset(self):
        self.order_food_name.state(['!disabled'])
        self.order_food_type.state(['!disabled'])
        self.order_food_price.state(['!disabled'])
        self.order_food_temp.state(['!disabled'])
        self.order_food_name.delete(0,END)
        self.order_food_type.delete(0,END)
        self.order_food_price.delete(0,END)
        self.order_food_temp.delete(0, END)

    def order_food_add(self):
        try:
            order_number = self.order_food_var_invoice_number.get()
            food_name = self.order_food_name.get()
            food_type = self.order_food_type.get()
            food_price = int(self.order_food_price.get())
            quantity = int(self.order_food_quantity.get())
            total = food_price*quantity
            conn=sqlite3.connect('cafe.db')
            c=conn.cursor()
            c.execute('INSERT INTO ORDER_ITEMS VALUES (?,?,?,?,?,?)',
                      (order_number,food_name,food_type,food_price,quantity,total,))
            conn.commit()
            c.close()
            conn.close()

            self.order_food_name.state(['!disabled'])
            self.order_food_type.state(['!disabled'])
            self.order_food_price.state(['!disabled'])
            self.order_food_temp.state(['!disabled'])
            self.order_food_name.delete(0, END)
            self.order_food_type.delete(0, END)
            self.order_food_price.delete(0, END)
            self.order_food_temp.delete(0, END)
            self.order_food_items.state(['!disabled'])
            self.order_food_items.delete(0,END)
            self.order_quantity.delete(0,END)
            self.order_items = self.order_items + 1
            self.order_food_items.insert(END, '{}'.format(self.order_items))
            self.order_food_items.state(['disabled'])
            self.order_quantity.insert(END,1)
        except:
            messagebox.showwarning('NIEVE CAFE','Item Did Add Without Selection')
            self.order_food_reset()

    def order_food_total(self):

        try:
            if self.order_food_items.get()=='0':
                raise ValueError
            else:
                conn = sqlite3.connect('cafe.db')
                c = conn.cursor()
                c.execute('SELECT total FROM ORDER_ITEMS WHERE order_number = ? ', (self.order_food_var_invoice_number.get(),))
                data=c.fetchall()
                price = 0
                for i in data:
                    temp = int(i[0])
                    price += temp
                order_number = self.invoice_number
                items =len(data)
                sub_total = int(price)
                vat_tax = int((price/100)*5)
                total = sub_total + vat_tax

                c.execute('INSERT INTO ORDER_DETAILS VALUES (?,?,?,?,?)',
                          (order_number,items,sub_total,vat_tax,total,))
                conn.commit()
                c.close()
                conn.close()
                self.temp_invoice_order_number = order_number
                self.temp_invoice_items = items
                self.temp_invoice_sub_total = sub_total
                self.temp_invoice_vat_tax = vat_tax
                self.temp_invoice_total = total

        except ValueError:
            messagebox.showwarning('NIEVE CAFE','Please Add Items First ')
            self.order_food()

        else:
            self.invoice()

    def invoice(self):
        # page twelve
        self.pagetwelve.tkraise()
        self.load1 = Image.open('invoice.png')
        self.logo1 = ImageTk.PhotoImage(self.load1)
        self.label1 = Label(self.pagetwelve, image=self.logo1)
        self.label1.image = self.logo1
        self.label1.grid(row=0, column=0)

        Button(self.pagetwelve, width=16, text='Back', font=('Arial', 9), foreground='black',
               background='white', relief=GROOVE, command=self.order_food).place(x=215, y=420)
        Button(self.pagetwelve, width=16, text='Print', font=('Arial', 9), foreground='black',
               background='white', relief=GROOVE, command=self.print).place(x=355, y=420)

        conn = sqlite3.connect('cafe.db')
        c = conn.cursor()

        self.invoice_invoice_number = ttk.Entry(self.pagetwelve, width=22, font=('Arial', 14))
        self.invoice_number_of_items = ttk.Entry(self.pagetwelve, width=22, font=('Arial', 14))
        self.invoice_sub_total = ttk.Entry(self.pagetwelve, width=22, font=('Arial', 14))
        self.invoice_tax = ttk.Entry(self.pagetwelve, width=22, font=('Arial', 14))
        self.invoice_total = ttk.Entry(self.pagetwelve, width=22, font=('Arial', 14))
        self.invoice_invoice_number.place(x=220, y=156)
        self.invoice_number_of_items.place(x=220, y=205)
        self.invoice_sub_total.place(x=220, y=255)
        self.invoice_tax.place(x=220, y=303)
        self.invoice_total.place(x=220, y=353)

        self.invoice_invoice_number.insert(0,self.temp_invoice_order_number)
        self.invoice_number_of_items.insert(0,self.temp_invoice_items)
        self.invoice_sub_total.insert(0,self.temp_invoice_sub_total)
        self.invoice_tax.insert(0,self.temp_invoice_vat_tax)
        self.invoice_total.insert(0,self.temp_invoice_total)
        self.invoice_invoice_number.state(['disabled'])
        self.invoice_number_of_items.state(['disabled'])
        self.invoice_sub_total.state(['disabled'])
        self.invoice_tax.state(['disabled'])
        self.invoice_total.state(['disabled'])

        conn = sqlite3.connect('cafe.db')
        c = conn.cursor()
        c.execute('SELECT * FROM ORDER_ITEMS WHERE order_number = ?', (self.invoice_invoice_number.get(),))
        data = c.fetchall()
        items = ''
        for i in data:
            items = items + '  ' + i[1] + '\t\t' + str(i[4]) + '\t\t' + str(i[5]) + '\n'

        c.execute('SELECT * FROM ORDER_DETAILS WHERE order_number = ?', (self.invoice_invoice_number.get(),))
        data = c.fetchall()
        for i in data:
            invoice = str(i[0])
            noofitems = str(i[1])
            subtotal = str(i[2])
            tax = str(i[3])
            total = str(i[4])
        c.close()
        conn.close()

        qrcode  =  ('\n\t\tNIEVE CAFE\n'
                   '  ____________________________________ '
                   '\n\n'
                   '  Invoice No. ' + invoice + '\n'
                   '  Date ' + dt.strftime('%d,%B,%Y %H:%M') +
                   '\n'
                   '  ____________________________________ '
                   '\n\n'
                   '  Number Of Items ' + noofitems + '\n\n'
                   '  Name\t\tQuantity\t\tPrice\n'
                   +items +
                   '\n\n'
                   '  ____________________________________ '
                   '\n\n'
                   '\t\t  Sub Total:  ' + subtotal + '\n'
                   '\t\t  Vat/Tax:    ' + tax + '\n'
                   '\t\t  Total:      ' + total + '\n' )

        self.code = pyqrcode.create(qrcode)
        self.code_xbm = self.code.xbm(scale=3)
        self.code_bmp = BitmapImage(data=self.code_xbm)
        self.code_bmp.config(background="white",foreground="black")
        self.label = Label(self.pagetwelve, image=self.code_bmp)
        self.label.place(x=570,y=150)

    def print(self):

        doc = SimpleInvoice('invoice.pdf')

        doc.invoice_info = InvoiceInfo(self.invoice_invoice_number.get(), datetime.now())  # Invoice info, optional

        doc.service_provider_info = ServiceProviderInfo(
            name='Nieve Cafe',
            street='Abc',
            city='Amritsar',
            state='Punjab',
            country='India',
            post_code='143001',
            vat_tax_number='22111997' )

        doc.client_info = ClientInfo(email='Nievecafe@gmail.com')

        conn = sqlite3.connect('cafe.db')
        c = conn.cursor()
        c.execute('SELECT * FROM ORDER_ITEMS WHERE order_number = ?', (self.invoice_invoice_number.get(),))
        data = c.fetchall()
        for i in data:
            doc.add_item(Item(i[1], i[2], i[4], i[3]))

        doc.set_item_tax_rate(5)

        doc.set_bottom_tip("Nievecafe@gmail.com<br />Please contact us for any questions.")

        doc.finish()

        webbrowser.open_new(r'file:///{}/invoice.pdf'.format(cur))

    ########################################################################################

    def print_invoice(self):
        # page thirteen
        self.pagethirteen.tkraise()
        self.load1 = Image.open('print invoice.png')
        self.logo1 = ImageTk.PhotoImage(self.load1)
        self.label1 = Label(self.pagethirteen, image=self.logo1)
        self.label1.image = self.logo1
        self.label1.grid(row=0, column=0)

        self.print_invoice_invoice = ttk.Entry(self.pagethirteen, width=22, font=('Arial', 12))
        self.print_invoice_invoice.place(x=220,y=234)

        Button(self.pagethirteen, width=16, text='Reset', font=('Arial', 9), foreground='black',
               background='white', relief=GROOVE, command=self.print_invoice).place(x=190, y=290)
        Button(self.pagethirteen, width=16, text='Submit', font=('Arial', 9), foreground='black',
               background='white', relief=GROOVE, command=self.print_invoice_submit).place(x=330, y=290)

        self.text_invoice=Text(self.pagethirteen,width=38,heigh=25,font=('Arial',9))
        self.text_invoice.place(x=580,y=120)
        text_scroll = Scrollbar(self.pagethirteen, orient=VERTICAL)
        self.text_invoice.configure(yscrollcommand=text_scroll.set)
        text_scroll.configure(command=self.text_invoice.yview)
        text_scroll.place(x=845, y=120, height=379)

    def print_invoice_submit(self):
        try:
            self.text_invoice.delete(1.0,END)
            conn = sqlite3.connect('cafe.db')
            c = conn.cursor()
            c.execute('SELECT * FROM ORDER_ITEMS WHERE order_number = ?', (self.print_invoice_invoice.get(),))
            data = c.fetchall()
            items = ''
            for i in data:
                items = items + '  ' + i[1] + '\t\t' + str(i[4]) + '\t\t' + str(i[5]) + '\n'

            c.execute('SELECT * FROM ORDER_DETAILS WHERE order_number = ?', (self.print_invoice_invoice.get(),))
            data = c.fetchall()
            for i in data:
                invoice = str(i[0])
                noofitems = str(i[1])
                subtotal = str(i[2])
                tax = str(i[3])
                total = str(i[4])
            c.close()
            conn.close()

            p_invoice =('\n\t\tNIEVE CAFE\n'
                       '  ____________________________________ '
                       '\n\n'
                       '  Invoice No. ' + invoice + '\n'
                       '  Date ' + dt.strftime('%d,%B,%Y %H:%M') +
                       '\n'
                       '  ____________________________________ '
                       '\n\n'
                       '  Number Of Items ' + noofitems + '\n\n'
                       '  Name\t\tQuantity\t\tPrice\n'
                       +items +
                       '\n'
                       '  ____________________________________ '
                       '\n\n'
                       '\t\t  Sub Total:  ' + subtotal + '\n'
                       '\t\t       Vat/Tax:  ' + tax + '\n'
                       '\t\t           Total:  ' + total + '\n' )
            self.text_invoice.insert(END,p_invoice)
            self.print_invoice_invoice.state(['disabled'])

        except:
            self.print_invoice_invoice.delete(0, END)
            messagebox.showwarning('NIEVE CAFE','Invalid Invoice Number.')

        else:
            Button(self.pagethirteen, width=16, text='Print', font=('Arial', 9), foreground='black',
                   background='white', relief=GROOVE, command=self.print_invoice_print).place(x=670, y=510)



    def print_invoice_print(self):
        self.print_invoice_invoice.delete(0, END)
        doc = SimpleInvoice('invoice.pdf')
        doc.invoice_info = InvoiceInfo(self.print_invoice_invoice.get(), datetime.now())
        doc.service_provider_info = ServiceProviderInfo(
            name='Nieve Cafe',
            street='Abc',
            city='Amritsar',
            state='Punjab',
            country='India',
            post_code='143001',
            vat_tax_number='22111997' )
        doc.client_info = ClientInfo(email='Nievecafe@gmail.com')
        conn = sqlite3.connect('cafe.db')
        c = conn.cursor()
        c.execute('SELECT * FROM ORDER_ITEMS WHERE order_number = ?', (self.print_invoice_invoice.get(),))
        data = c.fetchall()
        for i in data:
            doc.add_item(Item(i[1], i[2], i[4], i[3]))
        doc.set_item_tax_rate(5)
        doc.set_bottom_tip("Nievecafe@gmail.com<br />Please contact us for any questions.")
        doc.finish()
        self.print_invoice()
        webbrowser.open_new(r'file:///{}/invoice.pdf'.format(cur))


    ########################################################################################

    def about(self):
        # page fourteen
        self.pagefourteen.tkraise()
        self.load1 = Image.open('about.png')
        self.logo1 = ImageTk.PhotoImage(self.load1)
        self.label1 = Label(self.pagefourteen, image=self.logo1)
        self.label1.image = self.logo1
        self.label1.grid(row=0, column=0)

    #########################################################################################

cafe=cafe()

cafe.root.mainloop()
