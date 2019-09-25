from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Anna'}
    posts = [
        {
            'author': {'username': 'HeiHei'},
            'body': 'Yay its working.....jk its not!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Hi my name is Susan and I work in accounting..'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)