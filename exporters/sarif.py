
# exporters/sarif.py
import json

def export_sarif(score):
    sarif = {
        "version": "2.1.0",
        "runs": [{
            "tool": {"driver": {"name": "DjangoBestPractice", "version": "0.1.0"}},
            "results": [{
                "ruleId": "DBP001",
                "message": {"text": i["message"]},
                "level": i["severity"],
                "locations": [{"physicalLocation": {
                    "artifactLocation": {"uri": i["file"]},
                    "region": {"startLine": i["line"]}
                }}]
            } for i in score.issues]
        }]
    }
    with open(".django_audit/report.sarif", "w") as f:
        json.dump(sarif, f, indent=2)
