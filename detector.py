def detect_brute_force(logs):
    failed_attempts = {}


    for log in logs:
        if "LOGIN_FAIL" in log:
            parts = log.split()

            ip = None
            for part in parts:
                if part.startswith("ip="):
                    ip = part.split("=")[1]

            if ip:
                if ip not in failed_attempts:
                    failed_attempts[ip] = 0
                failed_attempts[ip] += 1

    # Analyze results
    for ip, count in failed_attempts.items():

        if count >= 7:
            print(f" HIGH ALERT: ACTIVE ATTACK DETECTED from {ip} ({count} fails)")
        elif count >= 5:
            print(f" MEDIUM ALERT: Possible brute force from {ip} ({count} fails)")
        elif count >= 3:
            print(f" LOW ALERT: Suspicious activity from {ip} ({count} fails)")

