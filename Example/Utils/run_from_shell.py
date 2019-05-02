import os

path_ = os.path.dirname(os.path.abspath(__file__))
def run_from_shell_script(path, script):
    path_script = path_ + '\\' + script
    print(path)
    print(path_script)
    commend = "cd %s && python manage.py shell %s" % (path, path_script)
    print(commend)
    os.system(commend)


def run_from_shell(path, script):
    print(path)
    commend = "cd %s && python manage.py shell %s" % (path, script)
    print(commend)
    os.system(commend)


def run(path, script):
    print(path)
    commend = "cd %s && python manage.py %s" % (path, script)
    print(commend)
    os.system(commend)
