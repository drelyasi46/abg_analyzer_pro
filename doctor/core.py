from doctor.project import check_project
from doctor.android import check_android
from doctor.github import check_github


def run_all():

    print("=" * 50)
    print("ABG Analyzer Pro Preflight")
    print("=" * 50)

    check_project()

    check_android()

    check_github()

    print("\nDONE")