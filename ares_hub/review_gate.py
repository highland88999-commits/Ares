@app.route('/v1/review_queue', methods=['GET'])
def get_review_queue():
    # Returns a list of all IPs currently in the 'Void'
    void_list = get_all_blackholed_ips() 
    return jsonify({"pending_review": void_list})

@app.route('/v1/verdict', methods=['POST'])
def issue_verdict():
    data = request.json
    ip = data.get('ip')
    action = data.get('action') # 'REPORT_TO_AUTHORITIES' or 'RELEASE'
    
    if action == 'REPORT_TO_AUTHORITIES':
        # 1. Package the evidence
        # 2. Flag for external reporting script
        move_to_reviewed(ip)
        return jsonify({"status": "OFFICIAL_REPORT_GENERATED"}), 200
