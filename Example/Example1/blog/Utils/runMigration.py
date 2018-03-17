import os

from Example.Utils.runFromShell import run

if __name__ == '__main__':
    run(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')),"makemigrations")
    run(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')),"migrate")