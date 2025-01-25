from collections import deque

command = input()
customers = deque()

while command != "End":
    if command == "Paid":
        while customers:
            print(customers.popleft())
    elif command != "Paid":
        customer_name = command
        customers.append(customer_name)

    command = input()

print(f"{len(customers)} people remaining.")
