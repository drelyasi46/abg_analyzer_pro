import os


def check_github():

    print("\n[GITHUB ACTIONS]")

    workflow = ".github/workflows/build.yml"

    if not os.path.exists(workflow):
        print("ERROR workflow missing")
        return

    print("OK workflow found")

    with open(workflow, "r", encoding="utf-8") as f:
        content = f.read()

    checks = {
        "checkout": "actions/checkout" in content,
        "upload": "actions/upload-artifact" in content,
        "buildozer": "buildozer android debug" in content,
        "python": "python" in content,
    }

    for name, result in checks.items():
        if result:
            print("OK", name)
        else:
            print("WARNING missing", name)