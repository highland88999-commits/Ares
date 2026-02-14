import requests

def get_country_from_ip(ip):
    """Detects the country of the attacker."""
    try:
        # Using a free GeoIP API (for development)
        response = requests.get(f"https://ipapi.co/{ip}/country_name/")
        return response.text.strip()
    except:
        return "Unknown"

def get_authority_email(country):
    """Parses authority_contacts.txt for the right email."""
    try:
        with open('authority_contacts.txt', 'r') as f:
            for line in f:
                if country in line and "@" in line:
                    # Extracts the email from the line
                    return line.split()[-1].strip("()")
    except FileNotFoundError:
        print("ARES ERROR: authority_contacts.txt missing.")
    return "ncrp-ic3@global_defense.ares" # Fallback
