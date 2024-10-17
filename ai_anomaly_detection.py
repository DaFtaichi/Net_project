import pandas as pd
from sklearn.ensemble import IsolationForest
import scapy.all as scapy

def capture_traffic():
    # Capture network traffic using scapy
    packets = scapy.sniff(filter="ip", count=1000)
    return packets

def analyze_traffic(packets):
    # Feature extraction (e.g., IP addresses, packet sizes)
    data = [{'src': packet[scapy.IP].src, 'dst': packet[scapy.IP].dst, 'len': len(packet)} for packet in packets]
    df = pd.DataFrame(data)

    # Train an Isolation Forest model to detect anomalies
    model = IsolationForest(contamination=0.01)
    model.fit(df[['len']])
    df['anomaly'] = model.predict(df[['len']])
    
    # Identify anomalous packets
    anomalies = df[df['anomaly'] == -1]
    print(f"Detected {len(anomalies)} anomalies")
    return anomalies

packets = capture_traffic()
analyze_traffic(packets)
