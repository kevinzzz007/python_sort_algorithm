A = [5,7,3,2,4,9]


class Solution:
	size = 0
	largest = 0
	
	def sort(self, A):
		self.radix_sort(A)
		return A
	
	def radix_sort(self, A):
		max_val = self.get_max(A)
		exp = 1
		while max_val/exp > 0:
			self.count_sort(A, exp)
			exp = exp * 10
		
		return A
	
	def count_sort(self, A, exp):
		output = [0 for x in range(0, len(A))]
		count = [0 for x in range(0, 10)]
		
		for i in range(0, len(A)):
			count[(A[i]/exp) % 10] += 1
		
		for i in range(1, 10):
			count[i] = count[i] + count[i - 1]
		
		for i in range(len(A) - 1, -1, -1):
			output[count[(A[i]/exp) % 10] - 1] = A[i]
			count[(A[i]/exp) % 10] -= 1
		
		for i in range(0, len(A)):
			A[i] = output[i]
	
	def get_max(self, A):
		ans = A[0]
		for i in range(1, len(A)):
			ans = max(ans, A[i])
		return ans
		
		

s = Solution()
print(s.sort(A))
