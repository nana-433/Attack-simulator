import random
from datetime import datetime

users = ["admin", "nana", "guest"]
ips = ["192.168.1.1", "192.168.1.10","10.0.0.5"]

events = ["LOGIN_SUCCESS", "LOGIN_FAIL", "ACCESS_GRANTED"]

def generate_log():
    user = random.choice(users)
    ip = random.choice(ips)
    event = random.choice(events)
    time = datetime.now().strftime("%H:%M:%S")

    log = f"[{event}] user={user} ip={ip} time={time}"
    return log
users = ["admin", "nana", "guest", "root"]
ips = ["192.168.1.1", "192.168.1.10", "10.0.0.5", "172.16.0.2"]
events = ["LOGIN_SUCCESS", "LOGIN_FAIL", "ACCESS_GRANTED", "ACCESS_DENIED"]
