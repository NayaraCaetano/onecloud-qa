# -*- coding: utf-8 -*-

import subprocess
import os

from lettuce import before, after, world
from pyvirtualdisplay import Display
from splinter.browser import Browser

DISPLAY = Display(visible=0, size=(1024, 2000))


@before.all
def initial_setup():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.functional_test'

    world.base_url = 'http://localhost:7000'
    world.settings_test = '--settings=settings.functional_test'

    subprocess.call(["python", "manage.py", "migrate", world.settings_test])
    initialize_server()

    DISPLAY.start()

    world.pages = initialize_pages()
    world.users = initialize_users()


@before.each_feature
def setup_some_feature(feature):
    world.browser = Browser('chrome')
    world.browser.driver.set_window_size(1024, 3000)


@before.each_scenario
def initialize_scenario(scenario):
    subprocess.call(["python", "manage.py", "flush", world.settings_test, "--noinput"])
    subprocess.call(["python", "manage.py", "loaddata", "onecloud/fixtures/users.json", world.settings_test])


@after.each_step
def teardown_some_step(step):
    #  Todo: captura tela se erro, se acontecer
    pass


@after.each_feature
def feature_teardown(feature):
    world.browser.quit()


@after.all
def teardown_environment(total):
    print "Resultado:"
    print "%d Features\t(%d Passed)" % (total.features_ran, total. features_passed)
    print "%d Scenario\t(%d Passed)" % (total.scenarios_ran, total.scenarios_passed)
    print "%d Steps" % (total.steps)
    kill_processo('127.0.0.1:7000')

    DISPLAY.stop()


def kill_processo(busca):
    get_pid = 'ps -eo pid,command | grep "' + busca + '" | grep -v grep | awk \'{print $1}\''
    pid = int(subprocess.check_output(get_pid, shell=True))
    subprocess.call(['kill', '-SIGINT', str(pid)])


def initialize_server():
    subprocess.call(['touch', '/tmp/input.in', '/tmp/out.out', '/tmp/tmp.tmp'])
    file_input = open('/tmp/input.in', 'w')
    file_out = open('/tmp/out.out', 'w')
    file_tmp = open('/tmp/tmp.tmp', 'w')
    world.server = subprocess.Popen(
        ["python", "manage.py", "runserver", "--noreload", world.settings_test, '127.0.0.1:7000'],
        stdin=file_input, stdout=file_out, stderr=file_tmp
    )


def initialize_pages():
    return {
        "login_admin": "/admin/login/",
        "logout_admin": "/admin/logout/",
        "admin": "/admin/"
    }


def initialize_users():
    return {
        "admin": ['admin', '123']
    }
