import re
from collections import Counter
import pandas as p
import datetime
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
    with open(file_path,'r') as f:
        for line in f:
            if line.startswith('#'):
                continue

            for match in re.finditer(rexp, line):
                # print(f"match_text: {match.group('query')} from {match.group('ip_origin_host')}")
                ip = match.group('ip_origin_host')
                ts_value = float(match.group('time_stamp'))
                timestamp = datetime.datetime.fromtimestamp(ts_value)

                ip_list.append(ip)
    print("Top 10 most Frequest Origin Ips are")
    top_ips = Counter(ip_list).most_common(10)

    for ip, count in top_ips:
        print(f"IP: {ip} | Request: {count}")


    
    # print(f"At Time: {timestamp.strftime('%Y-%m-%d %H:%M:%S')} query {match.group('query')} from {match.group('ip_origin_host')}")
except FileNotFoundError:
    print(f"Error: the file at {file_path} was not found.")




