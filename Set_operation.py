s1 = {10,20,30,40}
s2 = {40, 50, 60}

print(s1.union(s2))

print(s1.intersection(s2))

print(s1.difference(s2))
print(s2.difference(s1))

print(s1.symmetric_difference(s2))

print(s1.isdisjoint(s2))

print({1,2,3}.isdisjoint({10,20,30}))

print({1,2}.issubset({1,2,3,4}))