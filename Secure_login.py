import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def setup_db():
    # This creates the users.db file + table if it doesn't exist
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (username TEXT, password TEXT)''')
    
    # Add a test user: username = admin, password = password123
    # We hash the password before saving
    cursor.execute("INSERT OR IGNORE INTO users VALUES (?, ?)", 
                   ('admin', hash_password('password123')))
    
    conn.commit()
    conn.close()
    print("Database setup complete. Test user: admin / password123")

def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # FIX 1: Parameterized query prevents SQL Injection
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, hash_password(password)))

    result = cursor.fetchone()
    conn.close()
    
    if result:
        return "Login Successful"
    else:
        return "Login Failed"

# --- RUN THE PROGRAM ---
setup_db() # Run this once to create the DB

user_input = input("Enter username: ")
pass_input = input("Enter password: ")
print(login(user_input, pass_input))