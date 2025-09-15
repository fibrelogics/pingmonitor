import os
import platform
import subprocess

def ping(host):
    """
    Pings a host (IP or domain).
    Returns True if reachable, False if not.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        return True, output
    except subprocess.CalledProcessError:
        return False, None

def main():
    print("=== FibreLogics Ping Monitor (Beta) ===")
    ip = input("Enter IP address to ping: ").strip()

    if not ip:
        print("No IP entered. Exiting...")
        return

    print(f"Pinging {ip} ...")
    status, details = ping(ip)

    if status:
        print(f"✅ {ip} is UP")
    else:
        print(f"❌ {ip} is DOWN")

if __name__ == "__main__":
    main()
