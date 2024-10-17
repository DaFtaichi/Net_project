import pandas as pd
from sklearn.ensemble import IsolationForest
import scapy.all as scapy

def capture_traffic():
    """
    Capture network traffic using Scapy.
    Returns a list of captured packets.
    """
    try:
        packets = scapy.sniff(filter="ip", count=1000)  # Capture 1000 IP packets
        return packets
    except Exception as e:
        print(f"Error while capturing traffic: {e}")
        return []

def analyze_traffic(packets):
    """
    Analyze the captured traffic to detect anomalies using the Isolation Forest algorithm.
    Returns the packets identified as anomalies.
    """
    if not packets:
        print("No packets to analyze.")
        return []

    # Extract features (source address, destination, and packet size)
    data = [{'src': packet[scapy.IP].src, 'dst': packet[scapy.IP].dst, 'len': len(packet)} for packet in packets]
    
    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data)
    
    # Initialize the Isolation Forest model
    model = IsolationForest(contamination=0.01)  # Adjust contamination rate as needed
    model.fit(df[['len']])  # Train the model on packet sizes
    
    # Predict anomalies
    df['anomaly'] = model.predict(df[['len']])
    
    # Identify anomalous packets
    anomalies = df[df['anomaly'] == -1]
    print(f"Detected anomalies: {len(anomalies)}")
    
    return anomalies

if __name__ == "__main__":
    packets = capture_traffic()  # Capture traffic
    anomalies = analyze_traffic(packets)  # Analyze traffic to detect anomalies

