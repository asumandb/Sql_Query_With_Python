import pyodbc

connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=.;"
    "Database=master;" 
    "Trusted_Connection=yes;",
    autocommit= True

)
cursor = connection.cursor()

cursor.execute("CREATE DATABASE LibraryDB")
cursor.execute("USE LibraryDB")
print("Veritabanı oluşturuldu: LibraryDB")


create_table_query = """
CREATE TABLE Books(
Id INT IDENTITY(1,1) PRIMARY KEY,
Title NVARCHAR(255),
Author NVARCHAR(255),
Price DECIMAL(10,2),
Stock INT
)
"""
cursor.execute("DROP TABLE IF EXISTS Books")
cursor.execute(create_table_query)
print("Books tablosu oluşturuldu.")
connection.commit()

insert_query = "INSERT INTO Books(Title, Author, Price, Stock) VALUES(?,?,?,?)"
books = [
    ('The Catcher in the Rye', 'J. D. Salinger', 29.99, 15),
    ('To Kill a Mockingbird', 'Harper Lee', 24.99, 10), 
    ('1984', 'George Orwell', 19.99, 20)
]

cursor.executemany(insert_query, books)
print("Veriler oluşturuldu.")
connection.commit()

update_query = "UPDATE Books SET Stock = 25 WHERE Title = '1984'"
cursor.execute(update_query)
print("1984 kitabının stok miktarı güncellendi.")
connection.commit()

delete_query = "DELETE FROM Books WHERE Title = 'The Catcher in the Rye'"
cursor.execute(delete_query)
print("'The Catcher in the Rye' kitabı silindi.")
connection.commit()

alter_table_query = "ALTER TABLE Books ADD Genre NVARCHAR(50)"
cursor.execute(alter_table_query)
print("Genre sütunu eklendi.")
connection.commit()

cursor.execute("SELECT  * FROM Books")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM Books WHERE Price < 20")
for row in cursor.fetchall():
    print(row)

#cursor.execute("DROP TABLE Books")
#print("Books tablosu silindi.")
#connection.commit()
