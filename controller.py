from flask import Flask, render_template, request, redirect, url_for

from model import tasklist_DAL as db

app = Flask(__name__, template_folder='view/templates', static_folder='view/static')


@app.route('/')
def index():
    tasklist = db.get_tasks()
    return render_template('index.html', tasklist=tasklist)


@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['new_task']
    db.add_task(task)
    return redirect(url_for('index'))


@app.route('/remove_task', methods=['POST'])
def remove_task():
    task = request.form['removed_task']
    db.remove_task(task)
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']



if __name__ == '__main__':
    app.run()
