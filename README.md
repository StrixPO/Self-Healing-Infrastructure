# Self-Healing Infrastructure with Prometheus, Alertmanager, Ansible & Docker

This project demonstrates a self-healing infrastructure setup using **Prometheus**, **Alertmanager**, **Ansible**, and **Docker**, with a custom-built **Flask server** acting as the restart controller.

## 🔧 Tech Stack

- **Docker Compose**: Container orchestration
- **NGINX**: Simulated service to monitor
- **Prometheus**: Metrics and alerting
- **Alertmanager**: Alert routing to a Flask server
- **Flask (Python)**: Receives alerts and triggers Ansible
- **Ansible**: Executes the restart playbook

---

## 📁 Project Structure
``
self-healing-infra/ │ 
├── docker-compose.yml # Sets up NGINX, Prometheus, Alertmanager 
├── prometheus/ │ 
      └── prometheus.yml # Prometheus config (targets + rules) 
├── alertmanager/ │ 
        └── config.yml # Alertmanager route config 
├── server.py # Flask app for /health and /restart 
├── server.log # Logs for incoming alert activity 
├── restart_server.yml # Ansible playbook to restart service 
├── inventory.ini # Ansible inventory file 
├── ansible/ # (Optional) Ansible modules or roles 
├── venv/ # Python virtual environment 
└── screenshots/ # Screenshots for documentation/demo


## 🚀 How it Works

1. **Prometheus** scrapes NGINX metrics.
2. If NGINX is down for 30s, Prometheus triggers an alert.
3. **Alertmanager** forwards the alert to Flask server (`/restart` endpoint).
4. **Flask** runs an Ansible playbook to restart the NGINX container.
5. Logs are saved in `server.log`.


## 📦 Running the Project

### 1. Start Infrastructure

``
docker-compose up -d
``
2. Run Flask Server (in venv)
``
source venv/bin/activate
python3 server.py
``

  - Ensure Ansible is installed and Flask is in a virtual environment.

3. Simulate a Failure
Stop the NGINX container:
``
docker stop nginx_service
``

  - Watch the alert fire and trigger auto-recovery.

✅ Future Improvements
  - Add Jenkins for automated deployments
  - Add Grafana dashboards
  - Unit tests for Flask app

