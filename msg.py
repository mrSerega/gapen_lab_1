import datetime
import math

def norm(vec):
	answer = 0
	for i in vec:
		answer += i**2
	answer = math.sqrt(answer)
	return answer
	
def num_on_vec(num,vec):
	answer = [el*num for el in vec]
	return answer

def get_sc(vec1,vec2):
	if len(vec1)!=len(vec2):
		raise Exception('diff len of vec')
	s = 0
	for i in xrange(len(vec1)): s+=vec1[i]*vec2[i]
	return s

def print_vector(vector):
	for i in vector: print '%7.4f'%i,
	print

def print_matrix(matrix):
	for i in xrange(len(matrix)):
		for j in xrange(len(matrix[i])):
			print "%7.4f" %(matrix[i][j]),
		print

def eps():
    return 1e-3
    
def matrix_on_vec(matrix,vec):
	answer = []
	for i in xrange(len(vec)):
		answer.append(0.0)
		for j in xrange(len(vec)):
			answer[i]+=matrix[i][j]*vec[j]
	return answer
    
def vec_plus_vec(vec1,vec2):
	answer = []
	for i in xrange(len(vec1)):
		answer.append(vec1[i]+vec2[i])
	return answer
    
def vec_minus_vec(vec1,vec2):
	answer = []
	for i in xrange(len(vec1)):
		answer.append(vec1[i]-vec2[i])
	return answer

def main():
	print(10*'#'+'['+str(datetime.datetime.now())+']'+10*'#')
	input = open('inputmsg.txt','r')
	number_of_examples = int(input.readline())#examples number reading
	for i in xrange(number_of_examples):
		a = int(input.readline())#matrix height reading
		matrix = []
		for j in xrange(a):#matrix reading
			line_str = input.readline()
			line_int = [float(element) for element in line_str.rstrip().split(' ')]
			matrix.append(line_int)	
		#enter code here
		print ("matrix:")
		print_matrix(matrix)
		#0
		b = [line[-1] for line in matrix]
		A = []
		for l in xrange(len(matrix)):
			A.append(matrix[l][0:-1])
		#1.1
		x = [] 
		for l in xrange(len(matrix)): x.append(0.0)
		#1.2
		e = matrix_on_vec(A,x)
		e = vec_minus_vec(b,e)
		#1.3
		p=e[:]
		
		while(True):
			#2.1
			q=matrix_on_vec(A,p)
			#2.2
			a=get_sc(e,p)/get_sc(q,p)
			#2.3
			x = vec_plus_vec(x,num_on_vec(a,p))
			#2.4
			e = vec_minus_vec(e,num_on_vec(a,q))
			#2.5
			if norm(e)<eps(): break
			#3.1
			b_sc = get_sc(e,q)/get_sc(p,q)
			#3.2
			p = vec_minus_vec(e,num_on_vec(b_sc,p))
		print 'answer: ',
		print_vector(x)
		
if __name__=='__main__':
	main()