from flask import Flask, render_template, request, redirect, url_for, session

from model import tasklist_DAL as db

app = Flask(__name__, template_folder='view/templates', static_folder='view/static')

app.secret_key = "random_thing"




@app.route('/')
def index():
    if 'logged_in' not in session:
        return render_template('login_form.html')

    username = session['username']
    tasklist = db.get_tasks(username)
    return render_template('index.html', tasklist=tasklist, username=username)


@app.route('/add_task', methods=['POST'])
def add_task():

    task = request.form['new_task']
    username = session['username']
    db.add_task(username, task)
    return redirect(url_for('index'))


@app.route('/remove_task', methods=['POST'])
def remove_task():

    task = request.form['removed_task']
    username = session['username']
    db.remove_task(username, task)
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    users = db.get_users_as_list()
    username = request.form['username']
    if username in users:
        session['logged_in'] = True
        session['username'] = username
        return redirect(url_for('index'))
    return render_template('login_form.html', error="Username not found!")

@app.route('/login_form')
def show_login_form():
    if "logged_in" in session:
        return redirect(url_for('index'))
    error = request.args.get('error')
    if error is None:
        error = ''
    return render_template('login_form.html', error=error)

@app.route('/register_form')
def show_register_form():
    if "logged_in" in session:
        return redirect(url_for('index'))
    error = request.args.get('error')
    if error is None:
        error = ''
    return render_template('register_form.html', error=error)


@app.route('/register', methods=['POST'])
def register():
    users = db.get_users_as_list()
    username = request.form['username']
    if username in users:
        render_template('register_form.html', error="Username already registered!")
    db.add_new_user(username)
    return render_template('login_form.html', error="New user registered!")

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run()
