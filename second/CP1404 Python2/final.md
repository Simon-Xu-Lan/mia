![image](https://github.com/Simon-Xu-Lan/mia/assets/60492659/d0eeafc4-3556-4f5f-82fc-c75e0d32e6ee)
### solution
```py
counter = 0
def increment(counter):
    counter += 1
    return counter

increment(counter)
```

![image](https://github.com/Simon-Xu-Lan/mia/assets/60492659/4665fb80-5345-47a6-9b2c-85aeb04a43e7)

### solution
The name also is added to the list names.


![image](https://github.com/Simon-Xu-Lan/mia/assets/60492659/fcb7f52f-59d9-477e-961f-ae08afe5a43c)

### solution
"Create a function to calculate area"

# 5
![image](https://github.com/Simon-Xu-Lan/mia/assets/60492659/8d49be99-350c-44f8-9711-ffdd98b264f0)

### Solution

```py
def student_info(age, country):
    print("Age: {} Country: {}".format(age, country))
```

# 6
![image](https://github.com/Simon-Xu-Lan/mia/assets/60492659/8ac615e3-110d-4fae-a0d3-73be2a0f1a44)

### Solution

```py
from operator import itemgetter
frequency = {}
dna = list("acgtaact")
for letter in dna:
    try: 
        frequency[letter] += 1
    except:
        frequency[letter] = 1
sorted_frequency = dict(sorted(frequency.items(), key=itemgetter(1)))
for key, value in sorted_frequency.items(): 
    print(f"Frequency of {key} is {value}")
```

# 9
![image](https://github.com/Simon-Xu-Lan/mia/assets/60492659/b635671d-3189-43e9-b13d-f02089456e4d)

### solution:
```py
is_valid_float = False
while not is_valid_float:
    user_input = input("Cost of an Apple: ")
    try:
        apple_cost = float(user_input)
        if apple_cost < 0 or apple_cost > 3:
            print("Cost must be between 0 and 3")
        else:
           is_valid_float = True 
    except ValueError:
        print("Invalid input")
    
print(f"Cost of 10 Apples is ${10 * apple_cost:.2f}")
```

# 10
![image](https://github.com/Simon-Xu-Lan/mia/assets/60492659/86816507-bb1e-4cb0-a404-3df16ab4cd90)

### Solution:
a. Library - Book
    - is composed of
b. Bank Account – Fixed Account
    - is a child of
c. Pen - Travel
    - is unrelated to
d. Jim - Person
    - is a child of 




