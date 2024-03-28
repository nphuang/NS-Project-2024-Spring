import subprocess

def execute_curl_command():
    socks5_proxy = "localhost:1080"
    remote_hostname = "https://www.google.com"
    curl_command = f"curl --socks5-hostname {socks5_proxy} {remote_hostname}"

    try:
        output = subprocess.check_output(curl_command, shell=True)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error executing curl command: {e}")

if __name__ == "__main__":
    execute_curl_command()
