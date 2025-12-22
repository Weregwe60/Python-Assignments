#'''7-9'''
Sandwich_orders =[
    'tuna',
    'chicken',
    'veggie ',
    'pastrami',
    'egg'
]
Finished_Sandwiches = []
print("Starting sandwich orders:", Sandwich_orders)

while Sandwich_orders:
    current_order =Sandwich_orders.pop(0)
    print(f"I made your {current_order} sandwich.")
    Finished_Sandwiches.append(current_order)
print("\nSandwiches made:")
for sandwich in Finished_Sandwiches:
    print(f"-{sandwich.title()} sandwich")

#'''7-9'''
print("\nExercise 7-9: No Pastrami")
Sandwich_orders =[
    'Tuna',
    'pastrami',
    'chicken',
    'pastrami',
    'veggie',
    'egg',
    'pastrami'
]
Finished_Sandwiches =[]

print("Starting sandwich orders:", Sandwich_orders)
print("Sorry, the deli has runout of pastrami.")

while "pastrami" in Sandwich_orders:
    Sandwich_orders.remove("pastrami")
print("Update orders (no pastrami):",Sandwich_orders)
while Sandwich_orders:
    current_order =Sandwich_orders.pop(0)
    print(f"I made your {current_order} sandwich")
    Finished_Sandwiches.append(current_order)
print("\nFinal list of finished sandwiches:")
for sandwich in Finished_Sandwiches:
    print(f" -{sandwich.title()} sandwich")

if "pastrami" in Finished_Sandwiches:
    print("Error: 'pastrami ended up in Finished_Sandwiches!")
else:
    print("Confirmed: no pastrami sandwiches in Finished_Sandwiches.")


input(0)
