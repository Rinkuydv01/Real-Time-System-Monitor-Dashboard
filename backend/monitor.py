import psutil
import time
import threading
from backend.database import insert_metric, init_db
from backend.alert_manager import check_alert


SAMPLE_INTERVAL = 3


def get_top_processes(n=5):
procs = []
for p in psutil.process_iter(['pid','name','cpu_percent','memory_percent']):
try:
procs.append(p.info)
except:
continue
return sorted(procs, key=lambda x: (x['cpu_percent'], x['memory_percent']), reverse=True)[:n]


def collect_loop():
while True:
ts = int(time.time())
cpu = psutil.cpu_percent()
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent
net = psutil.net_io_counters()
net_sent = net.bytes_sent
net_recv = net.bytes_recv
processes = get_top_processes(8)
metric = {'cpu': cpu, 'memory': memory, 'disk': disk}
check_alert(metric)
insert_metric(ts, cpu, memory, disk, net_sent, net_recv, processes)
time.sleep(SAMPLE_INTERVAL)


def start_collector():
init_db()
t = threading.Thread(target=collect_loop, daemon=True)
t.start()


if __name__ == "__main__":
start_collector()
while True:
time.sleep(1)
