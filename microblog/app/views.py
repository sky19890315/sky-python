from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'ken'}
    posts = [
        {
            'author': {'nickname': 'ken win'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'katy'},
            'body': 'The Avenger movie was so cool!'
        }
    ]
    year = {'year': '2017-12-12'}
    return render_template('index.html', title='Home', user=user, posts=posts, year=year)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenId="' + form.openid + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form,
                           providers = app.config['OPENID_PROVIDERS'])






















