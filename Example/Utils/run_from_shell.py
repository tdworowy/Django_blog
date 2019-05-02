import os

path_ = os.path.dirname(os.path.abspath(__file__))
WINIDOWS_DRIVE = 'D'

def run_from_shell_script(path, script):
    path_script = path_ + '\\' + script
    print(path)
    print(path_script)
    commend = "%s: && cd %s && python manage.py shell %s" % (WINIDOWS_DRIVE, path, path_script)
    print(commend)
    os.system(commend)


def run_from_shell(path, script):
    print(path)
    commend = "%s: && cd %s && python manage.py shell %s" % (WINIDOWS_DRIVE, path, script)
    print(commend)
    os.system(commend)


def run(path, script):
    print(path)
    commend = "cd %s && python manage.py shell %s" % (path, script)
    print(commend)
    os.system(commend)
