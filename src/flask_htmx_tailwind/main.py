from flask import Blueprint, render_template, request

from .todo import todos

main = Blueprint('main', __name__)


@main.route("/")
def homepage():
    return render_template('index.html')


@main.route('/search', methods=['POST'])
def search():
    search_term = request.form.get('search')

    if not search_term:
        return render_template('todo.html', todos=[])

    res_todos = []
    for todo in todos:
        if search_term in todo['title']:
            res_todos.append(todo)

    return render_template('todo.html', todos=res_todos)
