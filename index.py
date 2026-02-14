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
