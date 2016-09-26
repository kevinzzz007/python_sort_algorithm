A = [5,7,3,2,4,9]


class Solution:
	size = 0
	largest = 0
	
	def sort(self, A):
		self.merge_sort(A, 0, len(A) - 1, [0 for x in range(0, len(A))])
		return A
	
	def merge_sort(self, A, start, end, tmp):
		if start >= end:
			return
		
		mid = start + (end - start) / 2
		self.merge_sort(A, start, mid, tmp)
		self.merge_sort(A, mid + 1, end, tmp)
		self.merge(A, start, mid, end, tmp)
		return
	
	def merge(self, A, start, mid, end, tmp):
		left = start
		right = mid + 1
		index = start
	
		while left <= mid and right <= end:
			if A[left] < A[right]:
				tmp[index] = A[left]
				left += 1
				index += 1
			else:
				tmp[index] = A[right]
				right += 1
				index += 1
		
		if left <= mid:
			for i in range(left, mid + 1):
				tmp[index] = A[i]
				index += 1
		
		if right <= end:
			for i in range(right, end + 1):

				tmp[index] = A[i]
				index += 1
		
		for i in range(start, end + 1):
			A[i] = tmp[i]
		
		

s = Solution()
print(s.sort(A))
