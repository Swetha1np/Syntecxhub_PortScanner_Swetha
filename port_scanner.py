import socket
import threading
import time
from datetime import datetime

target = input("Enter target IP or website: ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

print("\nScanning target:", target)
print(f"Scanning ports {start_port} to {end_port}")

start_time = time.time()
scan_time = datetime.now()

print("\n=============================")
print("Scan Time:", scan_time)
print("Target:", target)
print(f"Ports: {start_port} - {end_port}")
print("=============================")

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")

        s.close()

    except:
        pass

threads = []

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()

print("\nScan completed.")
print(f"Total scan time: {round(end_time - start_time, 2)} seconds")
