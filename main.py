

numbers = [5, 20, 30, 30, 50]
delval = int(input('Enter the deletion value: '))

# ******************************
# Make your Code
# ******************************
check = True
original_size = len(numbers)
while(check):
    try:
        numbers.remove(delval)
        check = True
    except:
        check = False
if len(numbers) is original_size:
    numbers.clear()
print(numbers)