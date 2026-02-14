import yaml
import subprocess

def load_config():
    with open("ares_config.yaml", "r") as f:
        return yaml.safe_load(f)

def engage_phalanx(ip):
    config = load_config()
    if ip in config['whitelist']:
        print(f"ARES: Target {ip} is a FRIEND. Aborting engagement.")
        return

    print(f"ARES: Red Card issued for {ip}. Deploying Phalanx.")
    # Calls the Go binary or a Shell script to execute the block
    subprocess.run(["./phalanx_bin", ip])

# Example: If a Honey-token is touched
# engage_phalanx("192.168.1.50")
