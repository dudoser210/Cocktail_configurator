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
        if check_name != ():
                return print("Такое имя занято")
        else:
            insert_query = f"INSERT INTO userdata (nickname, password) VALUES ('{name}', '{password}');"
            cursor.execute(insert_query)
            mydb.commit()

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

def create_coctail(name,auther,ingredient_list,alcohol):
    with mydb.cursor() as cursor:
        search_name = f"select name from cocteildata where name = '{name}'"
        cursor.execute(search_name)
        check_name = cursor.fetchall()
        mydb.commit()
        if check_name != ():
                return print("Такое название занято")
        else:
            insert_query = f"INSERT INTO cocteildata (name, author, alcohol ) VALUES ('{name}', '{auther}', '{alcohol}');"
            cursor.execute(insert_query)
            mydb.commit()
            searach_cocteil_id = f"select MAX(id) from cocteildata"
            cursor.execute(searach_cocteil_id)
            searach_cocteil_id = cursor.fetchall()
            mydb.commit()
            searach_cocteil_id = str(searach_cocteil_id).split(" ")[1].split("}")[0]
            for i in range(len(ingredient_list)):
                insert_inredients = f"insert into ingredients_in_cockteil ( coctail_id, ingredient_id) Values ('{searach_cocteil_id}','{ingredient_list[i]}')"
                cursor.execute(insert_inredients)
                mydb.commit()


def search_ingrideents():
    pass

def search_coctail_name():
    pass

def search_coctail_ingredients():
    pass

def top_drinks():
    pass

