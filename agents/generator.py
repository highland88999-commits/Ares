import os

def create_agent(site_name, log_path, sensitivity_level):
    """Generates a customized AI agent for a specific terrain."""
    agent_code = f"""
import time
from common.guardrail import is_friendly
from phalanx.void import BlackHoleIP

SITE_NAME = "{site_name}"
LOG_FILE = "{log_path}"
SENSITIVITY = {sensitivity_level}

def analyze_behavior(log_entry):
    # This is where the AI logic sits. 
    # It looks for patterns like directory traversal or rapid-fire 404s.
    if "admin" in log_entry and "404" in log_entry:
        return "SUSPICIOUS"
    return "SAFE"

def run_agent():
    print(f"Ares Agent for {{SITE_NAME}} is now standing guard.")
    with open(LOG_FILE, 'r') as f:
        f.seek(0, 2) # Move to the end of the file
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            
            # Brain logic
            verdict = analyze_behavior(line)
            if verdict == "SUSPICIOUS":
                # Extract IP (Simplified)
                ip = line.split()[0] 
                if not is_friendly(ip):
                    BlackHoleIP(ip)
    """
    
    file_path = f"agents/minion_{site_name}.py"
    with open(file_path, "w") as f:
        f.write(agent_code)
    print(f"ARES: Agent for {site_name} generated at {file_path}")

# Example: Generate an agent for your main site
# create_agent("Olympus_Main", "/var/log/nginx/access.log", 0.8)
def bake_ai_agent(target_site, log_path):
    """Bakes a fully autonomous AI Security Agent."""
    agent_template = f"""
import time
from common.intelligence import ask_ares_brain
from phalanx.void import BlackHoleIP
from common.guardrail import is_friendly

def stand_guard():
    print("ARES AGENT: Standing guard over {target_site}...")
    with open('{log_path}', 'r') as log:
        log.seek(0, 2)
        while True:
            line = log.readline()
            if not line:
                time.sleep(0.5)
                continue
            
            # 1. Quick Guardrail Check
            ip = line.split()[0] # Standard Nginx/Apache format
            if is_friendly(ip): continue

            # 2. AI Reasoning
            if ask_ares_brain(line):
                print(f"ARES: AI Verdict - VOID for {{ip}}")
                BlackHoleIP(ip)
                # 3. Report to Hub (Future step)

if __name__ == '__main__':
    stand_guard()
"""
    with open(f"agents/minion_{target_site}.py", "w") as f:
        f.write(agent_template)
    print(f"ARES: AI Agent for {target_site} is ready for deployment.")
    
