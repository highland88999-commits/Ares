from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# The 'Book of War': { ip: { "count": 0, "reports": [timestamp, ...] } }
threat_database = {}

CONSENSUS_THRESHOLD = 5  # Number of unique nodes required
TIME_WINDOW = 60         # Minutes to track reports

@app.route('/v1/report_threat', methods=['POST'])
def receive_report():
    data = request.json
    attacker_ip = data.get('ip')
    node_id = data.get('node_id') # Each website has a unique ID

    # Initialize entry if new
    if attacker_ip not in threat_database:
        threat_database[attacker_ip] = {"nodes": set(), "last_seen": None}

    # Add this node to the consensus list
    threat_database[attacker_ip]["nodes"].add(node_id)
    threat_database[attacker_ip]["last_seen"] = datetime.now()

    # Check if we hit the Global Threshold
    if len(threat_database[attacker_ip]["nodes"]) >= CONSENSUS_THRESHOLD:
        return jsonify({"status": "GLOBAL_THREAT", "action": "BLACK_HOLE"}), 201
    
    return jsonify({"status": "LOGGED", "current_consensus": len(threat_database[attacker_ip]["nodes"])}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888) # Secure this with an API key later
    @app.route('/v1/bulk_report', methods=['POST'])
def bulk_report():
    data = request.json
    found_threats = data.get('threats', [])
    for threat in found_threats:
        # Add to the 'Book of War' and check for global consensus
        process_threat(threat)
    return jsonify({"status": "INTEL_RECEIVED"}), 200
    
