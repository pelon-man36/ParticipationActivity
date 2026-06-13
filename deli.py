sandwich_orders = ["tuna", "turkey", "ham", "veggie", "cheese"]
finished_sandwiches = []

while sandwich_orders:
    current = sandwich_orders.pop()
    print(f"I have made your {current.title()} sandwich.")
    finished_sandwiches.append(current)

while finished_sandwiches:
    current = finished_sandwiches.pop(0)
    

