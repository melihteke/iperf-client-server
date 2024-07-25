#Client Side Code
import subprocess

def run_iperf_client(server_ip):
    # Run the iperf client and connect to port 5202
    subprocess.run(['iperf3-darwin', '-c', server_ip, '-p', '5202'])

# Use the function
run_iperf_client('192.168.178.240')
