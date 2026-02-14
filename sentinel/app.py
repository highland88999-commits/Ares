from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/report', methods=['POST'])
def report_threat():
    data = request.json
    ip = data.get('ip')
    threat_type = data.get('type') # e.g., 'honey_token', 'brute_force'
    
    # Check Whitelist first
    if ip in WHITELIST:
        return {"status": "ignored", "reason": "friend"}, 200

    # Log the offender in the Book of War
    mark_offender(ip, threat_type)
    
    # Trigger the Phalanx to shun them
    shun_result = phalanx.shun_ip(ip)
    
    return {"status": "engaged", "target": ip}, 200
