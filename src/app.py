import sqlite3
from flask import Flask, render_template
from datetime import date, timedelta
from random import shuffle

app = Flask(__name__)

@app.route('/')
def index():

    today = date.today()
    mon = today.month
    day = today.day

    if mon < 12:
        dec = date(today.year, 12, 1)
        remaining = dec - today
        return render_template('wait.html', days = remaining.days)

    con = sqlite3.connect('advent.db')
    cur = con.cursor()
    images = {}
    for row in cur.execute(f'SELECT * FROM images where id <= {day}'):
        images.update(dict([row]))
    order = list(range(1,25))
    shuffle(order)
    return render_template('index.html', images=images, order=order)
