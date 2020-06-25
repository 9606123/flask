#!/usr/bin/env python
import os
from app import create_app,db
from flask_script import Server, Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app('local')
# print(app.config)
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
manager.add_command("runserver",  Server(host="127.0.0.1", port=7000))

if __name__ == '__main__':
    manager.run()
