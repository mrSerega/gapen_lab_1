import math
import datetime
import copy

def eps():
	return 1e-5

def print_vector(vector):
	for i in vector: print '%7.4f'%i,
	print

def print_matrix(matrix):
	for line in matrix: print(line)

def is_first_column_zero(matrix):
	column = [matrix[i][0] for i in xrange(len(matrix))]
	mul = 1.0
	for i in column: mul*=i
	if mul == 0: return True
	return False 

def c(i,matrix):
	a = matrix[0][0]
	b = matrix[i+1][0]
	return a/math.sqrt(a**2+b**2)
	
def s(i,matrix):
	a = matrix[0][0]
	b = matrix[i+1][0]
	return b/math.sqrt(a**2+b**2)
	
def special_sum(matrix,k,answer):
	s = 0
	for i in xrange(k+1,len(matrix)):
		#print (matrix[k][i])
		#print (answer[i])
		s+=matrix[k][i]*answer[i]
	return s
		

def iter(i,matrix):
	#print("-----[iter:"+str(i)+"]-----")
	#if iter>100: return
	#print('matrix:')
	#for k in xrange(len(matrix)): print (matrix[k])
	
	#print ('i: '+str(i)+'|len: '+str(len(matrix)))
	if i >= len(matrix)-1:
		#print("result:")
		#for k in xrange(len(matrix)): print (matrix[k])
		return 
		
	sub_matrix = []
	
	#print ("matrix len: "+str(len(matrix)))
	for j in xrange(i,len(matrix)):
		sub_line = [matrix[j][l] for l in xrange(i,len(matrix[j]))]
		sub_matrix.append(sub_line)
	
	#print (is_first_column_zero(sub_matrix))
	if is_first_column_zero(sub_matrix):
		iter(i+1,matrix)
		return
		
	#print("sub matrix:")
	#print_matrix (sub_matrix)
	
	for m in xrange(1,len(sub_matrix)):
		_c=c(m-1,sub_matrix)
		_s=s(m-1,sub_matrix)
		#print ('c: '+str(_c))
		#print ('s: '+str(_s))
		for j in xrange(len(sub_matrix[0])):
			left1 = _c*sub_matrix[0][j]
			right1 = _s*sub_matrix[m][j]
			left2 = -_s*sub_matrix[0][j]
			right2 = _c*sub_matrix[m][j]
			#print ('left1: '+str(left1))
			#print ('left2: '+str(left2))
			#print ('right1: '+str(right1))
			#print ('right2: '+str(right2))
			up = left1+right1
			down = left2+right2
			if math.fabs(up)<eps(): up = 0.0;
			if math.fabs(down)<eps(): down = 0.0;
			sub_matrix[0][j]=up
			sub_matrix[m][j]=down
		#print('sub_matrix:')
		#print_matrix(sub_matrix)
	
	for j in xrange(i,len(matrix)):
		for l in xrange(i,len(matrix[j])):
			matrix[j][l]=sub_matrix[j-i][l-i]
			
	i+=1
	iter(i,matrix)
	return

def main():
	print(10*'#'+'['+str(datetime.datetime.now())+']'+10*'#')
	input = open('input.txt','r')
	number_of_examples = int(input.readline())
	for i in xrange(number_of_examples):
		a = int(input.readline())
		matrix = []
		for j in xrange(a):
			line_str = input.readline()
			line_int = [int(element) for element in line_str.rstrip().split(' ')]
			matrix.append(line_int)
		
		print ("matrix:")
		print_matrix(matrix)	
		iter(0,matrix)
		#print('end')
		answer = []
		for i in xrange(len(matrix)): answer.append([])
		for i in xrange(len(matrix)-1,-1,-1):
			answer[i]=(matrix[i][-1]-special_sum(matrix,i,answer))/matrix[i][i]
			if math.fabs(answer[i])<eps(): answer[i]=0.0
			#print special_sum(matrix,i,answer)
		print 'answer: ',
		print_vector(answer) 

if __name__ == '__main__':
	main()	