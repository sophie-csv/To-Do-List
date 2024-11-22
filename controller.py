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
    return render_template('index.html', tasklist=tasklist)


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




if __name__ == '__main__':
    app.run()
