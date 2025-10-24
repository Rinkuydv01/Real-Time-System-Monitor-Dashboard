from flask import Flask, jsonify
from backend.database import fetch_latest
from backend.monitor import start_collector


app = Flask(__name__)
start_collector()


@app.route("/api/latest", methods=["GET"])
def latest():
rows = fetch_latest()
if not rows:
return jsonify({"msg": "No data yet"}), 404
row = rows[0]
return jsonify({
"ts": row[1],
"cpu": row[2],
"memory": row[3],
"disk": row[4],
"net_sent": row[5],
"net_recv": row[6],
"processes": row[7]
})


if __name__ == "__main__":
app.run(host="0.0.0.0", port=5000)
