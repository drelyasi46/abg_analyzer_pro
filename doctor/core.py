from .project import check_project
import sys


def run_all():

    print("=" * 50)
    print("ABG Analyzer Pro Preflight")
    print("=" * 50)

    print("\n[PYTHON]")
    print(sys.version)

    check_project()

    print("\nDONE")