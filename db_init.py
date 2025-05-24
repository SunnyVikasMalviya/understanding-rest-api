import sqlite3

# Connect to a database (it will be created if it doesn't exist)
conn = sqlite3.connect('myRestDB.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')
# Use DB Browser to view the database and table structure

# Insert some data
users_data = [
    ('Alice', 30),
    ('Bob', 25),
    ('Charlie', 35)
]
cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users_data)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("SQLite database 'myRestDB.db' created with 'users' table and sample data.")