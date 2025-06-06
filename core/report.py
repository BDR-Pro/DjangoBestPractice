
# core/report.py
from rich.console import Console
from rich.table import Table
def display_results(score):
    from rich.console import Console
    from rich.table import Table

    console = Console()
    console.print(f"\n[bold cyan]Django Best Practice Score: [yellow]{max(0, score.score)}/100[/]")

    table = Table(title="Audit Breakdown")
    table.add_column("Impact")
    table.add_column("Detail")
    table.add_column("Severity")
    table.add_column("File/Line")

    for i, m, s in score.messages:
        style = "green" if '+' in i else ("red" if s == "error" else "yellow")
        matching_issue = next((issue for issue in score.issues if issue["message"] == m), None)
        fileline = f"{matching_issue['file']}:{matching_issue['line']}" if matching_issue else "-"
        table.add_row(f"[{style}]{i}[/{style}]", m, s.upper(), fileline)

    console.print(table)
