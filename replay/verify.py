"""Run both exact covering implementations and twelve coefficient/coverage mutants."""
from pathlib import Path
import subprocess
import sys
import time

root = Path(__file__).resolve().parent
cases = {
    "replay.py": ["pin", "strict-budget", "coverage-gap", "reserve-too-high", "hankel-tail", "centered-cone"],
    "independent.py": ["pin", "strict-budget", "coverage-gap", "reserve-too-high", "completion-sign", "tangent-intercept"],
}
for script, mutants in cases.items():
    for mutant in [None] + mutants:
        command = [sys.executable, "-B", str(root / script)]
        if mutant is not None:
            command.extend(["--mutant", mutant])
        started = time.monotonic()
        result = subprocess.run(command, cwd=root, capture_output=True, text=True, timeout=180)
        expected = 0 if mutant is None else 1
        print("COMMAND:", " ".join(command), flush=True)
        print("EXIT:", result.returncode, "EXPECTED:", expected, "SECONDS:", round(time.monotonic() - started, 3), flush=True)
        print(result.stdout, end="", flush=True)
        print(result.stderr, end="", flush=True)
        if result.returncode != expected or (mutant is not None and "REJECT:" not in result.stdout + result.stderr):
            raise SystemExit("FAIL: replay or guarded mutant outcome")
print("PASS: two independent exact coverings and all twelve mutants rejected (each mutant exit 1).", flush=True)
