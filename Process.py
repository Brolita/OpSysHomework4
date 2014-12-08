class Process:
	def __init__(self, _id, _frames, _eventTimes ):
		self.id = _id
		self.frames = int(_frames)
		
		self.arrivalTimes = []
		self.exitTimes = []
		
		#parse _eventTimes into arrival and exitTimes
		i=0
		for time in _eventTimes:
			if i%2 == 0:
				self.arrivalTimes.append(int(time))
			else:
				self.exitTimes.append(int(time))
			i+= 1
		
		
	