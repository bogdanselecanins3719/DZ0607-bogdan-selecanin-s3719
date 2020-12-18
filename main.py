from flask import Flask, render_template, redirect, url_for, request, session
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import hashlib
import time
import os
import mysql.connector


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dz'
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raspored"
)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/raspored')
def raspored():
    mc = mydb.cursor()
    mc.execute("SELECT * FROM raspored")
    res = mc.fetchall()
    mc2 = mydb.cursor()
    mc2.execute("SELECT DISTINCT nastavnik FROM raspored")
    nastavnici = mc2.fetchall()
    mc3 = mydb.cursor()
    mc3.execute("SELECT DISTINCT vreme FROM raspored")
    ucionice = mc3.fetchall()

    return render_template("index.html", raspored=res, nastavnici=nastavnici, ucionice=ucionice)


@app.route('/nastavnik/<ime>')
def nastavnik(ime):
    mc = mydb.cursor()
    mc.execute("SELECT * FROM raspored WHERE nastavnik='"+ime+"' ")
    res = mc.fetchall()
    mc2 = mydb.cursor()
    mc2.execute("SELECT DISTINCT nastavnik FROM raspored")
    nastavnici = mc2.fetchall()
    mc3 = mydb.cursor()
    mc3.execute("SELECT DISTINCT vreme FROM raspored")
    ucionice = mc3.fetchall()
    return render_template("index.html", raspored=res, nastavnici=nastavnici, ucionice=ucionice)


@app.route('/ucionica/<naziv>')
def ucionica(naziv):
    mc = mydb.cursor()
    mc.execute("SELECT * FROM raspored WHERE vreme='"+naziv+"' ")
    res = mc.fetchall()
    mc2 = mydb.cursor()
    mc2.execute("SELECT DISTINCT nastavnik FROM raspored")
    nastavnici = mc2.fetchall()
    mc3 = mydb.cursor()
    mc3.execute("SELECT DISTINCT vreme FROM raspored")
    ucionice = mc3.fetchall()
    return render_template("index.html", raspored=res, nastavnici=nastavnici, ucionice=ucionice)


if __name__ == '__main__':
    app.run(debug=True)
