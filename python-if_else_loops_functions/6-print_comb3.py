#!/usr/bin/python3
for count in range(10):
    for count2 in range(count + 1, 10):
        print("{}{}".format(count, count2), end="")

        if count != 8:
            print(", ", end="")


print("")
