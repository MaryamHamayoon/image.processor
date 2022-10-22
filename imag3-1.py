from tkinter import Y


# it will say merhaba python and also say that which number is bigger 

print("merhaba python")
a=20;
b=43;
if a>b:
    print("a büyüktür")
else :
 print("b büyüktür")


######################################## work second please enter the value for the code below


x = input("enter x number: ")
Y = input("enter y number: ")

if x>Y:
  print("First number is the largest")
else:
  print("Second number is the largest")


################################## work third  it will print from one to 10 number
for i in range(1, 11):
    print(i)

########################
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

######################################
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
###############################################
n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))

##########################################################
X = [[1,7,3],
    [4 ,9,6],
    [3 ,6,9]]

Y = [[6,5,1],
    [2,7,3],
    [3,42,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)


