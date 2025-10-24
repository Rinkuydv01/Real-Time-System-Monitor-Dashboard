# Real-Time System Monitor Dashboard

## Overview
A real-time system monitoring dashboard built using **Python**, **Flask**, **Streamlit**, and **psutil**.  
Tracks CPU, memory, disk, network, and process-level metrics, with console alerts for threshold breaches. Data is stored in an **SQLite** database for logging and analytics.

---

## Features
- Real-time CPU, Memory, Disk monitoring  
- Network usage tracking (Bytes sent/received)  
- Top processes by CPU and Memory usage  
- Configurable console alerts for high resource usage  
- SQLite logging for historical analysis  
- Streamlit dashboard for interactive visual monitoring  

---

## Tech Stack
- **Python 3.10+**  
- **Flask**: Backend API for metrics collection  
- **Streamlit**: Interactive dashboard  
- **psutil**: System metrics collection  
- **SQLite**: Persistent data storage  
- **Pandas**: Analytics and data handling  

---

## Folder Structure
real-time-system-monitor-dashboard/
│
├── backend/
│ ├── init.py
│ ├── database.py
│ ├── monitor.py
│ ├── alert_manager.py
│ └── server.py
│
├── dashboard/
│ └── app.py
│
├── data/ # SQLite DB auto-created
└── README.md

---

## Setup & Installation

1. **Clone the repository**
```bash
git clone https://github.com/Rinkuydv01/Real-Time-System-Monitor-Dashboard.git
cd Real-Time-System-Monitor-Dashboard


Create a virtual environment

python -m venv venv
# Activate:
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Run Backend (metrics collector + API)

python backend/server.py

Run Dashboard

streamlit run dashboard/app.py
