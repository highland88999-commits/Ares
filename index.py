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
    
