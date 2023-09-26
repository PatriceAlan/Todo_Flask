import os
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv  # Add this line

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__, template_folder='app_package/templates')

# Configure the database connection using environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{os.environ['MYSQL_ROOT_PASSWORD']}@{os.environ['MYSQL_HOST']}/{os.environ['MYSQL_DATABASE']}"
db = SQLAlchemy(app)

# Create Models
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    search_query = request.args.get('search', '')  # Get the search query from the URL

    if search_query:
        # If a search query is provided, filter tasks by title containing the query
        todo_list = Todo.query.filter(Todo.title.contains(search_query)).all()
    else:
        # If no search query, fetch all tasks
        todo_list = Todo.query.all()

    total_todo = Todo.query.count()
    completed_todo = Todo.query.filter_by(complete=True).count()
    uncompleted_todo = total_todo - completed_todo

    return render_template('index.html', **locals())

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit() 
    return redirect(url_for('index'))

@app.route('/update/<int:id>')
def update(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    with app.app_context():  # Create an application context
        db.create_all()  # Create database tables
    app.run(debug=True)
