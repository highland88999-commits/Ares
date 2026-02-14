import requests
from common.intelligence import ask_ares_brain

def hunt_threats(target_list):
    """Scans a list of potentially malicious IPs or Domains."""
    for target in target_list:
        # 1. Probe the target (e.g., check for known exploit paths)
        try:
            r = requests.get(f"http://{target}/wp-admin", timeout=5)
            # 2. Use the AI Brain to analyze the response
            if ask_ares_brain(r.text):
                print(f"ARES SCOUT: Confirmed threat at {target}. Reporting to Hub.")
                # Logic to report to Ares Hub goes here
        except:
            continue
