import sqlite3

def connect():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    connection.commit()
    connection.close()

connect()

def insert(title,author,year,isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book")
    content = cursor.fetchall()
    connection.close()
    return content

def search(title="",author="",year="",isbn=""):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    content = cursor.fetchall()
    connection.close()
    return content

def delete(id):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM book WHERE id=?", (id,))
    connection.commit()
    connection.close()

def update(id,title,author,year,isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
    connection.commit()
    connection.close()


#insert("The Earth", "John Smith",1925,46414168432)
#delete(3)
#update(1,"The Moon","John Tablet",1926,6548432)
print(view())
