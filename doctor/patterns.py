FAILURE_PATTERNS = [

    {
        "name": "Python 3.14 detected",
        "pattern": r"python3\.14|Python 3\.14",
        "advice": "Use Python 3.11 in GitHub Actions"
    },

    {
        "name": "Cython config.pxi problem",
        "pattern": r"config\.pxi|Dependency for .*\.pyx not resolved",
        "advice": "Check Kivy/Cython compatibility"
    },

    {
        "name": "Buildozer root execution",
        "pattern": r"running as root|BUILDOZER_WARN_ON_ROOT",
        "advice": "Run Buildozer with normal user"
    },

    {
        "name": "Android NDK/SDK problem",
        "pattern": r"NDK|sdkmanager|Android SDK",
        "advice": "Check Android SDK and NDK setup"
    },

    {
        "name": "Network download failure",
        "pattern": r"TLS handshake|timeout|Unable to establish SSL",
        "advice": "Check network or download source"
    },

    {
        "name": "APK not generated",
        "pattern": r"No files were found.*apk|bin/.*apk",
        "advice": "Build failed before APK generation"
    },

]