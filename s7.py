import datetime
import math

def print_vector(vector):
	for i in vector: print '%7.4f'%i,
	print
def eps():
	return 1e-3

def print_matrix(matrix):
	for i in xrange(len(matrix)):
		for j in xrange(len(matrix[i])):
			print "%7.4f" %(matrix[i][j]),
		print
	return

def get_max_element(matrix):
	max_el_i=0
	max_el_j=1
	max_el = matrix[max_el_i][max_el_j]
	for i in xrange(len(matrix)):
		for j in xrange(i+1,len(matrix[i])):
			if math.fabs(matrix[i][j])>math.fabs(max_el):
				max_el_i = i
				max_el_j = j
				max_el = matrix[max_el_i][max_el_j]
	answer = []
	answer.append(max_el)
	answer.append(max_el_i)
	answer.append(max_el_j)
	return (answer)
	
def calculate_angle(i,j,matrix):
	return 0.5 * math.atan(2*matrix[i][j]/(matrix[i][i]-matrix[j][j]))
	
def make_rotation_matrix(width,height,angle,i0,j0):
	matrix = []
	for i in xrange(height):
		matrix.append([])
		for j in xrange(width):
			matrix[i].append(0.0)
			if i==j: matrix[i][j]=1.0
	matrix[i0][i0]=math.cos(angle)
	matrix[i0][j0]=-math.sin(angle)
	matrix[j0][i0]=math.sin(angle)
	matrix[j0][j0]=math.cos(angle)
	return matrix
	
def make_tran_matrix(matrix):
	answer = []
	for i in xrange(len(matrix)):
		answer.append([])
		for j in xrange(len(matrix[i])):
			answer[i].append(matrix[j][i])
	return answer
	
def matrix_mult(m1,m2):
    s=0.0     #sum
    t=[]    #temp matrix
    m3=[]   #result matrix
    if len(m2)!=len(m1[0]):
        raise Exception('this matrix cant multiplicate')     
    else:
        r1=len(m1) 
        c1=len(m1[0]) 
        r2=c1           
        c2=len(m2[0])  
        for z in range(0,r1):
            for j in range(0,c2):
                for i in range(0,c1):
                   s=s+m1[z][i]*m2[i][j]
                t.append(s)
                s=0.0
            m3.append(t)
            t=[]           
    return m3
				
def is_null(matrix):
	for i in xrange(len(matrix)):
		for j in xrange(len(matrix[i])):
			if i==j : continue
			if math.fabs(matrix[i][j])>eps(): return False
	return True

def make_identity_matrix(height):
	answer = []
	for i in xrange(height):
		answer.append([])
		for j in xrange(height):
			answer[i].append(0.0)
			if i==j: answer[i][j]=1.0
	return answer

def main():
	print(10*'#'+'['+str(datetime.datetime.now())+']'+10*'#')
	input = open('input7.txt','r')
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
		
		#height and width
		height = len(matrix)
		width = len(matrix[0])
		
		rotation_matrix_log =[]#roatrion matrix store here
		
		i = make_identity_matrix(4)
		
		iter =0
		
		while(True):
			#print('iter'+str(iter))
			iter+=1
			ans = get_max_element(matrix) 
			#print('max el: ', str(ans)) #debug                                  #(1) finding of max element
			angle = calculate_angle(ans[1],ans[2],matrix)   
			#print('angle: '+str(angle))#debug                 #(3) calculate a angle
			rotation = make_rotation_matrix(width,height,angle,ans[1],ans[2])#(4) make a rotation matrix
			#print('rotation:')#debug
			#print_matrix(rotation)#debug
			rotation_matrix_log.append(rotation)                             #(5) put rotation matrix in memory
			rotation_t = make_tran_matrix(rotation)
			matrix = matrix_mult(rotation_t,matrix)                          #(6) calculate a new matrix
			matrix = matrix_mult(matrix,rotation) 
			#print('result:')#debug
			#print_matrix(matrix)#debug
			if is_null(matrix) : break                                       #(7)break if all elemenst except for in diag are zero
			if iter>100: break          
			#raw_input()                                     #alarm break
		print ('iter:' +str(iter))
		finish_rotation_matrix = make_identity_matrix(height)
		for element in rotation_matrix_log: 
			finish_rotation_matrix=matrix_mult(finish_rotation_matrix,element)
		
		#print('result matrix')
		#print_matrix(matrix)
		
		eigenvalues = [matrix[l][l] for l in xrange(height)]
		
		print('eigenvalues')
		print_vector(eigenvalues)
		
		print('eigenvector')
		print_matrix(finish_rotation_matrix)
	#end

if __name__=='__main__':
	main()