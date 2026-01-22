# Log-Analyzer

# Project Title

A Python-based utility to parse network DNS logs using Regular Expressions (Regex). This tool extracts connection metadata and identifies the top 10 most frequent origin IP addresses, helping administrators identify potential network bottlenecks or suspicious activity.
## Features

- Regex Parsing: Uses a robust regular expression to extract timestamps, source/destination IPs, ports, protocols, and DNS queries.
- Traffic Analysis: Utilizes the collections.Counter module for high-performance frequency calculation.
- Timestamp Conversion: Converts Unix epoch timestamps into human-readable YYYY-MM-DD HH:MM:SS format.


## Prerequisties

The script uses standard Python libraries, with a dependency on pandas.

Python 3.x

pandas (Imported but currently optional for the core logic)

``` pip install pandas ```
## Usage/Examples
Prepare the Log File: Ensure your log file is named dns.log and is located in the same directory as the script.

Run the Script:

```python dns_analyzer.py ```
## Log Format Support

Log Format Support
The script is configured to parse tab-separated or space-separated logs with the following structure:

- Timestamp: (e.g., 1541234567.123456)
- Origin Host IP: Source address.
- Origin Port: Source port.
- Response Host IP: Destination address.
- Response Port: Destination port.
- Protocol: (e.g., udp or tcp)
-Query: The domain name being requested.

## Regex Breakdown

The script uses the following named groups for data extraction:

- time_stamp
- ip_origin_host
- ip_origin_p
- ip_responsehost
- ip_responseport
- protocol
- transition
- query

## Example Output

Upon successful execution, the script will output the frequency table to the console:
```
Top 10 most Frequent Origin IPs are:
IP: 192.168.1.10  | Request: 452
IP: 10.0.0.5      | Request: 312
IP: 172.16.0.22   | Request: 89
```
