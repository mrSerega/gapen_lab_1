import numpy as np
 
def qr(A):
    m, n = A.shape#make a matrixs
    Q = np.eye(m)#make a identity matrix
    for i in range(n - (m == n)):
        H = np.eye(m)
        H[i:, i:] = make_householder(A[i:, i])
        Q = np.dot(Q, H)
        A = np.dot(H, A)
    return Q, A
 
def make_householder(a):
    v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    H = np.eye(a.shape[0])
    H -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
    return H

def main():
	input = open('input.txt','r')
	number_of_examples = int(input.readline())#examples number reading
	for i in xrange(number_of_examples):
		a = int(input.readline())#matrix height reading
		matrix = []
		for j in xrange(a):#matrix reading
			line_str = input.readline()
			line_int = [float(element) for element in line_str.rstrip().split(' ')]
			matrix.append(line_int)	
		#enter code here
		arr = []
		tmp_b =[]
		for i in xrange(len(matrix)): 
			arr.append(matrix[i][0:-1])
			tmp_b.append(matrix[i][-1])
		#################
		a = np.array(arr)
		b = np.matrix(tmp_b)
		
		print('a')
		print(a.round(4))
		print('b:')
		print(b.round(4))
		
		q, r = qr(a)
		#print('q:')
		#print(q.round(4))
		#print('r:')
		#print(r.round(4))
		y = np.matrix(q)
		y.I
		y=b*y
		#print('y')
		#print(y.round(4))
		r=np.matrix(r)
		r=r.I
		x = r*y.T
		print('answer:')
		print(x.round(4))

if __name__ == '__main__':
	main()