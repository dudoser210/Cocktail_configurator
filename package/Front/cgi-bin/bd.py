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

def acount_id_by_name(name):
    with mydb.cursor() as cursor:
        name_id = f"select id from userdata where nickname = '{name}'"
        cursor.execute(name_id)
        name_id = cursor.fetchall()
        mydb.commit()
    return str(name_id).split(" ")[1].split("}")[0]

def coctail_id_by_name(name):
    with mydb.cursor() as cursor:
        name_id = f"select id from cocteildata where name = '{name}'"
        cursor.execute(name_id)
        name_id = cursor.fetchall()
        mydb.commit()
    return str(name_id).split(" ")[1].split("}")[0]

def ingredient_id_by_name(name):
    with mydb.cursor() as cursor:
        name_id = f"select id from igredient where name = '{name}'"
        cursor.execute(name_id)
        name_id = cursor.fetchall()
        mydb.commit()
    return str(name_id).split(" ")[1].split("}")[0]

def acount_name_by_id(id):
    with mydb.cursor() as cursor:
        id_name = f"select nickname from userdata where id = '{id}'"
        cursor.execute(id_name)
        id_name = cursor.fetchall()
        mydb.commit()
    return str(id_name).split(" ")[1].split("}")[0]

def cocteil_name_by_id(id):
    with mydb.cursor() as cursor:
        id_name = f"select name from cocteildata where id = '{id}'"
        cursor.execute(id_name)
        id_name = cursor.fetchall()
        mydb.commit()
    return str(id_name).split(" ")[1].split("}")[0]

def ingredient_name_by_id(id):
    with mydb.cursor() as cursor:
        id_name = f"select name from igredient where id = '{id}'"
        cursor.execute(id_name)
        id_name = cursor.fetchall()
        mydb.commit()
    return str(id_name).split(" ")[1].split("}")[0]

def search_ingrideents(name):
    with mydb.cursor() as cursor:
        search_ings = f"select id from igredient where name like'{name}%'"
        cursor.execute(search_ings)
        search_ings = cursor.fetchall()
        mydb.commit()
        ingredinets = []
        for i in range(len(search_ings)):
            ing = str(search_ings[i]).split(" ")[1].split("}")[0]
            ingredinets.append(ing)
        return ingredinets


def search_coctail_name(name):
    with mydb.cursor() as cursor:
        search_coc = f"select id from cocteildata where name like'{name}%'"
        cursor.execute(search_coc)
        search_coc = cursor.fetchall()
        mydb.commit()
        cocteils = []
        for i in range(len(search_coc)):
            ing = str(search_coc[i]).split(" ")[1].split("}")[0]
            cocteils.append(ing)
        return cocteils


def search_coctail_ingredients():
    pass

def add_like():
    pass

def top_drinks():
    pass

