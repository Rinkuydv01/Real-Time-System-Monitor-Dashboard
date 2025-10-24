THRESHOLDS = {
'cpu_percent': 80,
'memory_percent': 85,
'disk_percent': 90
}


def check_alert(metric):
alerts = []
if metric['cpu'] >= THRESHOLDS['cpu_percent']:
alerts.append(f"⚠️ High CPU usage: {metric['cpu']}%")
if metric['memory'] >= THRESHOLDS['memory_percent']:
alerts.append(f"⚠️ High Memory usage: {metric['memory']}%")
if metric['disk'] >= THRESHOLDS['disk_percent']:
alerts.append(f"⚠️ High Disk usage: {metric['disk']}%")
for alert in alerts:
print(alert)
