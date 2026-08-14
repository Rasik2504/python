str=input("Enter:")
reverse=str[::-1]
forward=str[:3]
backward=str[-7:]+str[-2:]
limit=str[3:5]
print(limit)
print(reverse)
print(forward)
print(backward)

print(str.partition("is"))
print(str.split())

print(str.startswith("My",0))
print(str.lstrip(" girl"))