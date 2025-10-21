import random
from src.pite_project1.usefullFunctions import save

# Generate 100 records with random status and value
records = []
for i in range(100):
    status = random.choice(["ok", "bad", "error", "OK", "Bad"])
    # mix of int, float, str values
    val_type = random.choice(["int", "float", "str", "none"])
    if val_type == "int":
        value = random.randint(0, 100)
    elif val_type == "float":
        value = round(random.uniform(0, 100), 2)
    elif val_type == "str":
        value = str(random.randint(0, 100))
    else:
        value = None
    records.append({"status": status, "value": value})

# Save to file
save("data/sample_100.json", records)

