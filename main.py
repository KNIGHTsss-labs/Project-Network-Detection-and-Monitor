"""
Docstring for main

System Function
1. CUP
2. Memory
3. Disk
4. Network
5. Sensor

Other System info
1. Boot time
2. Users
"""

import time, psutil

def show_cores():
    print("Number of cors in system :", psutil.cpu_count(logical=True))
    print("Number of physical cores in system :", psutil.cpu_count(logical=False))
    print("Number of Threads in this notebook : ", psutil.cpu_count(logical=True)/psutil.cpu_count(logical=False))

def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))

    mem_percent = (mem_usage / 100.0)
    mem_bar = '' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    print(f"CPU Usage : |{cpu_bar}| {cpu_usage:.2f}%   ", end="")
    print(f"MEM Usage : |{mem_bar}| {mem_usage:.2f}%   ", end="\r")

def monitor_memory_usage():
    """
    Monitors and prints the memory usage of all running processes.
    Memory usage is displayed in Megabytes (MB).
    """
    print(f"| {'PID':<6} | {'Process Name':<30} | {'Memory Usage (MB)':<20} |")
    print("-" * 65)

    # Iterate over all running processes
    # The 'pid' and 'name' attributes are fetched automatically for efficiency
    for process in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            # Get process name and memory usage
            process_name = process.info['name']
            # rss (Resident Set Size) is the non-swapped physical memory used
            memory_usage_bytes = process.info['memory_info'].rss
            # Convert bytes to Megabytes (MB)
            memory_usage_mb = memory_usage_bytes / (1024 * 1024)

            print(f"| {process.info['pid']:<6} | {process_name:<30} | {memory_usage_mb:<20.2f} |")

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Skip processes that cannot be accessed or have terminated
            pass


if __name__ == "__main__":
    monitor_memory_usage()

while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent)
    time.sleep(0.5)