# File: cli.py
import argparse, sys, os
from core.engine import run_audit
from exporters.markdown import export_markdown
from exporters.sarif import export_sarif
from exporters.jsonout import export_json
from core.report import display_results
from core.autofixer import apply_autofixes
from core.bandit import run_bandit,apply_bandit_to_score
from core.config import load_config, ensure_dirs
def get_settings():
    "find where the settings.py file is located."
    for root, dirs, files in os.walk(os.getcwd()):
        if "settings.py" in files:
            return os.path.relpath(root, os.getcwd())
    raise FileNotFoundError("settings.py not found in the current directory or its subdirectories.")
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--markdown", action="store_true")
    parser.add_argument("--sarif", action="store_true",default=True,
                        help="Export results in SARIF format.")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--bandit", action="store_true",default=True,
                        help="Run Bandit security checks on the project.")
    parser.add_argument("--autofix", action="store_true")
    args = parser.parse_args()
    print("Starting Django Security Audit...")
    print("Checking current directory:", os.getcwd())
    print("Python version:", sys.version)
    print("Arguments:", args)
    if not "manage.py" in os.listdir(os.getcwd()):
        print("This script should be run from the project root directory.")
        sys.exit(1)
    settengs_path = os.path.join(os.getcwd(), get_settings(), "settings.py")
    print("Settings file found at:", settengs_path)
    ensure_dirs()
    config = load_config()

    if args.bandit:
        run_bandit()
    if args.autofix:
        apply_autofixes(config)

    result = run_audit(config,settings_path=settengs_path)
    if args.bandit:
        apply_bandit_to_score(result)
    display_results(result)

    if args.markdown:
        export_markdown(result)
    if args.json:
        export_json(result)
    if args.sarif:
        export_sarif(result)

