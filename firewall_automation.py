import requests

# Automatically block suspicious IPs using pfSense API
def block_ip(ip):
    url = "http://pfsense.local/api/firewall"
    headers = {"Authorization": "Bearer YOUR_API_TOKEN"}
    payload = {"action": "block", "ip": ip}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Successfully blocked {ip}")
    else:
        print(f"Failed to block {ip}")

suspicious_ips = ['192.168.1.100', '192.168.1.101']  # Example list
for ip in suspicious_ips:
    block_ip(ip)
