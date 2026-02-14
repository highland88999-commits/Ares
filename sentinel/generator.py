import uuid
import os

def generate_canary_file(filename, site_id):
    """Creates a fake file with a unique tracking ID."""
    token = uuid.uuid4().hex
    # This URL is your Ares Sentinel endpoint
    tracking_url = f"https://ares-sentinel.yourdomain.com/alert/{site_id}/{token}"
    
    content = f"""
    # SYSTEM BACKUP CONFIG - DO NOT MANUALLY EDIT
    # Last generated: 2026-02-13
    API_KEY = "ARES-TRAP-{token}"
    REPORT_URL = "{tracking_url}"
    """
    
    with open(filename, "w") as f:
        f.write(content)
    print(f"ARES: Honey-token generated at {filename}")

# Generate a fake .env file for your website
generate_canary_file(".env_production", "Site_Olympus_Main")
