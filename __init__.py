import os
import pyodbc
from flask import Flask ,request
from sqlalchemy import create_engine,Column,String,Integer,CHAR,text
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy.engine import URL
from dotenv import load_dotenv
from models import Person
import urllib.parse

query = text("SELECT TOP(10) * FROM Person.Person")
q2=text("SET IDENTITY_INSERT kastamar ON")
table= text("""CREATE TABLE kastamar (
    Customer_ID INT PRIMARY KEY,
    Firstname NVARCHAR(105) NOT NULL,
    Lastname NVARCHAR(105) NOT NULL,
    Password NVARCHAR(105) NOT NULL,
    [E-mail] NVARCHAR(105) NOT NULL
)""")
CREATE_t0 = text(" CREATE TABLE gondu(id INT PRIMARY KEY, name NVARCHAR(200))")
create_table= text("CREATE TABLE toadys(id INT PRIMARY KEY, name TEXT)")
CREATE_t2 = (" CREATE TABLE IF NOT EXISTS temp(city_id INTEGER, tempreture REAL ,date TIMESTAMP, FOREIGN KEY(city_id) REFERENCES city(id) ON DELETE CASCADE );")


app = Flask(__name__)
Base = declarative_base()
load_dotenv()

server = os.getenv("SERVER")
db = os.getenv("DATABASE")
driver = os.getenv("DRIVER")
uid = os.getenv("USER")
pwd = os.getenv("PASSWORD")



params = urllib.parse.quote_plus(
    f"DRIVER={{{driver}}};"
    f"SERVER={server};"
    f"DATABASE={db};"
    "Trusted_Connection=yes;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")



#raw execution
connection = engine.connect()
print(connection)
result = connection.execute(q2)
connection.execute(q2)
connection.execute(CREATE_t0)

# for r in resut:
#     print(r)
connection.commit()
connection.close()

# # Base.metadata.create_all(bind = engine)
# Session = sessionmaker(bind=engine)
# session = Session()
# per1 = Person("kf","xoni987","fgdj@gui.com","fgdj@gui.com")
# session.add(per1)
# session.commit()
#