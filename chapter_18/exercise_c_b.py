class matrix :
    size=3;
    def __init__(self,r,c):
        self.rows=r
        self.cols=c
        self.arr=[]
    def initilizematrix(self):
        print('Enter the contents of matrix row-wise ::')
        for i in range(self.rows):
            print('row',i,':')
            a=[]
            for j in range(self.cols):
                a.append(int(input()))
            print('row ',i,' is completed')
            self.arr.append(a)
        print('Matrix initilized successfully')

    def displaymatrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.arr[i][j],end='  ')
            print()
    def add(self,m):
        mat=matrix(self.rows,self.cols)
        for i in range(self.rows):
            lst=[]
            for j in range(self.cols):
                lst.append(self.arr[i][j]+m.arr[i][j])
            mat.arr.append(lst)
        return mat

    def multiply(self, m):
        mat = matrix(self.rows, self.cols)
        for i in range(self.rows):
            lst = []
            for j in range(self.cols):
                temp=0
                for k in range(self.cols): # why because what if a=3x3 amd b=3X5
                    temp=temp+self.arr[i][k]*self.arr[k][j]
                lst.append(temp)
            mat.arr.append(lst)
        return mat

    def transpose(self):
        mat=matrix(self.cols,self.rows)
        for i in range(self.cols):
            lst=[]
            for j in range(self.rows):
                lst.append(self.arr[j][i])
            mat.arr.append(lst)
        return mat

print('initilize matrix 1 : ')
mat1 = matrix(3, 3)
mat1.initilizematrix()

print('initilize matrix 2 : ')
mat2 = matrix(3, 3)
mat2.initilizematrix()

print('First matrix')
mat1.displaymatrix()

print('second matrix')
mat2.displaymatrix()

mat3 = mat1.add(mat2)
print('after addition')
mat3.displaymatrix()

mat4 = mat1.multiply(mat2)
print('after multiplication')
mat4.displaymatrix()

mat5 = mat1.transpose()
print('After transpose')
mat5.displaymatrix()

