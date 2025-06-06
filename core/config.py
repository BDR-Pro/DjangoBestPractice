
# core/config.py
import os, yaml

def ensure_dirs():
    os.makedirs(".django_audit", exist_ok=True)

DEFAULT_CONFIG = {
    "checks": {
        "debug": True,
        "allowed_hosts": True,
        "ssl_redirect": True,
        "cookie_secure": True,
        "hardcoded_secrets": True,
        "cors": True,
        "use_tz": True,
        "referrer_policy": True,
        "auto_now_add": True,
        "static_root_path": True,
        "media_cdn": True,
        "sqlite": True,
        "large_static": True,
        "template_safe": True,
        "csrf_token_form": True,
        "missing_login_required": True,
        "missing_csrf_protect": True,
        "secure_headers": True
    }
}

def load_config():
    path = ".dbp.yaml"
    if not os.path.exists(path):
        with open(path, "w") as f:
            yaml.dump(DEFAULT_CONFIG, f)
    with open(path) as f:
        return yaml.safe_load(f)
