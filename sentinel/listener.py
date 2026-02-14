from flask import Flask, request, jsonify
import sys
import os

# Add the root directory to path so we can import 'common'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.guardrail import is_friendly

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def handle_alert():
    data = request.json
    attacker_ip = data.get('ip')
    site_id = data.get('site_id')
    
    # THE PRIMARY CHECK
    if is_friendly(attacker_ip):
        print(f"ARES: Whitelisted IP {attacker_ip} touched a token on {site_id}. Ignoring.")
        return jsonify({"status": "ignored"}), 200

    print(f"ARES: MALICIOUS ACTIVITY DETECTED from {attacker_ip} on {site_id}!")
    
    # This is where we will call the Phalanx (Go) to block them next
    # For now, we just log it.
    return jsonify({"status": "under_review"}), 200

if __name__ == '__main__':
    app.run(port=5000)
