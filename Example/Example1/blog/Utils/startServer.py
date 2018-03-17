import os

import sys
from Example.Utils.runFromShell import run

if __name__ == '__main__':
    if len(sys.argv) < 1:
        port = 8081
    else:
        port = sys.argv[1]
    run(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')),"runserver "+str(port))