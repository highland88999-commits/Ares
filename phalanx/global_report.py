import requests

API_KEY = "YOUR_ABUSEIPDB_API_KEY"
URL = 'https://api.abuseipdb.com/api/v2/report'

def report_to_the_world(ip, categories, comment):
    """Reports a malicious IP to the global database."""
    params = {
        'ip': ip,
        'categories': categories, # 14 = Scraper, 15 = Brute-Force
        'comment': f"ARES DEFENSE: {comment}"
    }
    headers = {
        'Accept': 'application/json',
        'Key': API_KEY
    }
    
    response = requests.post(URL, data=params, headers=headers)
    if response.status_code == 200:
        print(f"ARES: {ip} has been reported to the global community.")
    else:
        print("ARES: Failed to report to global database.")

# Usage: Ares calls this when a Honey-token is triggered
# report_to_the_world("1.2.3.4", "14", "Scraper hit honey-token /admin_backup.php")
