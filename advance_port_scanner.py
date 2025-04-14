import socket
import threading

# Lock for synchronized console output
print_lock = threading.Lock()

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set timeout to 1 second
        result = s.connect_ex((ip, port))
        if result == 0:
            with print_lock:
                print(f"[+] Port {port} is open")
        s.close()
    except Exception as e:
        pass  # Ignore errors for now

def main():
    target = input("Enter target IP: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

    threads = []

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\nScan complete.")

if __name__ == "__main__":
    main()
