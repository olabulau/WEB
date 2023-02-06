from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def return_colon():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Миссия Колонизация Марса</title>
                      </head>
                      <body>
                        <h1>Миссия Колонизация Марса</h1>
                      </body>
                    </html>"""


@app.route('/index')
def return_mission():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Миссия Колонизация Марса</title>
                      </head>
                      <body>
                        <h1>И на Марсе будут яблони цвести!</h1>
                      </body>
                    </html>"""


@app.route('/promotion')
def return_mission():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Миссия Колонизация Марса</title>
                      </head>
                      <body>
                        <h1>И на Марсе будут яблони цвести!</h1>
                      </body>
                    </html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.2')