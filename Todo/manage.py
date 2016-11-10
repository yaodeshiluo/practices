from app import app
from app.models import Todo
from flask_script import Manager

manager = Manager(app)

@manager.command
def save():
    todo = Todo(content = 'study flask')
    todo.save()

@manager.command
def query():
    todos = Todo.objects.all()
    for each in todos:
        print each

if __name__ == '__main__':
    manager.run()