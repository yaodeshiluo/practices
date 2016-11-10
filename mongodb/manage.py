# from flask_script import Manager
# from app import app
# from models import User
#
# manage = Manager(app)
#
# @manage.command
# def save():
#     user = User('jike','jike@qq.com')
#     user.save()
#
# @manage.command
# def query():
#     users = User.query_users()
#     for user in users:
#         print user
#
# if __name__ == '__main__':
#     manage.run()
from flask_script import Manager
from app import app
from models import User

manage = Manager(app)

@manage.command
def save():
    user = User('jike2','jike2@qq.com')
    # user.save()
    user.save()

@manage.command
def query():
    # users = User.query_users()
    users = User.objects.all()
    for user in users:
        print user

if __name__ == '__main__':
    manage.run()
