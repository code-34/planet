from flask.templating import render_template
import pymysql
import mysql.connector
#database connection
connection = mysql.connector.connect(host="localhost", user="root", password="", database="planet")
cursor = connection.cursor()
#inserting data to db
def add_text(name,mobile,address,item,serial,detail,service,date,amount):
    cursor.execute("INSERT INTO Data(Id,Name,Mobile,Address,Item,Serial,Detail,Service,Date,Amount) VALUES (DEFAULT, %s,%s,%s, %s,%s,%s,%s,%s,%s)", (name,mobile,address,item,serial,detail,service,date,amount))
    connection.commit()
    return 1

def search_mobile(mobile):
    cursor.execute("SELECT * FROM Data WHERE Mobile=%s",(mobile,))
    data=cursor.fetchall()
    return data


def search_serial(serial):
    cursor.execute("SELECT * FROM Data where Serial=%s",(serial,))
    data=cursor.fetchall()
    return data

def search_date(mobile,sdate,edate):
    if mobile=="":
        cursor.execute("Select * from Data where Date Between %s and %s", (sdate,edate))
        data=cursor.fetchall()
        return data
    else:
        cursor.execute("Select * from Data where Date Between %s and %s and Mobile=%s", (sdate,edate,mobile))
        data=cursor.fetchall()
        return data



def dbrun():
    cursor.execute("""create Table Data(
        Id int not null auto_increment primary Key, 
        Name varchar(50), 
        Mobile varchar(10), 
        Address Varchar(150),
        Item varchar(50),
        Serial Varchar(50),
        Detail Varchar(100),
        Service Varchar(20),
        Date date,
        Amount int(10)
         )""")
    return 1
