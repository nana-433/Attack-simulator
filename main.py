from log_generator import generate_log
from attacker_sim import simulate_attack
from detector import detect_brute_force

# choose mode
logs = []

mode = "attack"  # change to "normal" or "attack"

if mode == "attack":
    logs = simulate_attack()
else:
    for i in range(30):
        logs.append(generate_log())

for log in logs:
    print(log)

detect_brute_force(logs)
