import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

# Argument parser
parser = argparse.ArgumentParser(description="Subdomain Scanner by Amoon Bhatti")

parser.add_argument("domain", nargs="?", help="Target domain (e.g. example.com)")
parser.add_argument("-t", "--threads", type=int, default=50, help="Number of threads")
parser.add_argument("-o", "--output", help="Save results to file")

args = parser.parse_args()

# 🔥 HYBRID LOGIC
if args.domain:
    domain = args.domain
else:
    domain = input("Enter target domain: ")

threads = args.threads
output_file = args.output

print(f"\nScanning {domain} using {threads} threads...\n")

# Load wordlist
with open("wordlist.txt", "r") as file:
    subdomains = file.read().splitlines()

found_list = []

# Scan function
def scan(sub):
    subdomain = sub + "." + domain

    try:
        ip = socket.gethostbyname(subdomain)
        print(f"[FOUND] {subdomain}  | IP: {ip}")
        found_list.append(f"{subdomain} | {ip}")
    except:
        pass

# Multithreading
with ThreadPoolExecutor(max_workers=threads) as executor:
    executor.map(scan, subdomains)

# Save results
if output_file:
    with open(output_file, "w") as f:
        for sub in found_list:
            f.write(sub + "\n")

    print(f"\nResults saved in {output_file}")

print("\nScan Completed 🔥")