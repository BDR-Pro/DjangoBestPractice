
# core/bandit.py

import subprocess, json
from core.score import ScoreResult

def check_if_bandit_installed():
    """Check if Bandit is installed."""
    try:
        subprocess.run(["bandit", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print("Bandit is not installed. Please install it using 'pip install bandit'.")
        exit(1)


def run_bandit():
    subprocess.run(["bandit", "-r", ".", "-f", "json", "-o", ".django_audit/bandit.json"])

def parse_bandit_results():
    try:
        with open(".django_audit/bandit.json", "r") as f:
            data = json.load(f)
        return data.get("results", [])
    except FileNotFoundError:
        print("Bandit results file not found. Please run Bandit first.")
        return []

def apply_bandit_to_score(score):
    results = parse_bandit_results()
    for finding in results:
        issue_text = finding.get("issue_text", "Bandit finding")
        severity = finding.get("issue_severity", "LOW").upper()
        filename = finding.get("filename", "?")
        line = finding.get("line_number", 0)
        points = 5 if severity == "HIGH" else 2 if severity == "MEDIUM" else 1
        level = "error" if severity == "HIGH" else "warning" if severity == "MEDIUM" else "info"
        score.deduct(points, f"Bandit: {issue_text}", filename, line, level)
