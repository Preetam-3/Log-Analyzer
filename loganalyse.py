import re
from collections import Counter
import datetime


# Define the Regular Expressions to parse the specific format of the dns.log file  
rexp = re.compile(
        r'(?P<time_stamp>\d{1,10}\.\d{1,8})\s+(?:\S+\s+){1}' + 
        r'(?P<ip_origin_host>\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3})\t+' + 
        r'(?P<ip_origin_p>\d{5})\t+' + 
        r'(?P<ip_responsehost>\d{1}.\d{1}.\d{1}.\d{1})\t+' + 
        r'(?P<ip_responseport>\d{2})\t+(?P<protocol>\w{1,10})\t+' + 
        r'(?P<transition>\d{1,7})\t+(?:\S+\s+)' +
        r'(?P<query>[\w-]+(?:\.[\w-]+)*)'

)
file_path = '/home/niku/Downloads/dns.log'
ip_list = []
try:
    with open(file_path,'r') as f: # Open the file in read-only mode
        for line in f:
            if line.startswith('#'):
                continue

            for match in re.finditer(rexp, line): #Search for the regex pattern in the current line
                ip = match.group('ip_origin_host') # Extract the source IP address from the match group
                ts_value = float(match.group('time_stamp')) # Convert the string timestamd to float
                timestamp = datetime.datetime.fromtimestamp(ts_value) # Convert the timestamp to readable datetime object

                ip_list.append(ip) # Store the IP in our list for counting
    print("Top 10 most Frequest Origin Ips are") # Use Counter to find the frequency of each IP address
    top_ips = Counter(ip_list).most_common(10)

    for ip, count in top_ips: # Iterate through the results and print them clearly
        print(f"IP: {ip} | Request: {count}")
    # print(f"At Time: {timestamp.strftime('%Y-%m-%d %H:%M:%S')} query {match.group('query')} from {match.group('ip_origin_host')}")
except FileNotFoundError:
    print(f"Error: the file at {file_path} was not found.")




