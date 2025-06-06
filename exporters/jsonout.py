# exporters/jsonout.py
import json

def export_json(score):
    with open(".django_audit/problems.json", "w") as f:
        json.dump(score.issues, f, indent=2)