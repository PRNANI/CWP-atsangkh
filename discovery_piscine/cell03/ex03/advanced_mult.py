import sys

if len(sys.argv) > 1:
    print("Error")
    sys.exit()

i = 0
while i <= 10: 
    j = 0
    line = []
    while j <= 10:
        line.append(str(i * j))
        j += 1
    print(f"Table de {i}: " + " ".join(line))
    i += 1