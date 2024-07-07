import time


def wait_for_timeout(timeout_seconds):
    print(f"Waiting for {timeout_seconds} seconds for the key to expire...")
    time.sleep(timeout_seconds)
