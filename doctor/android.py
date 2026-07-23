import os
import platform
import subprocess


def check_android():

    print("\n[ANDROID / BUILDOZER]")

    # OS check
    system = platform.system()

    if system == "Windows":
        print("WARNING Running on Windows")
        print("Buildozer should run in WSL/Linux/GitHub Actions")
    else:
        print("OK Linux environment")

    # Buildozer check
    try:
        result = subprocess.run(
            ["buildozer", "--version"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("OK Buildozer:")
            print(result.stdout.strip())
        else:
            print("WARNING Buildozer problem")

    except FileNotFoundError:
        print("WARNING Buildozer not installed")

    # Python-for-android
    if os.path.exists("python-for-android-master"):
        print(
            "WARNING python-for-android-master found "
            "(possible conflict)"
        )
    else:
        print("OK No external python-for-android")

    # buildozer.spec
    if os.path.exists("buildozer.spec"):
        print("OK buildozer.spec found")
    else:
        print("ERROR buildozer.spec missing")
