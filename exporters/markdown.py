
# exporters/markdown.py
def export_markdown(score):
    with open(".django_audit/report.md", "w") as f:
        f.write("# Django Audit Report\n\n")
        f.write(f"**Score:** {score.score}/100\n\n")
        f.write("| Impact | Message | Severity |\n|--------|---------|----------|\n")
        for i, m, sev in score.messages:
            f.write(f"| {i} | {m} | {sev.upper()} |\n")
