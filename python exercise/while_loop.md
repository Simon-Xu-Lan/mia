<details><summary>while loop</summary>

### while loop execute a set of statements as long as a condition is true.

```py
while condition:
    # body of while loop
```

1. A while loop evaluates the condition
2. If the condition evaluates to True, the body(the code inside the while loop) is executed.
3. condition is evaluated again.
4. If the condition evaluates to True, the body(the code inside the while loop) is executed again.
5. This process continues until the condition is False.
6. When condition evaluates to False, the loop stops.

## Flowchart of while loop

<img src="images/python-while-loop.png" width="800px"/>

## Example of while loop

```py
i = 1
while i < 6:
    print(i)
    i += 1
print("After while loop")
```

```py
# Create a variable to control the loop. Set the initial value as 1
i = 1
# Test the condition. if true, enter into while loop. if false, go the the statements after loop.
while i < 6:
    # Body of while loop
    print(i)
    # increase the variable i by 1
    i += 1
# Statement after while loop
print("After while loop")
```

<img src="images/Example1.png" width="500px">

<img src="images/while-loop-example-1.png" width="500px" />

</details>

<details><summary>While loop with break</summary>

# break can stop the loop if the while condition is true.

## Example: Exit the loop when i is 3

```py
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print("Statements after loop")
```

```py
# Create a varialbe to control loop. Set initial/start value as 1
i = 1
# Test condition. if true, enter into while loop; if False, go to statements after loop
while i < 6:
    # body of while loop
    print(i)
    # check if i is 3. if true, execute break statement which will break the loop, the program will move to the statement after loop. If false, move to the next statement in the body of while loop (statement after if)
    if i == 3:
        break
    # increase i by 1
    i += 1

print("Statements after loop")
```

<img src="images/while-loop-break.png" width="500px" />

</details>
