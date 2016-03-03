# A class definition for matrices

import numpy as np

class MyMatrix:
	
	""" A class definition for matrices. The problem didn't really specify what 
		which floats to put in it, so I just have the matrix counting upwards."""
		
	""" Looking back now that the thing is done, it probably would've been better if
		I had just given MyMatrix a list of lists and it had turned it into a matrix.
		This would avoid all the weirdness with adding or multiplying two "MyMatrices" 
		and getting back an array."""

	# def __init__(self, m, n):
		# tot = range(m*n)
		# rows = [[float(tot[x+j*n]) for x in range(n)] for j in range(m)]
		# self.matrix = np.array(rows)
		# self.m = m
		# self.n = n
		
	def __init__(self, A):
		""" I decided to fix it"""
	
		self.m, self.n = np.array(A).shape
		flt_A = [[float(A[i][j]) for j in range(self.n)] for i in range(self.m)]
		self.matrix = np.array(flt_A)

		
		
	def __add__(self, other):
		""" Addition works as one would expect. Includes a gentle reminder for fools
			that don't know how to add matrices."""
			
		""" Also this one's and multiplication are a bit weird because you give it
			something that belongs to MyMatrix and it gives you back an array"""
			
		try:
			self.sum = self.matrix + other.matrix
			return MyMatrix(self.sum)
		except ValueError:
			print 'Matrices must have the same dimensions to be added'
	
	
	def __mul__(self,other):
		""" Written according to the definition of matrix multiplication. 
			I could have used list comprehension but I was intimidated.
			Also, I'm willing to bet my left nut that there's a function
			already in numpy that totally would've done the job."""
			
		m = self.m
		n = self.n
		hopefully_also_n = other.m
		l = other.n
		
		if n == hopefully_also_n:
			prod = []
			for i in range(m):
				row = []
				for j in range(l):
					terms = []
					for k in range(n):
						terms.append(self.matrix[i][k]*other.matrix[k][j])
					sum = np.sum(terms)
					row.append(sum)
				prod.append(row)
				
			self.product = prod
			return MyMatrix(self.product)
		else:
			print "Inner dimensions of matrices being multiplied must match"
			
	def pinv(self):
		""" Pseudo inverse. Instead of writing this one myself I relied on numpy."""
		
		self.pinv = np.linalg.pinv(self.matrix)
		return MyMatrix(self.pinv)
	
	def __repr__(self):
		s = str(self.matrix)
		return s
