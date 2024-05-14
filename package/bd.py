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
        search_name = f"select nickname from userdata where nickname = '{name}'"
        cursor.execute(search_name)
        check_name = cursor.fetchall()
        mydb.commit()
        print(check_name)
        if check_name != ():
                return print("Такое имя занято")
        else:
            insert_query = f"INSERT INTO userdata (nickname, password) VALUES ('{name}', '{password}');"
            cursor.execute(insert_query)
            mydb.commit()
c = reg("Anna","wrw")

def enter(name,password):
    with mydb.cursor() as cursor:
        insert_query = f"select password from userdata where nickname = '{name}'"
        cursor.execute(insert_query)
        check_pass = cursor.fetchall()
        mydb.commit()
        if str(check_pass).split("'")[3] == password:
            return True
        else:
            return False

def create_coctail():
    pass

def search_ingrideents():
    pass

def search_coctail_name():
    pass

def search_coctail_ingredients():
    pass

def top_drinks():
    pass