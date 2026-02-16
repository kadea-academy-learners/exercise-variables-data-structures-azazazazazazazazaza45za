import ast
import re
import subprocess
import sys

def run_program(name: str, city: str, birth_year: int, current_year: int, foods_raw: str) -> str:
    user_input = f"{name}\n{city}\n{birth_year}\n{current_year}\n{foods_raw}\n"
    proc = subprocess.run(
        [sys.executable, "data_structures.py"],
        input=user_input,
        text=True,
        capture_output=True
    )
    assert proc.returncode == 0, (
        "Le programme a crash.\n"
        f"STDERR:\n{proc.stderr}\n"
        f"STDOUT:\n{proc.stdout}"
    )
    return proc.stdout

def assert_prompts(output: str) -> None:
    for p in [
        "Enter full name:",
        "Enter city:",
        "Enter birth year:",
        "Enter current year:",
        "Enter favorite foods (comma-separated):",
    ]:
        assert p in output, f"Prompt manquant: {p}\nOUTPUT:\n{output}"

def _line_value(output: str, label: str) -> str:
    m = re.search(rf"^{re.escape(label)}\s*(.*)$", output, flags=re.MULTILINE)
    assert m, f"Ligne manquante: {label}\nOUTPUT:\n{output}"
    return m.group(1).strip()

def extract_age(output: str) -> int:
    return int(_line_value(output, "Age:"))

def extract_foods_list(output: str):
    s = _line_value(output, "Foods (list):")
    return ast.literal_eval(s)

def extract_foods_count(output: str) -> int:
    return int(_line_value(output, "Foods count:"))

def extract_unique_foods(output: str) -> int:
    return int(_line_value(output, "Unique foods:"))

def extract_profile_dict(output: str):
    s = _line_value(output, "Profile (dict):")
    return ast.literal_eval(s)

def extract_summary_tuple(output: str):
    s = _line_value(output, "Summary (tuple):")
    return ast.literal_eval(s)
