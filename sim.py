import datetime
import math

def print_vector(vector):
	for i in vector: print '%7.4f'%i,
	print

def make_good_matrix(bad_matrix):#no return
	for i in xrange(len(bad_matrix)):
		if bad_matrix[i][i]==0:
			continue
		for j in xrange(len(bad_matrix[i])):
			if i!=j:
				bad_matrix[i][j]/=(bad_matrix[i][i]+0.0)
		bad_matrix[i][i]=0.0
							
def print_matrix(matrix):
	for i in xrange(len(matrix)):
		for j in xrange(len(matrix[i])):
			print "%7.4f" %(matrix[i][j]),
		print
	return
	
def eps():
    return 1e-5
	
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
	input = open('inputsim.txt','r')
	number_of_examples = int(input.readline())
	for i in xrange(number_of_examples):
		a = int(input.readline())
		matrix = []
		for j in xrange(a):
			line_str = input.readline()
			line_int = [float(element) for element in line_str.rstrip().split(' ')]
			matrix.append(line_int)
		
		print ("matrix:")
		print_matrix(matrix)
		make_good_matrix(matrix)
		#print ('good matrix:')
		#print_matrix(matrix)	
		
		b = [i[-1] for i in matrix]
		answer = [0 for i in xrange(len(matrix))]

		for i in xrange(len(matrix)):
			matrix[i]=matrix[i][0:-1]
		iter =0
		while(True):
			current_answer = matrix_on_vec(matrix,answer)
			current_answer = vec_minus_vec(b,current_answer)
			delta = [math.fabs(current_answer[i]-answer[i]) for i in xrange(len(answer))]
			delta = max(delta)
			answer = current_answer[:]
			#print_vector(answer)
			#raw_input()
			if delta < eps(): break
			iter+=1
			if iter>100:
				#print('alarm break')
				break
		print 'answer: ',
		print_vector(answer)

if __name__ == '__main__':
	main()