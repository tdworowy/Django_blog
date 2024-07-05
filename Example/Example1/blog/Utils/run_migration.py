import os

from Example.Utils.run_from_shell import run

if __name__ == "__main__":
    try:
        run(
            os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
            "makemigrations",
        )
    finally:
        run(
            os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
            "migrate",
        )
