import pyodbc
import pandas as pd

user = "daniel"
password = "G0207b0803"
database = "Northwind"
server = "tcp:danielsqlsever0520.database.windows.net,1433"
odbcserver = "{ODBC Driver 18 for SQL Server}"

conn = pyodbc.connect(f'Driver={odbcserver};Server={server};Database={database};Uid={user};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
#=====
#1
df = pd.read_sql("select * from Products", conn)
# print(df)
print(df.UnitsInStock.describe()) #可分析資料的統計量
#2
df = pd.read_sql("select Country from Employees", conn)
# print(df)
print(df.Country.value_counts()) #可分析國籍資料的累計值
#3
df = pd.read_sql("select Title from Employees", conn)
# print(df)
print(df.Title.value_counts()) #可分析職位資料的累計值
df = pd.read_sql("select * from Customers", conn)
# print(df)
print(df.Title.value_counts()) #可分析職位資料的累計值

#=====
conn.close()