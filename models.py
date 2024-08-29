from sqlalchemy import create_engine,Column,String,Integer,CHAR,NVARCHAR
from sqlalchemy.ext.declarative import declarative_base
import os
import urllib
from dotenv import load_dotenv

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

class Person(Base):
    __tablename__= "kastamar"
    c_id = Column("Customer_ID" , Integer ,unique=True,nullable=True,primary_key=True,)
    F_name = Column("Firstname", NVARCHAR(105) ,nullable=False)
    L_name = Column("lastname", NVARCHAR(105),nullable=False)
    Password = Column("Password",NVARCHAR(105) ,nullable=False)
    email  = Column("E-mail",NVARCHAR(105),nullable=False)
    # Purchase = relationship('',backref)

    def __init__(self,c_id,fname,lname,pwd,email):
        self.c_id = c_id
        self.F_name = fname
        self.L_name = lname
        self.Password = pwd
        self.email = email

    def __repr__(self):
        return f' User:  , {self.F_name} {self.F_name} , Email: {self.email} has been Created '



# Base.metadata.create_all(bind=engine)