# Libraries
import tkinter as tk
# Back-end script
import backend

# start of the interface
class Application(tk.Frame):

    # inicial definitions
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
        master.wm_title("BookStore")

    # Start of actions for buttons
    def get_row(self, event):
        try:
            global selected_tuple
            index = self.listbox.curselection()[0]
            selected_tuple = self.listbox.get(index)
            self.entryTitle.delete(0, tk.END)
            self.entryTitle.insert(tk.END, selected_tuple[1])
            self.entryAuthor.delete(0, tk.END)
            self.entryAuthor.insert(tk.END, selected_tuple[2])
            self.entryYear.delete(0, tk.END)
            self.entryYear.insert(tk.END, selected_tuple[3])
            self.entryISBN.delete(0, tk.END)
            self.entryISBN.insert(tk.END, selected_tuple[4])
        except IndexError:
            pass
            
    def view_command(self):
        self.listbox.delete(0,tk.END)
        for row in backend.view():
            self.listbox.insert(tk.END,row)
    
    def search_command(self):
        self.listbox.delete(0,tk.END)
        for row in backend.search(self.inputTitle.get(),self.inputAuthor.get(),self.inputYear.get(),self.inputISBN.get()):
            self.listbox.insert(tk.END, row)
    
    def add_command(self):
        backend.insert(self.inputTitle.get(),self.inputAuthor.get(),self.inputYear.get(),self.inputISBN.get())
        self.listbox.delete(0, tk.END)
        self.search_command()

    def delete_command(self):
        backend.delete(selected_tuple[0])
        self.view_command()
    
    def update_command(self):
        line = selected_tuple
        backend.update(line[0],self.inputTitle.get(),self.inputAuthor.get(),self.inputYear.get(),self.inputISBN.get())
        self.view_command()
    
    # End Actions for Buttons
    
    #Interface Widgets
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
        self.entryYear.grid(row=1, column=1)
        self.inputAuthor = tk.StringVar()
        self.entryAuthor = tk.Entry(self)
        self.entryAuthor["textvariable"] = self.inputAuthor
        self.entryAuthor.grid(row=0, column=4)
        self.inputISBN = tk.StringVar()
        self.entryISBN = tk.Entry(self)
        self.entryISBN["textvariable"] = self.inputISBN
        self.entryISBN.grid(row=1,column=4)

        self.btnView = tk.Button(self, width=12)
        self.btnView["command"] = self.view_command
        self.btnView["text"] = "View All"
        self.btnView.grid(row=2,column=4)
        self.btnSearch = tk.Button(self, width = 12)
        self.btnSearch["command"] = self.search_command
        self.btnSearch["text"] = "Search entry"
        self.btnSearch.grid(row=3,column=4)
        self.btnEntry = tk.Button(self, width = 12)
        self.btnEntry["command"] = self.add_command
        self.btnEntry["text"] = "Add entry"
        self.btnEntry.grid(row=4,column=4)
        self.btnUpdate = tk.Button(self, width = 12)
        self.btnUpdate["command"] = self.update_command
        self.btnUpdate["text"] = "Update Selected"
        self.btnUpdate.grid(row=5,column=4)
        self.btnDelete = tk.Button(self, width = 12)
        self.btnDelete["command"] = self.delete_command
        self.btnDelete["text"] = "Delete Selected"
        self.btnDelete.grid(row=6,column=4)
        self.btnClose = tk.Button(self, text="Close", fg="red", command=self.master.destroy, width=12)
        self.btnClose.grid(row=7,column=4)

        self.listbox = tk.Listbox(self, height=9,width=35)
        self.listbox.grid(row=2,column=0,rowspan=6,columnspan=2)
        self.listbox.bind('<<ListboxSelect>>', self.get_row)

        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=2,column=2,rowspan=6)
        self.listbox.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.listbox.yview)
        #End of interface Wigets

root = tk.Tk()
app = Application(master=root)
app.mainloop()
