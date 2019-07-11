import tkinter as tk
import backend


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        self.labelTitle = tk.Label(self)
        self.labelTitle["text"] = "Title"
        self.labelTitle.grid(row=0,column=0)
        self.labelYear = tk.Label(self)
        self.labelYear["text"] = "Year"
        self.labelYear.grid(row=1,column=0)
        self.labelAuthor = tk.Label(self)
        self.labelAuthor["text"] = "Author"
        self.labelAuthor.grid(row=0,column=3)
        self.labelISBN = tk.Label(self)
        self.labelISBN["text"] = "ISBN"
        self.labelISBN.grid(row=1,column=3)

        self.inputTitle = tk.StringVar()
        self.entryTitle = tk.Entry(self)
        self.entryTitle["textvariable"] = self.inputTitle
        self.entryTitle.grid(row=0,column=1)
        self.inputYear = tk.StringVar()
        self.entryYear = tk.Entry(self)
        self.entryYear["textvariable"] = self.inputYear
        self.entryYear.grid(row=0, column=4)
        self.inputAuthor = tk.StringVar()
        self.entryAuthor = tk.Entry(self)
        self.entryAuthor["textvariable"] = self.inputAuthor
        self.entryAuthor.grid(row=1, column=1)
        self.inputISBN = tk.StringVar()
        self.entryISBN = tk.Entry(self)
        self.entryISBN["textvariable"] = self.inputISBN
        self.entryISBN.grid(row=1,column=4)

        self.btnView = tk.Button(self, width=12)
        self.btnView["command"] = ""
        self.btnView["text"] = "View All"
        self.btnView.grid(row=2,column=4)
        self.btnSearch = tk.Button(self, width = 12)
        self.btnSearch["command"] = ""
        self.btnSearch["text"] = "Search entry"
        self.btnSearch.grid(row=3,column=4)
        self.btnEntry = tk.Button(self, width = 12)
        self.btnEntry["command"] = ""
        self.btnEntry["text"] = "Add entry"
        self.btnEntry.grid(row=4,column=4)
        self.btnUpdate = tk.Button(self, width = 12)
        self.btnUpdate["command"] = ""
        self.btnUpdate["text"] = "Update Selected"
        self.btnUpdate.grid(row=5,column=4)
        self.btnDelete = tk.Button(self, width = 12)
        self.btnDelete["command"] = ""
        self.btnDelete["text"] = "Delete Selected"
        self.btnDelete.grid(row=6,column=4)
        self.btnClose = tk.Button(self, text="Close", fg="red", command=self.master.destroy, width=12)
        self.btnClose.grid(row=7,column=4)

        self.listbox = tk.Listbox(self, height=9,width=35)
        self.listbox.grid(row=2,column=0,rowspan=6,columnspan=2)

        self.scrollbar= tk.Scrollbar(self)
        self.scrollbar.grid(row=2,column=2,rowspan=6)
        self.listbox.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.listbox.yview)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
