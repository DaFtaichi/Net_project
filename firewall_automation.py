import requests

def block_ip(ip, api_token):
    """
    Block a suspicious IP address using the pfSense API.
    
    Args:
        ip (str): The IP address to block.
        api_token (str): The authentication token for the pfSense API.
    """
    url = "http://pfsense.local/api/firewall"  # Replace with your pfSense URL
    headers = {"Authorization": f"Bearer {api_token}"}
    
    payload = {"action": "block", "ip": ip}  # Payload to block the IP
    
    try:
        response = requests.post(url, json=payload, headers=headers)  # Send request to block the IP
        response.raise_for_status()  # Check if the request was successful
        print(f"Successfully blocked IP {ip}.")
    except requests.exceptions.RequestException as e:
        print(f"Error while blocking IP {ip}: {e}")

if __name__ == "__main__":
    # List of suspicious IPs (example)
    suspicious_ips = ['192.168.1.100', '192.168.1.101']
    api_token = "YOUR_API_TOKEN"  # Replace with your API token
    
    # Block each suspicious IP
    for ip in suspicious_ips:
        block_ip(ip, api_token)
