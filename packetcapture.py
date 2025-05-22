import os
import json
import time
import sys
from getdownloaddirectory import get_downloads_directory
from file import pcaporjson
from file import compress_pcap_file
from scapy.all import sniff, wrpcap
from datetime import datetime



# Capture function
def capture_packets(duration = 900):
    start_time = time.time()  # Get start time

    file_type = pcaporjson() # PCAP or JSON

    print("Capturing Packets")

    def stop_capture(_):
        return time.time() - start_time > duration

    # Define a capture filter for specific traffic (simplified)
    capture_filter = (
    "udp port 53 or tcp port 443 or arp or icmp "  # DNS, HTTPS, ARP, ICMP
    "or tcp port 80 or tcp port 22 or tcp port 21 or tcp port 25 "  # HTTP, SSH, FTP, SMTP
    "or ip or ip6 "  # Capture all IPv4 and IPv6 traffic
    "or tcp or udp"  # Capture all TCP and UDP packets
)
    try:
        # Capture packets for a fixed duration or until manually stopped
        packets = sniff(filter=capture_filter, stop_filter=stop_capture)

    except KeyboardInterrupt:
        print("\nCapture manually stopped. Saving packets...")

    # Get the Downloads directory path
    downloads_folder = get_downloads_directory()

    # Check if the Downloads folder exists and is writable
    if not os.path.exists(downloads_folder):
        raise Exception(f"Downloads directory {downloads_folder} does not exist.")
    if not os.access(downloads_folder, os.W_OK):
        raise PermissionError(f"Not allowed to write to {downloads_folder}")

    # Define timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Save to JSON file
    if file_type == 2:
        json_file_path = os.path.join(downloads_folder, f"packetdata_{timestamp}.json")

        try:
            packets_json = [packet.show(dump=True) for packet in packets if packet is not None]  # Ignore None packets
            with open(json_file_path, "w") as f:
                json.dump(packets_json, f, indent=4)
            print(f"Captured {len(packets)} packets in {duration/60:.2f} minute(s), saved to: {json_file_path}")
        except Exception as e:
            print(f"Error saving JSON file: {e}")

    # Save to PCAP file
    if file_type == 1:
        pcap_file_path = os.path.join(downloads_folder, f"packetdata_{timestamp}.pcap")

        try:
            if packets:  # Ensure packets were captured before writing
                wrpcap(pcap_file_path, packets)
                compress_pcap_file(pcap_file_path)
                print(f"Captured {len(packets)} packets in {(time.time() - start_time)/60:.2f} minute(s), saved to: {pcap_file_path}")
            else:
                print("No packets captured, skipping PCAP file save.")
        except Exception as e:
            print(f"Error saving PCAP file: {e}")

    sys.exit()




 