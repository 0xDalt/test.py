from monitor_logic import SystemMonitor
import time

monitor = SystemMonitor()

print(f"--- Monitoring {monitor.cpu_count} Cores ---")

while True:
    usage, cores, switches, calls = monitor.get_cpu_stat()
    sent, recv = monitor.get_network_usage()
    
    mb_sent = monitor.bytes_to_mb(sent)
    switch_num = monitor.format_large_number(switches)
    calls_num = monitor.format_large_number(calls)
    
    print(f"CPU: {usage}% | Net: {mb_sent} MB |"
          f" Switches:{switch_num}M Calls:{calls_num}")
    
    
    time.sleep(0.5) 