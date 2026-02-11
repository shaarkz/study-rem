class State:
	def __init__(self, enabled, channel_id):
		self.enabled = enabled
		self.channel_id = channel_id
		
		self.study_time = None
		self.duration_time = None
				
		self.schedule = {}
