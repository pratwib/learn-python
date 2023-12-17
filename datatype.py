x = 6
print(type(x))
x = 6.0
print(type(x))
x = 1 + 2j
print(type(x))

var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

x = True
print(type(x))
x = False
print(type(x))

x = "Dicoding"
print(type(x))
print(x[0])
print(x[2:])
# x[0] = "F" ERROR

multi_line = """Pratama
Wibi"""
print(multi_line)

name = "Pratama Wibi"
print(f"Hello, nama saya {name}")

name = "Pratama Wibi"
print("Nama saya %s" % (name))

name = "Pratama Wibi"
print("Nama saya {}".format(name))

x = [1, 2.3, "Dicoding"]
print(type(x))
print(x[2])
x[0] = "Indonesia"
print(x)
print(x[-1])

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
print(x[0:5:2])
print(x[1:])
print(x[:3])

x = (1, "Dicoding", 1 + 3j)
print(type(x))
print(x[1])
print(x[0:3])
# x[1] = "Dicoding" ERROR CANNOT CHANGE

x = {1, 2, 3, 2, 3, 13, 3, 4}
# print(x[0]) ERROR DIDNT HAVE INDEXES
print(x)
print(type(x))

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set1.union(set2)
print("Union: ", union)
intersection = set1.intersection(set2)
print("Intersection: ", intersection)

x = {"name": "Pratama Wibi", "age": 20, "isMarried": False}
print(type(x))
print(x["name"])
x["job"] = "Web Developer"
print(x)
del x["isMarried"]
print(x)
x["name"] = "Fairuz"
print(x)

print(float(5))
print(int(5.6))
print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))
# print(int("1p")) ERROR

print(set([1, 2, 3]))
print(tuple({5, 6, 7}))
print(list("hello"))

print(dict([[1, 2], [3, 4]]))
print(dict([(3, 26), (4, 44)]))
