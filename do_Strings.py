# This project is all 'bout string operators.
# An input text will be processed through chosen string method
# The string method determined by the user's(me) input
# It has to be here words looking statement(for "word" in)

cte = '"insert text for conducting our testing:\n"'
print(len(cte))

request = str(input("task: "))
if request == "chop":
    start = int(input())
    ending = int(input())
    print(cte[start: ending])

elif request == "list":
    lT = input("what type of list?\n")
    if lT == "whole":
        for w in cte:
            print(w)
    elif lT == "a slice":
        a_s = int(input("the index of the slice?\n"))
        print(cte[a_s])
    elif lT == "cut 'til end":
        print(cte[int(input()):])
    elif lT == "cut end to 'til":
        print(cte[:int(input())])

elif request == "upper":   # upper and lower brothers are here
    print(cte.upper())
elif request == "lower":
    print(cte.lower())

elif request == "replace":    # replace method is on position
    t_object = input("replacing object: ")
    p_object = input("given object: ")
    print(cte.replace(t_object, p_object))

elif request == "check":                # FKN helper erased my comment
    check = input("look for:\n")
    print(check in cte)

elif request == "check&count":
    lost = str(input("I look for "))
    count = 0
    for z in cte:                # I see now. I have no idea how for loops statement works
        if z == lost:            # Whatever I do it ends up by spamming by unwanted text
            count += 1
    if count > 0:                # Now I have the slightest idea of how it works
        print(count)
    else:
        print("There is no such a character")


elif request == "print":
    print(cte)


elif request == "strip":
    print(cte.strip())



else:
   print("finish your code")

# In total, it should have 8 string operators
