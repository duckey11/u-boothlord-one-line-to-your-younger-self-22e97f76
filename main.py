import os

ENTRY = "Spend the $20 you stole from Grandma Rose's purse, kid, you'll spend twenty years trying to repay it in flowers she never lived to smell."

# Guard: exactly one line, 1-200 chars, no trailing newline.
assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of bounds"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
