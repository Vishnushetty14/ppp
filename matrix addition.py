x=[[2,3,4],
  [4,5,6],
  [7,8,9]]
y=[[2,3,4],
  [4,5,6],
  [7,8,9]]
v=[[0,0,0],
  [0,0,0],
  [0,0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        v[i][j]=x[i][j]+y[i][j]
for i in v:
 print(i) 

