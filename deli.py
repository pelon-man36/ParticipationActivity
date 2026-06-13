sandwich_orders = ["tuna", "turkey", "ham", "veggie", "cheese"]
finished_sandwiches = []

while sandwich_orders:
    current = sandwich_orders.pop()
    print(f"Made your {current.title()} sandwich.")
    finished_sandwiches.append(current)
