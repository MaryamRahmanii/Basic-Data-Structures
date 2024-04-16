import numpy as np

class SparseMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows, self.cols = matrix.shape
        self.data=["V"]
        self.row=["R"]
        self.col=["C"]

        for i in range(self.rows):
            for j in range(self.cols):
                if matrix[i,j] !=0:
                    self.row.append(i)
                    self.col.append(j)
                    self.data.append(self.matrix[i, j])








rows=int(input("Enter number of rows:"))
cols=int(input("Enter number of columns:"))
matrixelement=[]
for i in range(rows):

    row=list(map(int, input("enter row:").split()))
    matrixelement.append(row)

input_matrix=np.array(matrixelement)

sparse=SparseMatrix(input_matrix)

for a,b,c in zip(sparse.row, sparse.col, sparse.data):
    print(a,b,c)