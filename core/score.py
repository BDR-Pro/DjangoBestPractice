
# core/score.py
class ScoreResult:
    def __init__(self):
        self.score = 100
        self.messages = []
        self.issues = []

    def deduct(self, points, message, file=None, line=None, severity="warning"):
        self.score -= points
        self.messages.append((f"-{points}", message, severity))
        if file and line:
            self.issues.append({"file": file, "line": line, "message": message, "severity": severity})

    def award(self, points, message):
        self.score += points
        self.messages.append((f"+{points}", message, "info"))
