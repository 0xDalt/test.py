import psutil
import time

# ---Logic---

def get_network_usage():
    net = psutil.net_io_counters()
    return net.bytes_sent, net.bytes_recv

def bytes_to_mb(bytes_value):
    return round(bytes_value / (1024 * 1024), 2)

def cpu_stat ():
    usage_pct = psutil.cpu_percent(interval=1)
    core_usage = psutil.cpu_percent(percpu=True)
    stats = psutil.cpu_stats()
    return usage_pct, core_usage, stats.ctx_switches, stats.syscalls 

def format_large_number (num):
    return round(num / (1000000), )


# ---Main execution---


#Get CPU Data
usage, cores, switches, calls = cpu_stat()
count = psutil.cpu_count()


# Get Network Data
sent, recv = get_network_usage()
mb_sent = bytes_to_mb(sent)
switch_num = format_large_number(switches)
calls_num = format_large_number(calls)



# 3. Print the Report
print("---System Monitor ---")
print(f"CPU Usage: {usage}% across {count} cores")
print(f"Per-Core Breakdown: {cores}")
print(f"Network Sent: {mb_sent} MB")
print(f"Context Switches: {switch_num} | Syscalls: {calls_num}")

if count > 5:
    print("Status: High-core count system detected.")