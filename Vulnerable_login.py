import sqlite3

def setup_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (username TEXT, password TEXT)''')
    cursor.execute("INSERT OR IGNORE INTO users VALUES (?, ?)", 
                   ('admin', 'admin123')) # note: plain text for vulnerable version
    conn.commit()
    conn.close()
    print("Database ready. Test user: admin / admin123")

setup_db() # <--- ADD THIS LINE HERE

def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULN 1: SQL Injection
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return "Login Successful"
    else:
        return "Login Failed"

user_input = input("Enter username: ")
pass_input = input("Enter password: ")
print(login(user_input, pass_input))