from db import run_query_select, run_update_query

run_update_query("""CREATE TABLE IF NOT EXISTS authors (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  country TEXT NOT NULL
);""")

run_update_query("""CREATE TABLE IF NOT EXISTS books (
  id         INTEGER PRIMARY KEY,
  title       TEXT    NOT NULL,
  author_id    INTEGER,
  year     INTEGER    NOT NULL,
  FOREIGN KEY (author_id) REFERENCES authors(id)
);""")

run_update_query("""INSERT INTO authors VALUES
  (1,'George Orwell','UK'),
  (2,'Gabriel García Márquez','Colombia'),
  (3,'Haruki Murakami','Japan');
""")
run_update_query("INSERT INTO books (id, title, author_id, year) VALUES (?, ?, ?, ?)", (1, '1984', 1, 1949))
run_update_query("INSERT INTO books (id, title, author_id, year) VALUES (?, ?, ?, ?)", (2, 'Animal Farm',1, 1945))
run_update_query("INSERT INTO books (id, title, author_id, year) VALUES (?, ?, ?, ?)", (3, 'One Hundred Years of Solitude', 2, 1967))
run_update_query("INSERT INTO books (id, title, author_id, year) VALUES (?, ?, ?, ?)", (4, 'Norwegian Wood',3, 1987))

print("All Books")
books = run_query_select("SELECT * FROM books")
for b in books:
    print(b)

print("Books from 1960")
books = run_query_select("SELECT * FROM books WHERE year > 1960")
for b in books:
    print(b)

print("books and authors")
books = run_query_select("""SELECT b.title, a.name
                            FROM   books b
                            INNER JOIN authors a ON b.author_id = a.id""")
for b in books:
    print(b)

print("Add new book")
try:
    title = input("Title: ")
    author_id = int(input("Author ID: "))
    year = int(input("Year: "))

    run_update_query(
    """
    INSERT INTO books (title, author_id, year)
    VALUES (?, ?, ?)
    """,
    (title, author_id,year)
    )
    print("Book added")
except Exception as e:
    print("Error:", e)
