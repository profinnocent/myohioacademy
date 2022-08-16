import sqlite3

with sqlite3.connect("studentsdb") as sdb:
    c = sdb.cursor()

# Create Table
# c.execute("CREATE TABLE students(id integer AUTO_INCREMENT PRIMARY KEY, fullname text, department text, level integer, gender text, email text, password text)")

# Create Table2
# c.execute("CREATE TABLE sec(id int)")

# Drop Table2
# c.execute("DROP TABLE sec")

# Table2 insert
# g = [5]
# print(g[0])
# val = str(g[0])
# c.execute(("INSERT INTO sec(id)VALUES(?)"),val)

# Table2 delete
# c.execute("DELETE FROM sec")

# Fetech Table2
c.execute("select * from sec")
result = c.fetchall()
print(result)
for res in result:
    print(result[0])


# Alter Table
# c.execute("CREATE TABLE students ALTER id PRIMARY KEY IDENTITY(0,1)")

# Drop Table
# c.execute("DROP TABLE students")

# Truncate Table
# c.execute("TRUNCATE TABLE students")

# try:
#     c.execute("TRUNCATE TABLE students")
#     print("Table data truncated")
# except ConnectionError:
#     print("Truncate not executed.")

# Select table
# c.execute("select * from students")
# result = c.fetchall()
# print(result)


# print(len(result))
# print(len(result[0]))

# INSERT
# c.execute("INSERT INTO students (id,fullname, department, level, gender, email, password)VALUES(?,?,?,?,?,?,?)", (1, 'Prof1', 'Biology', 100, 'Male', 'prof1@gmail.com', '1000'))


sdb.commit()
sdb.close()