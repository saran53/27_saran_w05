import random

print(f"{random.random}")
print(f"{random.random(1,99)}")
print(f"{random.randrange(1,10,2)}")
print(f"{random.uniform(2,100):.4f}")


colors = ["rad" , "green" , "blue" , "bleak" , "white"]

random_list = random.choice(colors) # สุ่มใน list
random_3 = random.choices(colors, k=3) #สุ่มใน list ออกมา 3 ค่า
random_uniq = random.sample(colors, 3)



numbers = list(range(1,100))
print(numbers)
random.shuffle(numbers)
print("===========================")
print(numbers)