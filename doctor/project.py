import os


def check_project():

    print("\n[PROJECT STRUCTURE]")

    warnings = []

    folders = [
        ".buildozer",
        "bin",
        "python-for-android-master",
        ".venv",
        "venv",
        "venv_buildozer",
        "venv_win"
    ]

    for f in folders:
        if os.path.exists(f):
            warnings.append(f)

    if warnings:
        print("Found:")
        for w in warnings:
            print("  WARNING:", w)
    else:
        print("Clean")

    print("\nChecking required files...")

    required = [
        "main.py",
        "main.kv",
        "buildozer.spec",
        "requirements.txt"
    ]

    for r in required:
        print(
            "OK  " if os.path.exists(r) else "MISS ",
            r
        )