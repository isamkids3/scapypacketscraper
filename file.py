# Handling file type and compression of PCAP file
import sys
import gzip
import shutil

def pcaporjson():
    input1 = input("Would you like to capture your packets into PCAP or JSON?")
    if input1 == "PCAP" or input == "pcap":
        return 1
    elif input1 == "JSON" or input == "json":
        return 2
    else: 
        print("Please type in either PCAP or JSON")
        sys.exit()
        

def compress_pcap_file(filename):
    try:
        with open(filename, 'rb') as f_in:
            with gzip.open(f"{filename}.gz", 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"Compressed {filename} to {filename}.gz")
    except Exception as e:
        print(f"Error compressing {filename}: {e}")