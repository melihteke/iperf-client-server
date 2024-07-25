#Server Side Code
import subprocess

def run_iperf_server():
    # Run the iperf server on port 5202
    subprocess.run(['iperf3-darwin', '-s', '-p', '5202'])

# Use the function
run_iperf_server()

