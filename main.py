from getssid import get_ssid
from packetcapture import capture_packets





# Run the program
if __name__ == "__main__":
    # Start the timer thread
    print(f"Connected to WiFi SSID: {get_ssid()}")
    print("Starting packet capture...")
    print("CTRL + C to end capture early.")
    capture_packets()
    print("Maximum Packet reached")
   
    