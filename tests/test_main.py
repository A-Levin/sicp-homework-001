import subprocess
import sys

def test_main_output():
    result = subprocess.run(
        [sys.executable, 'main.py'],
        capture_output=True,
        text=True
    )
    lines = result.stdout.strip().split('\n')

    assert len(lines) == 5, f"Expected 5 lines, got {len(lines)}"
    assert lines[0].strip() == '12', f"Example 1: expected 12, got {lines[0]}"
    assert lines[1].strip() == '-3', f"Example 2: expected -3, got {lines[1]}"
    assert lines[2].strip() == '1024', f"Example 3: expected 1024, got {lines[2]}"
    assert lines[3].strip() == '9', f"Example 4: expected 9, got {lines[3]}"
    assert lines[4].strip() == '15', f"Example 5: expected 15, got {lines[4]}"
