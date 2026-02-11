import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('soul_library.db')
cursor = conn.cursor()

# Create tables

# Table for books
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    published_date DATE,
    genre TEXT,
    available_copies INTEGER NOT NULL DEFAULT 0
);
''')

# Table for members
cursor.execute('''
CREATE TABLE IF NOT EXISTS members (
    member_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    membership_date DATE NOT NULL,
    email TEXT UNIQUE,
    phone_number TEXT
);
''')

# Table for borrowing
cursor.execute('''
CREATE TABLE IF NOT EXISTS borrowing (
    borrow_id INTEGER PRIMARY KEY,
    member_id INTEGER,
    book_id INTEGER,
    borrow_date DATE NOT NULL,
    return_due_date DATE NOT NULL,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);
''')

# Table for returns
cursor.execute('''
CREATE TABLE IF NOT EXISTS returns (
    return_id INTEGER PRIMARY KEY,
    borrow_id INTEGER,
    return_date DATE NOT NULL,
    fine_amount REAL NOT NULL DEFAULT 0,
    FOREIGN KEY (borrow_id) REFERENCES borrowing(borrow_id)
);
''')

# Table for fines
cursor.execute('''
CREATE TABLE IF NOT EXISTS fines (
    fine_id INTEGER PRIMARY KEY,
    member_id INTEGER,
    amount REAL NOT NULL,
    date_issued DATE NOT NULL,
    paid BOOLEAN NOT NULL DEFAULT 0,
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);
''')

# Table for reservations
cursor.execute('''
CREATE TABLE IF NOT EXISTS reservations (
    reservation_id INTEGER PRIMARY KEY,
    member_id INTEGER,
    book_id INTEGER,
    reservation_date DATE NOT NULL,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);
''')

# Table for reports
cursor.execute('''
CREATE TABLE IF NOT EXISTS reports (
    report_id INTEGER PRIMARY KEY,
    member_id INTEGER,
    report_details TEXT NOT NULL,
    report_date DATE NOT NULL,
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);
''')

# Commit changes and close the connection
conn.commit()
conn.close()