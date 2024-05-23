import pyodbc

user = "daniel"
password = "G0207b0803"
database = "Northwind"
server = "tcp:danielsqlsever0520.database.windows.net,1433"
odbcserver = "{ODBC Driver 18 for SQL Server}"

conn = pyodbc.connect(f'Driver={odbcserver};Server={server};Database={database};Uid={user};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
#=====
cursor = conn.cursor()
cursor.execute("delete Customers where CustomerId=?", "GanAI")
conn.commit()
print(f"{cursor.rowcount}筆記錄刪除成功!")               
#=====
conn.close()