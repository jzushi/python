# Day One, Calorie Counting

# Read in input file with calories list
f = open("input.txt", "r")
calories_packed = f.read()

# Separate calories carried by the elves
packs = calories_packed.split("\n\n")

# Total up the calories 
totals = []
for pack in packs:
    total = sum(eval(item) for item in pack.split('\n'))
    totals.append(total)

# Get the most yolked elf
print(max(totals))

# Find the top 3 
N = 3

def Nmaxelements(totals, N):
    final_list = []
 
    for i in range(0, N):
        max1 = 0
         
        for j in range(len(totals)):    
            if totals[j] > max1:
                max1 = totals[j];
                 
        totals.remove(max1);
        final_list.append(max1)
         
    print(sum(final_list))
 
 
# Calling the function
Nmaxelements(totals, N)