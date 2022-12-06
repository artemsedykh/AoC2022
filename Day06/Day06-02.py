with open('day06.txt', 'r') as file:
    data = file.read()

i = 13
while i < len(data):
    marker_chars = set(data[i-13:i+1])
    if len(marker_chars) == 14:
        print(i+1)
        break
    i += 1