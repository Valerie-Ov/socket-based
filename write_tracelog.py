import subprocess
from urllib.parse import urlparse

def write_logs(url):
    parsed = urlparse(url)
    log_file = "traceroute.log"

    try:
        with open(log_file, 'r') as f:
            subprocess.run(
                ["traceroute", parsed.netloc],
                stdout=f,
                stderr=subprocess.STDOUT,
                check=True
            )
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] traceroute failed with return code {e.returncode}")
    except FileNotFoundError:
        print("[ERROR] 'traceroute' command not found. Is it installed?")
    except Exception as e:
        print(f"[ERROR] Unexpected error during traceroute: {e}")
