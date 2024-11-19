from flask import Flask, request, render_template, redirect, url_for
from model import DAL as db

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_task')
def add():
    task = request.args.get('the_task')
    db.add_task(task)
    return redirect(url_for('index', task=task))


if __name__ == '__main__':
    app.run()
