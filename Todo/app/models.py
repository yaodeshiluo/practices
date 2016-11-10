from app import db
from datetime import datetime
from flask_mongoengine.wtf import model_form

class Todo(db.Document):
    content = db.StringField(required=True, max_length=20)
    time = db.DateTimeField(default=datetime.now())
    status = db.IntField(default=0)

    def __str__(self):
        return 'content:{},time:{},status:{}'.format(self.content,self.time,self.status)

todoform = model_form(Todo)
