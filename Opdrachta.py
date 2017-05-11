"""
This file executes some code that tests how python works. Used for debugging and hypothesizing mistakes/
and looking for ways to improve the code
2017-4-7

Leander
"""
import numpy as np
import time


# We are timing this code!
tstart = time.time()
# Our genome!
Gen1 = np.array([23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9])

# range != [blalala]
sol = range(5)
genes = [1,2,3,4]
bla = [1,2,3,4]

print(sol[0], sol[1], sol[2], sol[3])
print(sol)
print(genes[0], genes[1], genes[2], genes[3])
print(genes)

print("\ngenes==bla: {}".format(genes==bla))
print("genes==sol: {}".format(genes==sol))

# Very strange equation that does not crash
print("2<False:    {}\n".format(2<False))

# searching in a dictionary
archive = dict()
key = "1234567890"
print('archive.get(key,False): {}'.format(archive.get(key,False)))
archive[key] = True
print('archive.get(key,False): {}'.format(archive.get(key,False)))
archive[key] = 23
print('archive.get(key,False): {}'.format(archive.get(key,False)))
print('archive len = {}'.format(len(archive)))
archive["alsfjasldfj"] = 124
archive["alsfjasldfj"] = 125
archive["12345139051012"] = True
print('archive len = {}'.format(len(archive)))

flips = [[1,2], [3,4,], [5,6]]
print("len(flips): {}".format(len(flips)))

genelength = 10
array = []
for i in range(1,genelength+1):
    array.append(i)

print(array)

time.sleep(0.2525)
timed = time.time() - tstart
print("execution duration = {}".format(timed))