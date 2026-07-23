import re
from doctor.patterns import FAILURE_PATTERNS


def analyze_log(text):

    print("\n[BUILD FAILURE ANALYSIS]")

    found = False

    for item in FAILURE_PATTERNS:

        if re.search(item["pattern"], text, re.IGNORECASE):

            found = True

            print("ERROR:", item["name"])
            print("Advice:", item["advice"])
            print()

    if not found:
        print("No known failure pattern detected")