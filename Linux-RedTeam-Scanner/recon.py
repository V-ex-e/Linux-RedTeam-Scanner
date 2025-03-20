import os
import socket
import subprocess

def get_system_info():
    info = {
        "OS": os.uname().sysname,
        "Kernel": os.uname().release,
        "Hostname": socket.gethostname(),
        "User": os.getenv("USER"),
    }
    return info

def get_running_processes():
    processes = subprocess.getoutput("ps aux --sort=-%mem | head -10")
    return processes

def get_network_info():
    interfaces = subprocess.getoutput("ip -br addr")
    open_ports = subprocess.getoutput("netstat -tulnp | grep LISTEN")
    return interfaces, open_ports

if __name__ == "__main__":
    print("🔍 Gathering System Info...")
    print(get_system_info())
    print("\n🔍 Running Processes (Top 10 Memory Usage):")
    print(get_running_processes())
    print("\n🔍 Network Info:")
    interfaces, open_ports = get_network_info()
    print("Interfaces:\n", interfaces)
    print("Open Ports:\n", open_ports)
