items = ["apple", "banana", "apple" ,"orange", "apple", "mango"]

unique_items = set()

for item in items:
    if item  in unique_items:
       print("Duplicate item found:", item)
       break
    
    unique_items.add(item)
    print("Adding item:", item)