
r=int(input("enter the row of first matrix"))
c=int(input("enter the colum of first matrix"))
a=[]

for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input()))
    a.append(row)
print("yr first matrix")
for i in range(r):
  for j in range(c):
    print(a[i][j],end=" ")
  print()
r1=int(input("enter the row of second matrix"))
c1=int(input("enter the colum of second matrix"))
b=[]

for i in range(r1):
    row=[]
    for i in range(c1):
        row.append(int(input()))
    b.append(row)
print("yr second matrix")
for i in range(r1):
  for j in range(c1):
    print(b[i][j],end=" ")
  print()
print("the sum of matrix")
k=[]
for i in range(r):
    row=[]
    for j in range(c):
        row.append(a[i][j]+b[i][j])
    k.append(row)
for i in range(r):
  for j in range(c):
    print(k[i][j],end=" ")
  print()