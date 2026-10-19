"""Run every member's assignment answer in one pass.

Usage:
    python run_all.py            # run all assignment-1 answers
    python run_all.py lesson1    # also run the lesson1.py starter

Prints a header per file so each member's output is easy to find,
and reports which answers failed to run (bad import, syntax error,
missing input) instead of stopping at the first failure.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent

CANDIDATES = [
    "assignment.py",
    "assignments/answer1-Michael.py",
    "assignments/answer1_Reggie.py",
    "assignments/answer_Raifu.py",
    "assignments/answer_Stephen.py",
    "assignments/assignment-1-Elnas.py",
]

OPTIONAL = {
    "lesson1": "lesson1.py",
}


def run_file(path):
    print(f"\n=== {path} ===")
    try:
        result = subprocess.run(
            [sys.executable, str(path)],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=ROOT,
        )
        print(result.stdout.rstrip() or "(no output)")
        if result.returncode != 0:
            print(f"!! exited with {result.returncode}: {result.stderr.strip()[:200]}")
    except subprocess.TimeoutExpired:
        print("!! timed out after 30s (probably waiting for input)")


def main():
    files = list(CANDIDATES)
    for flag, path in OPTIONAL.items():
        if flag in sys.argv[1:]:
            files.append(path)

    for name in files:
        path = ROOT / name
        if path.exists():
            run_file(path)
        else:
            print(f"\n=== {name} === (not present, skipped)")

    print("\nDone.")


if __name__ == "__main__":
    main()
