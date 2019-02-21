import mysql.connector
db=mysql.connector.connect (
    host='localhost',
    user='root',
    password='abc123',
    database='new'
)
x=db.cursor()
x.execute("insert into product(id,name,description,price) values('p105','tv','Mi-32',13000)")
db.commit()
db.rollback()
db.close()