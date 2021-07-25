l = [1, 2, 3]
l.append([4, 5])

l1 = l
l2 = l[:]

l1[1:3] = ["Otto", "Peter"]
l2[3:5] = l[3]
l2[0] = -l2[-1]
l2[1] = -l2[-2]
l[1] = "abc"

print(l)
print(l1)
print(l2)