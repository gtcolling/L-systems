
#Demonstration of a D0L-system (deterministic and 0-context / context-free)
#implemented using nested for loop

import time


def main():
    #starting string
    s = "b"
    #number of generations
    gen = 20

    #ex_1 nested forloop
    start = time.time()
    ex_1(s, gen)
    end = time.time()
    ex1 = str(end - start) + " seconds"

    print(ex1)

def ex_1(s, gen):
    new = s
    for x in range(gen):
        print("Generation " + str(x + 1) + ": " + str(new))
        temp = ''
        for y in range(len(new)):
            if new[y] == 'a':
                temp += 'ab'
            elif new[y] == 'b':
                temp += 'a'
        new = temp

def ex_2(s, gen, count):
    if gen == count - 1:
        return
    print("Generation " + str(count) + ": " + s)
    temp = ''
    for x in range(len(s)):
        if s[x] == 'a':
            temp += 'ab'
        elif s[x] == 'b':
            temp += 'a'
    count += 1
    ex_2(temp, gen, count)



main()
