import sqlite3

conn = sqlite3.connect('sophia.db')
cursor = conn.cursor()



query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)


# # # to insert values
# query = "INSERT INTO sys_command VALUES (null,'Postman', 'C:\\Users\\User\\AppData\\Local\\Postman\\Postman.exe')"
# cursor.execute(query)
# conn.commit()
# conn.close()  # Don't forget to close the connection when done


query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

# # to insert values
query = "INSERT INTO web_command VALUES (null,'gmail', 'https://gmail.com')"
cursor.execute(query)
conn.commit()
conn.close()  # Don't forget to close the connection when done