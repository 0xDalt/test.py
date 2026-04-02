import psutil

class SystemMonitor:
    def __init__(self):
        self.cpu_count = psutil.cpu_count()
        
    def get_cpu_stat(self):
        usage_pct = psutil.cpu_percent(interval=1)
        core_usage = psutil.cpu_percent(percpu=True)
        stats = psutil.cpu_stats()
        return usage_pct, core_usage, stats.ctx_switches, stats.syscalls

    def get_network_usage(self):
        net = psutil.net_io_counters()
        return net.bytes_sent, net.bytes_recv

    def bytes_to_mb(self, bytes_value):
        return round(bytes_value / (1024 * 1024), 2)
    
    def format_large_number (self, num):
        return round(num / (1000000), 2)