import pyodbc

user = "daniel"
password = "G0207b0803"
database = "Northwind"
server = "tcp:danielsqlsever0520.database.windows.net,1433"
odbcserver = "{ODBC Driver 18 for SQL Server}"

conn = pyodbc.connect(f'Driver={odbcserver};Server={server};Database={database};Uid={user};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
#=====
cursor = conn.cursor()
cursor.execute("select * from Products")
for row in cursor:
    # print(f'商品名稱:{row[1]}, 庫存量:{row[7]}') 
    print(f'商品名稱:{row.ProductName}, 庫存量:{row[7]}')    
#=====
conn.close()