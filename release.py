import shutil
import subprocess
from pathlib import Path
import calculator
import glob
import typer

version = calculator.__version__


def cleanup():
    paths = ["dist", "site", ".pytest_cache"]
    paths += glob.glob("*.egg-info")
    paths += glob.glob("*.pytest_cache")
    for path in paths:
        path = Path(__file__).parent / path
        if path.exists():
            shutil.rmtree(path)


def check(question: str):
    response = input(question + "\n")
    if response.lower() not in ["y", "yes"]:
        raise Exception(f"Action required")


def shell(cmd: str):
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        raise Exception(
            f"{result.args} exited with returncode={result.returncode}"
        )


def announce(s: str):
    msg = "\n".join(
        [
            "=" * 80,
            s.center(80),
            "=" * 80,
        ]
    )
    typer.secho(
        message=msg,
        fg=typer.colors.RED,
        bold=True,
    )
    # print(BOLD + HEADER)
    # print("=" * 80)
    # print(s.center(80))
    # print("=" * 80)
    # print(ENDC)


HEADER = "\033[95m"
OKBLUE = "\033[94m"
OKCYAN = "\033[96m"
OKGREEN = "\033[92m"
WARNING = "\033[93m"
FAIL = "\033[91m"
ENDC = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

if __name__ == "__main__":
    print(f"Releasing version {version}")
    cleanup()

    announce("Running tests")
    shell("pytest")

    announce("Checking formatting with Black")
    shell("black . --check")

    announce("Checking conventional commits format")
    FIRST_CONVENTIONAL_COMMIT = "84059a5a6a0f88878c3687222fd63574bf856226"
    shell(f"cz check --rev-range {FIRST_CONVENTIONAL_COMMIT}..HEAD")

    announce("Bump version and auto-update changelog")
    shell("cz bump")

    print("Building docs")
    shell(f"mike deploy {version}")
    shell(f"mike alias {version} latest --update-aliases")
    try:
        process = shell("mike serve")
    except KeyboardInterrupt:
        pass
    check("Do the docs look OK?")
    shell("mike list")
    check("Does the list of docs versions look OK?")

    # print("Deploying docs")
    # shell(f"mike set-default latest --push")

    # announce("Building package")
    # shell("python -m build")
    # shell("twine check dist/*")

    # print("PyPI test run")
    # shell("twine upload -r pypitest dist/*")
    # check(f"Does the testpypi output look OK?")
    #
    # print("PyPI deploy")
    # shell("twine upload dist/*")
    #
    cleanup()

    print("Done!")
