from flask import render_template, Flask, request, url_for
from apps import app

from flaskext import wtf
from flaskext.wtf import Form, TextField, SubmitField, \
    validators, ValidationError

import urllib2


class ContactForm(Form):
    sort = TextField(
        "sort", [validators.Required("Please enter sorting number")])
    submit = SubmitField("send")


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('index.html', form=form)
        else:
            def ed(form.sort.data):
                a = urllib2.urlopen("http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=%d" % (
                    form.sort.data))
                html = a.read().split('<ul class="type06_headline">')

                for data in html[1:]:
                    print data.split('</dd>')[9]

    return render_template('index.html', form=form)
