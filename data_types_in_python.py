
print("---------------------Integer--------------------")
### Integer
x=20
print(type(x))

x=-15
print(type(x))
print("---------------------Float--------------------")
### float
x=1.15
print(type(x))

x=-1.15
print(type(x))
print("---------------------Complex--------------------")
###Complex
x=(3+4j)
print(type(x))

x=(3+20j)
print(type(x))

x=-3-4j
print(type(x))

data="data Science"
print(data)

print("---------------------Even Characters in a string--------------------")

# # ##### EVEN CHARACTERS
for i in range (len(data)):
  if i%2==0:
    print(data[i])

# print("---------------------Odd Characters in a string--------------------")

# # # ##### ODD CHARACTERS
for i in range (len(data)):
  if i%2!=0:
    print(data[i])
print("---------------------One by one letter--------------------")

for i in range (len(data)):
  print(data[:i+1])

