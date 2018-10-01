from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemyUserDatastore, Security
from flask_security import current_user
from flask import redirect, url_for, request


app = Flask(__name__) #__name__ это имя теукщего файла app.py (необходимо указывать это отталкивающая точка)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

### Admin ###
from models import *

class AdminView(ModelView):
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, **kwargs):
        return redirect(url_for('security.login', next=request.url ))


admin = Admin(app)
admin.add_view(AdminView(Post, db.session()))
admin.add_view(AdminView(Tag, db.session()))

###flask_security

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
