import random

def simulate_attack():
    ips = ["192.168.1.10", "10.0.0.5", "172.16.0.2"]

    attacks = []

    for i in range(20):
        ip = random.choice(ips)

        log = f"[LOGIN_FAIL] user=admin ip={ip} time=12:{i:02d}"
        attacks.append(log)

    return attacks