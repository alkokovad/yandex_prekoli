from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def first_output():
    return "Миссия Колонизация Марса"


@app.route('/index')
def second_output():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def advertising():
    ad_list = ["Человечество вырастает из детства.",
               "Человечеству мала одна планета.",
               "Мы сделаем обитаемыми безжизненные пока планеты.",
               "И начнем с Марса!",
               "Присоединяйся!"]
    return '</br>'.join(ad_list)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                    <h7></br>Вот она какая, красная планета!</h7>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
