from enum import Enum
class Mode(Enum):
    first = 0
    best = 1
    next = 2
	worst = 3
	noncontig = 4

class FragmentationError(Exception):
	def __str__(self):
		return "Fragmentation error in main memory"
	
class Memory:
	def __init__(self, mode):
		self._value = ''
		for i in xrange(1600):
			if i < 80:
				self._value += '#'
			else
				self._value += '.'
		self.mode = mode
		self.seeker = 80
		self.end = 1600
		self.isDefragmented = True
		
	def __str__(self):
		rv = ''
		for i in xrange(self.end / 80):
			rv += self._value[80*i : 80*i + 79] + '\n'
		return rv
		
	def insert(self, pid, mem):
		'''
		FIRST AVAILIBLE SPACE
		'''
		if self.mode is Mode.first:
			# check if theres enough memory in the front
			if self.end - self.seeker >= mem:
				for i in range(mem):
					self._value[self.seeker] = pid
					self.seeker++;
			else: 
				self.defragment()
				self.insert(pid, mem)
				
		if self.mode is Mode.best:
			# find all the spaces and find the lowest
			
			open = (-1,self.end)
			hit = self.hit()
			hit.insert(0,0)
			for i in xrange(len(hit) / 2):
				if hit[2*i+1] - hit[2*i] > mem and hit[2*i+1] - hit[2*i] < open[1]:
					open = hit[2*i], hit[2*i+1] - hit[2*i]
				
			if open[0] < 0:
				self.defragment()
				self.insert(pid, mem)
			
			else:
				self.seeker = open[0]
				for i in range(mem):
					self._value[self.seeker] = pid
					self.seeker++;
	
	def remove(self, pid):
		if self.mode is not Mode.noncontig:
			for i xrange(self.end):
				if self._value[i] == pid:
					self.value[i] = '.'
		
	def hit(self):
		hit = [];
		open = True
		for seek in xrange(self.end):
			if (self._value[seek] == '.') != open:
				# a switch on hitting blocks of memory
				hit.append(seek)
			
		hit.append(self.end)
		
		return hit
		
	def defragment(self):
		hit = self.hit()
		
		if len(hit) == 3:
			raise FragmentationError()
			
		seek = 0
		newvalue = ''
		
		for i in xrange(len(hit) / 2):
			newvalue += self._value[hit[2*i]:hit[2*i+1]]
			
		for i in xrange(self.end - len(newvalue)):
			newvalue += '.';
			
		self._value = newvalue
			