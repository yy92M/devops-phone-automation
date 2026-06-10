import requests
import datetime

def check_site(url):
    try:
        response = requests.get(url, timeout=5)
        status = f"Status Code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        status = f"Error: {e}"
        
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | URL: {url} | {status}\n"
    
    with open("site_monitor.log", "a") as f:
        f.write(log_entry)
    
    print(log_entry.strip())

if __name__ == "__main__":
    # Check Google as a test
    check_site("https://www.google.com")
