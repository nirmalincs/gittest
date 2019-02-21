def connection():
    import mysql.connector
    a= mysql.connector.connect (
    host='localhost',
    user='root',
    password='abc123',
    database='new')
    return a

#print(db)

def read():
    con=connection()
    mycursor=con.cursor()
    mycursor.execute("select * from product")
    result = mycursor.fetchall()
    con.commit()
    print (result)
    for x in result:
        print(x)

    #con.commit()

    #x=con.cursor()
    #x.execute("select * from cust")
    #for y in x:

#        print(y)
#y=x.fetchone()
#m=x.fetchone()
#print(y)
#print(m)
read()