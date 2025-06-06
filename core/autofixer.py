import os
# core/autofixer.py
def apply_autofixes(config):
    path = "project/settings.py"
    if not os.path.exists(path): return
    with open(path) as f:
        lines = f.readlines()
    updated, new_lines = False, []
    for line in lines:
        if config["checks"].get("debug") and "DEBUG = True" in line:
            new_lines.append("DEBUG = False\n"); updated = True
        else:
            new_lines.append(line)
    if updated:
        with open(path, "w") as f:
            f.writelines(new_lines)
        print("🔧 Autofix applied to settings.py")
