from __future__ import with_statement
from fabric.api import *
#from fabric.contrib.project import rsync_project
# from fabric.contrib.console import confirm
# from fabric.contrib.files import exists
# from fabric.operations import prompt

import os
home = os.path.expanduser("~")


env.project_name = "prject_name_goes_here"
env.project_dir = os.path.join(home, 'Sites', 'django', env.project_name)


def runserver():
    with settings(warn_only=True):
        with cd(oenv.project_dir):
            local('source bin/activate')
            local('export PYTHONPATH=config.environments.development')
            syncdb()
            local("python manage.py runserver")


def validate():
    local("python manage.py validate")


def shell():
    local("python manage.py shell")


def syncdb():
    local("python manage.py syncdb")
