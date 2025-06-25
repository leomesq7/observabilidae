import random
from datetime import datetime, timedelta

# Caminho do arquivo
with open("data/app.log", "w") as file:
    timestamp = datetime(2024, 11, 8, 10, 0, 0)
    levels = ["INFO", "DEBUG", "ERROR", "WARN"]
    messages = [
        "User admin logged in",
        "Failed to connect to database",
        "Query executed in 120ms",
        "User admin accessed dashboard",
        "Connection pool running low",
        "Query executed in 80ms",
        "Service timeout error",
        "User guest failed login",
        "Cache cleared successfully"
    ]

    for _ in range(1_000_000):
        time_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        level = random.choice(levels)
        message = random.choice(messages)
        file.write(f"{time_str} {level} {message}\n")
        timestamp += timedelta(seconds=random.randint(1, 5))
