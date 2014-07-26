from flask import render_template, Flask, request
from apps import app

import urllib
from bs4 import BeautifulSoup


@app.route('/')
def get():
    return render_template("index.html")


@app.route('/crawl', methods=['GET', 'POST'])
def crawl():
    rocurl = "http://rocketpun.ch/companies/" + request.form["page"] + "/"
    return rocurl
