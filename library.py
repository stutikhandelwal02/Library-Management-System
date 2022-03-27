import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import tkinter
import  mysql.connector
from tkinter import messagebox
import datetime


class LibManagementSys:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        #-----------------------Variables---------------------------
        self.member=StringVar()
        self.firstname=StringVar()
        self.lastname=StringVar()
        self.address = StringVar()
        self.id = StringVar()
        self.postalcode = StringVar()
        self.mobile = StringVar()
        self.bookno = StringVar()
        self.bookname = StringVar()
        self.author = StringVar()
        self.borrowed = StringVar()
        self.duedate = StringVar()
        self.latefine = StringVar()


        lbltitle = Label(self.root,text = "LIBRARY MANAGEMENT SYSTEM",bg="#FFC0D3",fg="#9C0F48" , bd=15, relief = RIDGE, font = ("times new roman",45,"bold"),padx=1,pady=5)
        lbltitle.pack(side=TOP,fill=X);

        frame = Frame(self.root,bd=8,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=95,width=1270,height=300)

        #--------------------------------Left Frame--------------------------------------
        frameleft = LabelFrame(frame,text="Library Membership Information",bg ="powder blue",bd=10,relief=RIDGE,font=('times new roman',15,"bold"),padx=10)
        frameleft.place(x=0,y=5,width=900,height=270)

        lbl = Label(frameleft,bg="powder blue",text="Member Type",font=('times new roman',15,"bold"),padx=10,pady=5)
        lbl.grid(row=0,column=0,sticky=W)

        #---------------------------------Left Side Entries------------------------------
        comMember= ttk.Combobox(frameleft,textvariable=self.member, font=('times new roman', 12, "bold"), width=20,state="readonly" )
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0, column=1)

        lblroll = Label(frameleft,bg="powder blue", text="Registration Number", font=('arial', 12, "bold"), padx=10, pady=5)
        lblroll.grid(row=1, column=0, sticky=W)
        textroll = Entry(frameleft,textvariable=self.id, font=('arial', 13, "bold"), width=20)
        textroll.grid(row=1, column=1)

        lblFirstname = Label(frameleft,bg="powder blue", text="First Name", font=('arial', 12, "bold"), padx=10, pady=5)
        lblFirstname.grid(row=2, column=0, sticky=W)
        textFirstname = Entry(frameleft,textvariable=self.firstname, font=('arial', 13, "bold"), width=20)
        textFirstname.grid(row=2, column=1)

        lblLastname = Label(frameleft,bg="powder blue", text="Last Name", font=('arial', 12, "bold"), padx=10, pady=5)
        lblLastname.grid(row=3, column=0, sticky=W)
        textLastname = Entry(frameleft,textvariable=self.lastname, font=('arial', 13, "bold"), width=20)
        textLastname.grid(row=3, column=1)

        lblAddress = Label(frameleft,bg="powder blue", text="Address", font=('arial', 12, "bold"), padx=10,pady=5)
        lblAddress.grid(row=4, column=0, sticky=W)
        textAddress = Entry(frameleft,textvariable=self.address, font=('arial', 13, "bold"), width=20)
        textAddress.grid(row=4, column=1)

        lblPostalcode= Label(frameleft, bg="powder blue", text="Postal Code", font=('arial', 12, "bold"), padx=10, pady=5)
        lblPostalcode.grid(row=5, column=0, sticky=W)
        textPostalcode = Entry(frameleft,textvariable=self.postalcode, font=('arial', 13, "bold"), width=20)
        textPostalcode.grid(row=5, column=1)

        lblMobile = Label(frameleft, bg="powder blue", text="Mobile No.", font=('arial', 12, "bold"), padx=10, pady=5)
        lblMobile.grid(row=6, column=0, sticky=W)
        textMobile= Entry(frameleft,textvariable=self.mobile, font=('arial', 13, "bold"), width=20)
        textMobile.grid(row=6, column=1)

        lblBookNo = Label(frameleft, bg="powder blue", text="Book No.", font=('arial', 12, "bold"), padx=10, pady=5)
        lblBookNo.grid(row=1, column=2, sticky=W)
        textBookNo = Entry(frameleft,textvariable=self.bookno, font=('arial', 13, "bold"), width=20)
        textBookNo.grid(row=1, column=3)

        lblBookName = Label(frameleft, bg="powder blue", text="Book Name", font=('arial', 12, "bold"), padx=10, pady=5)
        lblBookName.grid(row=2, column=2, sticky=W)
        textBookName = Entry(frameleft,textvariable=self.bookname, font=('arial', 13, "bold"), width=20)
        textBookName.grid(row=2, column=3)

        lblAuthor = Label(frameleft, bg="powder blue", text="Author", font=('arial', 12, "bold"), padx=10, pady=5)
        lblAuthor.grid(row=3, column=2, sticky=W)
        textAuthor = Entry(frameleft,textvariable=self.author, font=('arial', 13, "bold"), width=20)
        textAuthor.grid(row=3, column=3)

        lblborrowDate= Label(frameleft, bg="powder blue", text="Borrow Date", font=('arial', 12, "bold"), padx=10, pady=5)
        lblborrowDate.grid(row=4, column=2, sticky=W)
        textborrowDate= Entry(frameleft,textvariable=self.borrowed, font=('arial', 13, "bold"), width=20)
        textborrowDate.grid(row=4, column=3)

        lblDue = Label(frameleft, bg="powder blue", text="Due Date", font=('arial', 12, "bold"), padx=10, pady=5)
        lblDue.grid(row=5, column=2, sticky=W)
        textDue = Entry(frameleft,textvariable=self.duedate, font=('arial', 13, "bold"), width=20)
        textDue.grid(row=5, column=3)

        lblLateFine = Label(frameleft, bg="powder blue", text="Late Fine", font=('arial', 12, "bold"), padx=10, pady=5)
        lblLateFine.grid(row=6, column=2, sticky=W)
        textLateFine = Entry(frameleft,textvariable=self.latefine, font=('arial', 13, "bold"), width=20)
        textLateFine.grid(row=6, column=3)


        #-------------------------Right Frame---------------------
        frameright= LabelFrame(frame,text="Book Details",bg ="powder blue",bd=10,relief=RIDGE,font=('times new roman',15,"bold"),padx=5)
        frameright.place(x=700,y=5,width=525,height=270)

        #------------------------Right Side Entries---------------
        self.txtBox = Text(frameright,font=("arial",8,"bold italic"),width=40,height=26,padx=10)
        self.txtBox.grid(row=0,column=4)

        listScrollbar=Scrollbar(frameright)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listbooks=["First ABC of python","Don Quixote	Miguel de Cervantes","Alice's Adventures in Wonderland	Lewis Carroll","The Adventures of Huckleberry Finn	Mark Twain",
"The Adventures of Tom Sawyer	Mark Twain","Treasure Island	Robert Louis Stevenson","Pride and Prejudice Jane Austen","Wuthering Heights Emily Brontë",
"Jane Eyre	Charlotte Brontë","Moby Dick Herman Melville","The Scarlet Letter Nathaniel Hawthorne","Gulliver's Travels	Jonathan Swift",
"The Pilgrim's Progress	John Bunyan","A Christmas Carol	Charles Dickens","David Copperfield	Charles Dickens","A Tale of Two Cities	Charles Dickens",
"Little Women Louisa May Alcott","Great Expectations Charles Dickens","The Hobbit, or, There and Back Again	J.R.R. Tolkien","Frankenstein, or, the Modern Prometheus Mary Shelley",
"Oliver Twist Charles Dickens","Uncle Tom's Cabin Harriet Beecher Stowe","Crime and Punishment Fyodor Dostoyevsky","Madame Bovary: Patterns of Provincial life	Gustave Flaubert","The Return of the King J.R.R. Tolkien",
"Dracula Bram Stoker","The Three Musketeers Alexandre Dumas","Brave New World Aldous Huxley","War and Peace	Leo Tolstoy","To Kill a Mockingbird	Harper Lee","The Wizard of Oz L. Frank Baum",
"Les Misérables	Victor Hugo","The Secret Garden	Frances Hodgson Burnett","Animal Farm George Orwell","The Great Gatsby F. Scott Fitzgerald","The Little Prince	Antoine de Saint-Exupéry",
"The Call of the Wild Jack London","20,000 Leagues Under the Sea Jules Verne","Anna Karenina Leo Tolstoy","The Wind in the Willows	Kenneth Grahame",
"The Picture of Dorian Gray	Oscar Wilde","The Grapes of Wrath	John Steinbeck","Sense and Sensibility	Jane Austen","The Last of the Mohicans	James Fenimore Cooper",
"Tess of the d'Urbervilles	Thomas Hardy","Harry Potter and the Sorcerer's Stone J.K. Rowling"]
        def SelectBook(event=""):
            value=str(listbox.get(listbox.curselection()))
            x=value
            for i in range(len(listbooks)):
                if listbooks[i]==x:
                    break
            self.bookno.set("BKID"+str(5454+i))
            self.bookname.set(x)
            self.author.set("Paul Berry")

            d1=datetime.date.today()
            d2=datetime.timedelta(days=15)
            d3=d1+d2
            self.borrowed.set(d1)
            self.duedate.set(d3)
            self.latefine.set("Rs.100")


        #------------------------Listbox-------------------------
        listbox=Listbox(frameright,font=("helvatica",10,"italic"),width=30,height=20 )
        listbox.bind("<<ListboxSelect>>",SelectBook)
        listbox.grid(row=0,column=0,padx=0)
        listScrollbar.config(command=listbox.yview)


        for item in listbooks:
            listbox.insert(END,item)


        #---------------------------BUTTONS-----------------------
        framebutton = Frame(self.root,bd=12,relief=RIDGE,bg="powder blue",pady=1)
        framebutton.place(x=0,y=370,width=1530,height=60)

        btnAddData = Button(framebutton,command=self.insert_data ,text="Add Data", font=("arial", 12, "bold"), width=20, bg="blue", fg="white")
        btnAddData.grid(row=0, column=0)

        btnshowData = Button(framebutton,command=self.showData, text="Show Data", font=("arial", 12, "bold"), width=20, bg="blue", fg="white")
        btnshowData.grid(row=0, column=1)

        btnupdate = Button(framebutton,command=self.update, text="Update", font=("arial", 12, "bold"), width=20, bg="blue", fg="white")
        btnupdate.grid(row=0, column=2)

        btndelete = Button(framebutton,command=self.delete, text="Delete", font=("arial", 12, "bold"), width=20, bg="blue", fg="white")
        btndelete.grid(row=0, column=3)

        btnreset = Button(framebutton,command=self.reset, text="Reset", font=("arial", 12, "bold"), width=20, bg="blue", fg="white")
        btnreset.grid(row=0, column=4)

        btnexit = Button(framebutton,command=self.Exitt, text="Exit", font=("arial", 12, "bold"), width=20, bg="blue", fg="white")
        btnexit.grid(row=0, column=5)

        #---------------------------INFO FRAME--------------------
        frameDetails=Frame(self.root,bd=10,relief=RIDGE,padx=3,bg="powder blue")
        frameDetails.place(x=0,y=430,width=1530,height=510)

        table=Frame(frameDetails,bd=6,relief=RIDGE,bg="powder blue")
        table.place(x=0,y=2,width=1260,height=201)

        xscroll = ttk.Scrollbar(table,orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(table,orient=VERTICAL)
        self.library_table=ttk.Treeview(table,column=("membertype","registration_no","firstname","lastname","address","postalcode","mobile_no","book_no","bookName","author","borrowed_on","dueDate","LateFine"),xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)


        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("registration_no", text="Registration No.")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address", text="Address")
        self.library_table.heading("postalcode", text="Postal Code")
        self.library_table.heading("mobile_no", text="Mobile No.")
        self.library_table.heading("book_no", text="Book No.")
        self.library_table.heading("bookName", text="Book Name")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("borrowed_on", text="Borrow Date")
        self.library_table.heading("dueDate", text="Due Date")
        self.library_table.heading("LateFine", text="Late Fine")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=True)

        self.library_table.column("membertype", width=100 )
        self.library_table.column("registration_no", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address", width=100)
        self.library_table.column("postalcode", width=100)
        self.library_table.column("mobile_no", width=100)
        self.library_table.column("book_no", width=100)
        self.library_table.column("bookName", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("borrowed_on", width=100)
        self.library_table.column("dueDate", width=100)
        self.library_table.column("LateFine", width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


    def insert_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="emp")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.member.get(),self.id.get(),self.firstname.get(),self.lastname.get(),
            self.address.get(), self.postalcode.get() ,self.mobile.get() ,self.bookno.get(),self.bookname.get(),self.author.get(),
            self.borrowed.get(),self.duedate.get(),self.latefine.get()))

        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success","Member has been Added Successfully")
        self.reset()
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="emp")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(* self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member.set(row[0])
        self.id.set(row[1])
        self.firstname.set(row[2])
        self.lastname.set(row[3])
        self.address.set(row[4])
        self.postalcode.set(row[5])
        self.mobile.set(row[6])
        self.bookno.set(row[7])
        self.bookname.set(row[8])
        self.borrowed.set(row[10])
        self.author.set(row[9])
        self.duedate.set(row[11])
        self.latefine.set(row[12])

    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+self.member.get()+"\n")
        self.txtBox.insert(END, "Registration no.\t\t" + self.id.get() + "\n")
        self.txtBox.insert(END, "First Name\t\t" + self.firstname.get() + "\n")
        self.txtBox.insert(END, "Last Name\t\t" + self.lastname.get() + "\n")
        self.txtBox.insert(END, "Address\t\t" + self.address.get() + "\n")
        self.txtBox.insert(END, "Postal code\t\t" + self.postalcode.get() + "\n")
        self.txtBox.insert(END, "Mobile no.\t\t" + self.mobile.get() + "\n")
        self.txtBox.insert(END, "Book no.\t\t" + self.bookno.get() + "\n")
        self.txtBox.insert(END, "Book Name\t\t" + self.bookname.get() + "\n")
        self.txtBox.insert(END, "Author\t\t" + self.author.get() + "\n")
        self.txtBox.insert(END, "Borrow Date\t\t" + self.borrowed.get() + "\n")
        self.txtBox.insert(END, "Due Date\t\t" + self.duedate.get() + "\n")
        self.txtBox.insert(END, "Late Fine\t\t" + self.latefine.get() + "\n")

    def reset(self):
        self.member.set("")
        self.id.set("")
        self.firstname.set("")
        self.lastname.set("")
        self.address.set("")
        self.postalcode.set("")
        self.mobile.set("")
        self.bookno.set("")
        self.bookname.set("")
        self.borrowed.set("")
        self.author.set("")
        self.duedate.set("")
        self.latefine.set("")
        self.txtBox.delete("1.0",END)


    def Exitt(self):
        Exitt=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if Exitt>0:
            self.root.destroy()
            return

    def delete(self):
        if self.id.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="emp")
            my_cursor = conn.cursor()
            query = "delete from library where ID=%s"
            value = (self.id.get(),)
            my_cursor.execute(query,value)
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been Deleted Successfully")
    def update(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="emp")
        my_cursor = conn.cursor()
        query = "update library set Member=%s, FirstName=%s, LastName=%s,Address=%s, PosId=%s,Mobile=%s,BookNo=%s, BookName=%s,Author=%s, BorrowDate=%s, DueDate=%s, LateFine=%s where ID=%s "
        my_cursor.execute(query,(self.member.get(),self.firstname.get(),self.lastname.get(),
            self.address.get(), self.postalcode.get() ,self.mobile.get() ,self.bookno.get(),self.bookname.get(),self.author.get(),
            self.borrowed.get(),self.duedate.get(),self.latefine.get(),self.id.get()))

        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been Updated Successfully")

if __name__== "__main__":
    root=Tk()
    obj=LibManagementSys(root)
    root.mainloop()
