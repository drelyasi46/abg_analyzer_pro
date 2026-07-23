import sys
from doctor.core import run_all
from doctor.failure import analyze_log


def main():

    if len(sys.argv) >= 3 and sys.argv[1] == "--analyze":

        log_file = sys.argv[2]

        try:
            with open(log_file, "r", encoding="utf-8") as f:
                content = f.read()

            analyze_log(content)

        except FileNotFoundError:
            print("ERROR: Log file not found:", log_file)

        return

    run_all()


if __name__ == "__main__":
    main()