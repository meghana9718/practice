import os

def print_system_uptime():
    try:
        # For Linux/Unix systems
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            hours = int(uptime_seconds // 3600)
            minutes = int((uptime_seconds % 3600) // 60)
            seconds = int(uptime_seconds % 60)
            print(f"System uptime: {hours} hours, {minutes} minutes, {seconds} seconds")
    except FileNotFoundError:
        # For Windows systems
        import subprocess
        output = subprocess.check_output("net stats workstation", shell=True, text=True)
        for line in output.split('\n'):
            if "Statistics since" in line:
                print("System uptime since:", line.split("Statistics since")[1].strip())
                break

if __name__ == "__main__":
    print_system_uptime()
