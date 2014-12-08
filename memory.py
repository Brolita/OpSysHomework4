#from enum import Enum
class Mode():
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
			else:
				self._value += '.'
		self.mode = mode
		self.seeker = 80
		self.end = 1600
		
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
					self.seeker+=1
			else: 
				self.defragment()
				self.insert(pid, mem)
		
		'''
		BEST AVAILIBLE SPACE
		'''
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
					self.seeker+=1
		
		'''
		NEXT AVAILIBLE SPACE
		'''		
		if self.mode is Mode.next:
			# find the next big enough memory space
			
			hit = self.hit()
			hit.insert(0,0)
			for i in xrange(len(hit) / 2):
				if hit[2*i+1] - hit[2*i] > mem:
					self.seeker = hit[2*i + 1]
					for i in range(mem):
						self._value[self.seeker] = pid
						self.seeker+=1
					return
			
			self.defragment()
			self.insert(pid, mem)		
		
		'''
		WORST AVAILIBLE SPACE
		'''
		if self.mode is Mode.best:
			# find all the spaces and find the lowest
			
			open = (-1,self.end)
			hit = self.hit()
			hit.insert(0,0)
			for i in xrange(len(hit) / 2):
				if hit[2*i+1] - hit[2*i] > mem and hit[2*i+1] - hit[2*i] > open[1]:
					open = hit[2*i], hit[2*i+1] - hit[2*i]
				
			if open[0] < 0:
				self.defragment()
				self.insert(pid, mem)
			
			else:
				self.seeker = open[0]
				for i in range(mem):
					self._value[self.seeker] = pid
					self.seeker+=1
		
		'''
		NONCONTIGUOUS 
		'''
		
		if self.mode is Mode.noncontig:
			# start insertion at next availible place
			
			i = 0
			while mem > 0:
				if self._value[i] == '.':
					self._value[i] = pid
					mem -= 1
				i += 1
				if i == 1600:
					break
					
			if mem != 0:
				self.remove(pid)
				raise FragmentationError()
	
	def remove(self, pid):
		for i in xrange(self.end):
			if self._value[i] == pid:
				self.value[i] = '.'
		
	def hit(self):
		hit = [];
		open = True
		for seek in xrange(self.end):
			if (self._value[seek] == '.') != open:
				# a switch on hitting blocks of memory
				open = not open
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
			