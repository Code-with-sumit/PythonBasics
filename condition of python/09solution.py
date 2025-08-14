items = ["apple","banana","orange"]
unique_items = set()
for item in items:
      if items in unique_items:
          print("Duplicate:",item)
          break
      unique_items.add(item)
      