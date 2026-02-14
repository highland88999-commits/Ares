from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
EVIDENCE_DIR = os.path.abspath("evidence/pending")

@app.route('/')
def index():
    # Scans the evidence folder for IP-based subdirectories
    ips = [d for d in os.listdir(EVIDENCE_DIR) if os.path.isdir(os.path.join(EVIDENCE_DIR, d))]
    return render_template('dashboard.html', ips=ips)

@app.route('/view/<ip>')
def view_ip_logs(ip):
    # Lists all files (logs, pcaps) inside that IP's folder
    path = os.path.join(EVIDENCE_DIR, ip)
    files = os.listdir(path)
    return render_template('view_ip.html', ip=ip, files=files)

if __name__ == "__main__":
    app.run(port=8080)
    from common.diplomat import get_country_from_ip, get_authority_email

@app.route('/generate_report/<ip>')
def generate_report(ip):
    country = get_country_from_ip(ip)
    target_email = get_authority_email(country)
    
    # Standard Reporting Template
    subject = f"OFFICIAL CYBERCRIME REPORT: Attack detected from {ip} ({country})"
    body = f"""
    To the Cybercrime Division of {country},
    
    The Ares Autonomous Security System has identified and neutralized a malicious 
    attack originating from the IP address: {ip}.
    
    Evidence has been captured and categorized in our secure local repository.
    The attacker has been placed in a permanent Null-Route (Void) pending your review.
    
    Please advise on the transmission of the full PCAP and log evidence.
    
    System: Ares (Global Defense Network)
    """
    
    # Constructing the mailto link
    import urllib.parse
    safe_subject = urllib.parse.quote(subject)
    safe_body = urllib.parse.quote(body)
    
    return f"mailto:{target_email}?subject={safe_subject}&body={safe_body}"
    
import os
import json
from flask import Flask, render_template

app = Flask(__name__)
EVIDENCE_PATH = "evidence/"

def get_threat_data():
    threat_list = []
    # Loop through each IP folder in evidence/
    for ip_folder in os.listdir(EVIDENCE_PATH):
        folder_path = os.path.join(EVIDENCE_PATH, ip_folder)
        if os.path.isdir(folder_path):
            # Try to load metadata if it exists
            metadata_file = os.path.join(folder_path, 'metadata.json')
            if os.path.exists(metadata_file):
                with open(metadata_file, 'r') as f:
                    data = json.load(f)
            else:
                # Default data if no metadata.json
                data = {"category": "UNCLASSIFIED", "timestamp": "Unknown", "country": "Global"}

            # Get list of files in the folder (logs, captures)
            files = os.listdir(folder_path)
            
            threat_list.append({
                "ip": ip_folder,
                "category": data.get("category"),
                "timestamp": data.get("timestamp"),
                "country": data.get("country"),
                "logs": files
            })
    return threat_list

@app.route('/')
def home():
    offenders = get_threat_data()
    return render_template('index.html', offenders=offenders)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
    import os
import json
from flask import Flask, render_template

app = Flask(__name__)
EVIDENCE_PATH = "evidence/"

def get_threat_data():
    threat_list = []
    # Loop through each IP folder in evidence/
    for ip_folder in os.listdir(EVIDENCE_PATH):
        folder_path = os.path.join(EVIDENCE_PATH, ip_folder)
        if os.path.isdir(folder_path):
            # Try to load metadata if it exists
            metadata_file = os.path.join(folder_path, 'metadata.json')
            if os.path.exists(metadata_file):
                with open(metadata_file, 'r') as f:
                    data = json.load(f)
            else:
                # Default data if no metadata.json
                data = {"category": "UNCLASSIFIED", "timestamp": "Unknown", "country": "Global"}

            # Get list of files in the folder (logs, captures)
            files = os.listdir(folder_path)
            
            threat_list.append({
                "ip": ip_folder,
                "category": data.get("category"),
                "timestamp": data.get("timestamp"),
                "country": data.get("country"),
                "logs": files
            })
    return threat_list

@app.route('/')
def home():
    offenders = get_threat_data()
    return render_template('index.html', offenders=offenders)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
    
