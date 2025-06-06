
# core/engine.py
import os, re
from core.score import ScoreResult

def run_audit(config, settings_path=None):
    """Run the security audit on the Django project."""
    score = ScoreResult()
    path = settings_path 
    try:
        with open(path) as f:
            lines = f.readlines()
    except:
        score.deduct(10, "Missing settings.py", path, 1, "error")
        return score

    for i, line in enumerate(lines):
        if config["checks"].get("debug") and "DEBUG = True" in line:
            score.deduct(10, "DEBUG=True", path, i+1, "error")
        if config["checks"].get("cookie_secure") and "SESSION_COOKIE_SECURE = False" in line:
            score.deduct(4, "SESSION_COOKIE_SECURE=False", path, i+1, "warning")
    return score
