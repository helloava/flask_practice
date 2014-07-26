from flask import render_template, Flask, request
from apps import app

import urllib2


@app.route('/')
def get():
    return render_template("index.html")


@app.route('/crawl', methods=['GET', 'POST'])
def crawl():
	rocurl = urllib2.urlopen("http://rocketpun.ch/companies/%d/"%(request.form["page"])

	html = rocurl.read().split('<div class="main_img_title">')


	for data in html[1:]:
		return data.split('</div>')[0]
