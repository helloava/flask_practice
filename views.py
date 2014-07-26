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
	
	htmltext = urllib.urlopen(rocurl)

	soup = BeautifulSoup(htmltext, from_encoding="urf-8")

	authors = []

	for tag in soup.select(".main_img_title"):
		authors.append(tag.get_text())

	for author in authors:
		return author.encode("utf8")
