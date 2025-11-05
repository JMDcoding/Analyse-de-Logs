# Script 1: Traitement de logs avec des algorithmes de traitement de chaines

def parse_logs_with_strings(log_file):
    with open(log_file, "r") as file:
        for line in file:
            parts = line.split(" ")
            ip = parts[0]
            timestamp = parts[3][1:] + " " + parts[4][:-1]  # Suppression des crochets
            method = parts[5][1:]  # Suppression du premier guillemet
            path = parts[6]
            status = parts[8]
            print(f"IP: {ip}, Timestamp: {timestamp}, Method: {method}, Path: {path}, Status: {status}")

# Utilisation
log_file_1 = "Log1.txt"  # Remplace par le chemin correct
parse_logs_with_strings(log_file_1)


# Script 2: Traitement de logs avec des expressions régulières
import re

def parse_logs_with_regex(log_file):
    log_pattern = re.compile(r"(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] \"(\w+) (.*?) HTTP/1.1\" (\d+)")
    
    with open(log_file, "r") as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                ip, timestamp, method, path, status = match.groups()
                print(f"IP: {ip}, Timestamp: {timestamp}, Method: {method}, Path: {path}, Status: {status}")

# Utilisation
log_file_2 = "Log1.txt"  # Remplace par le chemin correct
parse_logs_with_regex(log_file_2)
