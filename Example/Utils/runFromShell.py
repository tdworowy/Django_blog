import os

path_ = os.path.dirname(os.path.abspath(__file__))


def runFromShellScript(path, script):
    pathScript = path_ + '\\' + script
    print(path)
    print(pathScript)
    commend = "D: && cd " + path + " && python manage.py shell < " + pathScript
    print(commend)
    os.system(commend)


def runFromShell(path, script):
    print(path)
    commend = "D: && cd " + path + " && python manage.py shell  " + script
    print(commend)
    os.system(commend)


def run(path, script):
    print(path)
    commend = "cd " + path + " && python manage.py " + script
    print(commend)
    os.system(commend)
