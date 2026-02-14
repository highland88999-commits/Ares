import os

# Define the path to your whitelist file
WHITELIST_PATH = os.path.join(os.path.dirname(__file__), 'whitelist.txt')

def is_friendly(ip):
    """Returns True if the IP is whitelisted and should never be attacked."""
    try:
        if not os.path.exists(WHITELIST_PATH):
            # If no whitelist exists, only localhost is safe by default
            return ip == "127.0.0.1"
            
        with open(WHITELIST_PATH, 'r') as f:
            friends = [line.strip() for line in f if line.strip()]
            
        return ip in friends or ip == "127.0.0.1"
    except Exception as e:
        print(f"ARES ERROR: Guardrail failure: {e}")
        return False # Safety first: if logic fails, don't assume they are friendly

def add_friend(ip):
    """Adds a new IP to the whitelist."""
    if not is_friendly(ip):
        with open(WHITELIST_PATH, 'a') as f:
            f.write(f"\n{ip}")
        print(f"ARES: {ip} added to the Whitelist.")
