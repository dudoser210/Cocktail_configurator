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


def registration(password,name):
    mycursor.execute(f"INSERT INTO userdata (name,password) VALUES({name},{password}")

c = registration("12345pupup","Papapem",)