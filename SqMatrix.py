from MyMatrix import MyMatrix

import numpy as np

class SqMatrix(MyMatrix):
	
	def __init__(self, A):
		MyMatrix.__init__(self, A)
		
		if self.m != self.n:
			raise ValueError, "YOUR MATRIX IS NOT SQUARE, DINGDONG"
		else:
			None
	
	def inv(self):
		self.inv = np.linalg.inv(self.matrix)
		return self.inv
		
	def eig(self):
		self.eig = np.linalg.eig(self.matrix)
		return self.eig
