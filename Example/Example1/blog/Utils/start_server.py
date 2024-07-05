import os

import sys
from Example.Utils.run_from_shell import run

if __name__ == "__main__":
    if len(sys.argv) < 2:
        port = "0.0.0.0:8083"
    else:
        port = sys.argv[1]
    run(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
        "runserver " + str(port),
    )
