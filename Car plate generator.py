letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "R", "X", "Y", "Z"]
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
car_plate = []
for l1 in letters:
    for l2 in letters:
        for n1 in nums:
            for n2 in nums:
                for n3 in nums:
                    car_plate.append(l1 + l2 + str(n1) + str(n2) + str(n3))
print(car_plate)