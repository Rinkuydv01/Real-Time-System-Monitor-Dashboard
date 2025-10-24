import sqlite3
import json
import os


DB_PATH = "data/logs.db"
os.makedirs("data", exist_ok=True)


def init_db():
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS metrics (
id INTEGER PRIMARY KEY AUTOINCREMENT,
ts INTEGER NOT NULL,
cpu REAL,
memory REAL,
disk REAL,
net_sent REAL,
net_recv REAL,
processes TEXT
)
''')
conn.commit()
conn.close()


def insert_metric(ts, cpu, memory, disk, net_sent, net_recv, processes):
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute('''
INSERT INTO metrics (ts, cpu, memory, disk, net_sent, net_recv, processes)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', (ts, cpu, memory, disk, net_sent, net_recv, json.dumps(processes)))
conn.commit()
conn.close()


def fetch_latest(limit=1):
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute('SELECT * FROM metrics ORDER BY ts DESC LIMIT ?', (limit,))
rows = cur.fetchall()
conn.close()
return rows
