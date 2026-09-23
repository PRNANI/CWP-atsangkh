original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

for num in original_array: 
    if num > 5: 
        new_array.append(num + 2) #มากกว่า 5 บวก 2 แล้วใส่อาเรย์ใหม่

print(original_array)
print(new_array)