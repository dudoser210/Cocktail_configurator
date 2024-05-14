import pymysql.cursors

mydb = pymysql.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "newuser",
    password = "QWERTY123456qwerty!",
    database = "test",
    cursorclass = pymysql.cursors.DictCursor
)

mycursor = mydb.cursor()

def reg(name, password):
    with mydb.cursor() as cursor:
        insert_query = f"INSERT INTO userdata (nickname, password) VALUES ('{name}', '{password}');"
        cursor.execute(insert_query)
        mydb.commit()
c = reg('ututut','3uy3y3y3')