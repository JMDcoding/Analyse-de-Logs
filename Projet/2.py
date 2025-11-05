import re

def analyse_log_regex(log_file):
    pattern = re.compile(r'\[(.*?)\] (ERROR|WARNING|INFO): (.*)')
    with open(log_file, 'r') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                timestamp, level, message = match.groups()
                print(f"{level} détecté à {timestamp}: {message}")

# Exemple d'utilisation
analyse_log_regex('log2.txt')
