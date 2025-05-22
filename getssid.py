#Code to get SSID
import subprocess
import platform

def get_ssid():
        try:
            system = platform.system()

            if system == "Windows":
                raw_wifi = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces'], text=True)
                for line in raw_wifi.split("\n"):
                    if "SSID" in line and "BSSID" not in line:
                        return line.split(":")[1].strip()

            elif system == "Darwin":  # macOS
                raw_wifi = subprocess.check_output(
                    "system_profiler SPAirPortDataType | awk '/Current Network/ {getline;$1=$1;gsub(\":\",\"\");print;exit}'",
                    text=True,
                    shell=True  # Needed for pipes
                ).strip()  # Strip to remove extra spaces or newlines
                return raw_wifi

            elif system == "Linux":
                raw_wifi = subprocess.check_output(['nmcli', '-t', '-f', 'active,ssid', 'dev', 'wifi'], text=True)
                for line in raw_wifi.split("\n"):
                    if line.startswith("yes:"):
                        return line.split(":")[1].strip()

            return "SSID not found"

        except Exception as e:
            return f"Error retrieving SSID: {e}"
    

