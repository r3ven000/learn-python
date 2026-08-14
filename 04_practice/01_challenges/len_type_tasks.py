# 1
t = (1, "a", 3.14, True)
print(type(t), len(t))

# 2
items = ["pen", 42, None, [1, 2], {"k": "v"}]
for i in items:
    print(type(i))

# 3
x = input("enter number: ")
if type(x) == str:
    print(len(x))
else:
    print("no string")

# 4
a = "Hello"
b = b"Hello"
print(a, b)  # я незнаю что за форматирование но б делает Hello с кавычками
print(len(a), len(b))


# 5
def typer(object):
    try:
        dic_t = {"type": object, "len": object}
        print(dic_t)
    except:
        dic_t = {"type": object, "len": None}
        print(dic_t)


z = input("enter word: ")
typer(z)
