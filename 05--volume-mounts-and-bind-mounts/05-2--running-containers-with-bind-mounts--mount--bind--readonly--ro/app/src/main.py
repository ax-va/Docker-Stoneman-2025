from pathlib import Path

file = Path("/data/text.txt")

with file.open("r+") as f:
    run_number = 1
    for line in f:
        if "Run" in line:
            run_number += 1

    f.write(f"\nRun {run_number}")

print(file.read_text())
