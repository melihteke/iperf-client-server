# Iperf3 Python Automation 

This project provides a simple Python automation for running Iperf3 network performance tests. It includes scripts for both the server and client sides, facilitating easy setup and execution of network throughput measurements.

## Requirements
- Python 3.x
- Iperf3 installed on both server and client machines. The binary should be named iperf3-darwin on macOS. For other operating systems, you may need to replace iperf3-darwin with iperf3 in the scripts.

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install Iperf3 on both the server and client machines.
- For macOS, use brew install iperf3.
- For Linux, use your distribution's package manager, e.g., apt-get install iperf3 for Debian/Ubuntu.
3. Clone this repository or download the Python scripts to your server and client machines.

## Usage
### Server Side
Run the server script on the machine designated as the server. This will start the Iperf3 server listening on port 5202.
```python
python server_script.py
```

### Client Side
Run the client script from the machine designated as the client, specifying the server's IP address as an argument. This will initiate the Iperf3 test, connecting to the server on port 5202.
```python
python client_script.py <server_ip>
```
>
Replace <server_ip> with the actual IP address of your server.

## Customization
To change the port used for the test, modify the -p argument in both scripts.
For non-macOS systems, replace iperf3-darwin with iperf3 in the subprocess.run command.

## Troubleshooting
Ensure Iperf3 is correctly installed and accessible from the command line on both the server and client machines. If you encounter permission issues, you may need to run the scripts with sudo.
