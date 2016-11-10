from flask import render_template,request
from app import app
from models import Todo,todoform

@app.route('/')
def index():
    form = todoform()
    todos = Todo.objects.order_by('-time')
    return render_template("index.html",todos=todos,form = form)

@app.route('/add', methods = ['POST',])
def add():
    form = todoform(request.form)
    if form.validate():
        content = form.content.data
        todo = Todo(content=content)
        todo.save()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos=todos, form=form)

@app.route('/done/<string:id>')
def done(id):
    form = todoform()
    todo = Todo.objects.get_or_404(id=id)
    todo.status = 1
    todo.save() # must save
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos=todos, form=form)

@app.route('/undone/<string:id>')
def undone(id):
    form = todoform()
    todo = Todo.objects.get_or_404(id=id)
    todo.status = 0
    todo.save() # must save
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos=todos, form=form)

@app.route('/delete/<string:id>')
def delete(id):
    form = todoform()
    todo = Todo.objects.get_or_404(id=id)
    todo.delete() # must save
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos=todos, form=form)

@app.errorhandler(404)
def not_found(error): # takes one argument
    return render_template('404.html')
