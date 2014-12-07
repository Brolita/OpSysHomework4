class Process:
	def __init__(self, _id, _frames, _eventTimes ):
		self.id = id
		self.frames = _frames
		
		self.arrivalTimes = []
		self.exitTimes = []
		
		#parse _eventTimes into arrival and exitTimes
		i=0
		for int in _eventTimes:
			if i%2 = 0:
				arrivalTimes.append(int)
			else:
				exitTimes.append(int)
			i+= 1
		
		
	