# common viva problem
import time

end = 1000
start_time1 = time.time()

for i in range(1,end): # range (start, stop)
    output = ""
    if i % 3 == 0:
        output += "Fizz "
    if i % 5 == 0:
        output += "Buzz "
    if output == "":
        output += str(i)
    print(output)

end_time1 = time.time()

# another way
start_time2 = time.time()
for j in range (1,end):
    if j % 15 == 0:
        print("Fizz Buzz")
    elif j % 3 == 0:
        print("Fizz")
    elif j % 5 == 0:
        print("Buzz")
    else:
        print(j)

# Time comperasion
end_time2 = time.time()
elapsed_time1 = end_time1 - start_time1
elapsed_time2 = end_time2 - start_time2

print(f" String Method time = {elapsed_time1}\n If Else Method time = {elapsed_time2} ")
fast = (elapsed_time1 - elapsed_time2) * 1000
print(f" 2nd method is {fast} mili-second faster") 