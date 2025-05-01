from flask import Flask, request, jsonify
import subprocess
import logging

app = Flask(__name__)

# Set up logging to file
logging.basicConfig(filename='server.log', level=logging.INFO)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})

@app.route('/restart', methods=['POST'])  # <== this is the one we care about
def restart():
    logging.info("Restart triggered by Alertmanager")
    try:
        result = subprocess.run(
            ['ansible-playbook', 'restart_server.yml', '-i', 'inventory.ini'],
            capture_output=True, text=True
        )
        logging.info(result.stdout)
        if result.returncode == 0:
            return jsonify({"message": "Restart executed"}), 200
        else:
            return jsonify({"error": "Restart failed", "details": result.stderr}), 500
    except Exception as e:
        logging.error(str(e))
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
