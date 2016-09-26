A = [5,7,3,2,4,9]


class Solution:
	size = 0
	largest = 0
	
	def sort(self, A):
		self.size = len(A)
		self.build_heap(A)
		for i in range(len(A) - 1, -1, -1):
			self.swap(A, i, 0)
			self.size -= 1
			self.heapify(A, 0)
		return A
		
	
	def build_heap(self, A):
		for i in range(self.size / 2, -1, -1):
			self.heapify(A, i)
	
	def heapify(self, A, index):
		left = 2 * index + 1
		right = 2 * index + 2
		if left < self.size and A[left] > A[index]:
			self.largest = left 
		else:
			self.largest = index
		
		if right < self.size and A[right] > A[self.largest]:
			self.largest = right
		if self.largest != index:
			self.swap(A, self.largest, index)
			self.heapify(A, self.largest)
	
	def swap(self, A, left, right):
		tmp = A[left]
		A[left] = A[right]
		A[right] = tmp
		
		

s = Solution()
print(s.sort(A))
