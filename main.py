from monitor_logic import SystemMonitor
import time
import subprocess
import os
import datetime

monitor = SystemMonitor()


print(f"--- Monitoring {monitor.cpu_count} Cores ---")

try:
      while True:
      
            usage, cores, switches, calls = monitor.get_cpu_stat()
            sent, recv = monitor.get_network_usage()
            
            
            mb_sent = monitor.bytes_to_mb(sent)
            switch_num = monitor.format_large_number(switches)
            calls_num = monitor.format_large_number(calls)
            
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            report  = f"{now} CPU: {usage}% | Net: {mb_sent} MB | Switches:{switch_num}M Calls:{calls_num}"
            
            with open("monitor_log.txt", "a") as f:
                  f.write(report + "\n")
            
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
      
            print(report)
    
      
            time.sleep(0.5) 
except KeyboardInterrupt:
      print("\n[!] Monitor: session saved. Closing...")