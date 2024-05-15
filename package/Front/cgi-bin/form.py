#!/usr/bin/env python3
import cgi
from package.bd import reg

form = cgi.FieldStorage()
text1 = form.getfirst("name", "не задано")
text2 = form.getfirst("password", "не задано")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>TEXT_1: {}</p>".format(text1))
print("<p>TEXT_2: {}</p>".format(text2))

print("""</body>
        </html>""")

registration = reg(f"{text1}",f"{text2}")