class Quest:
	def __init__(self, reward, action, desc, before, after, req, fail_msg, pass_msg, room):
		"""Constructor creates the attributes for the arguments entered when initiating an instance of this class. Reward is an item object that has been previously initialised.
		Action, description, before, after, req, fail_msg, pass_msg and room are all string types. Req is a requirement for a quest that can be split into either skill or will
		and the respective level required by the player in order to succeed when attempting to complete the quest. self.complete is a static attribute that begins
		with the value False when a quest is initialised and changes depending on whether the character completes it."""
		self.reward = reward.lower()
		self.action = action.lower()
		self.desc = desc
		self.before = before
		self.after = after

		quest_requirement = req.split(" ")
		#Test the req argument and assign it to a Quest attribute.
		if (quest_requirement[0] == "SKILL") or (quest_requirement[0] == "WILL") and len(quest_requirement) == 2:
			try:
				self.char_req = quest_requirement[0]
				self.char_lvl = int(quest_requirement[1])
			except ValueError:
				print("Please specify a valid configuration file")
				sys.exit()
		else:
			raise FileNotFoundError

		self.fail_msg = fail_msg
		self.pass_msg = pass_msg
		self.room = room
		self.complete = False

	def check_room(self, rooms):
		#rooms is a list of room objects that have been previously entered in through a file.
		whether_valid = False
		for room in range(len(rooms)):
			if rooms[room].name == self.room:
				whether_valid = True
				self.room = rooms[room]

		if whether_valid == False:
			print("Please specify a valid configuration file.")
			quit()
		

	def check_reward(self, items):
		"""Assigns an item object as a reward for the appropriate quest instance"""
		whether_valid = False
		quest_reward = None
		for item in range(len(items)):
			if items[item].name.lower() == self.reward:
				whether_valid = True
				self.reward = items[item]

		if whether_valid == False:
			raise FileNotFoundError

	def get_info(self):
		#Returns the quest's description.
		return self.desc

	def is_complete(self):
		#Returns whether or not the quest is complete.
		return self.complete

	def get_action(self):
		"""Returns a command that the user can input to attempt the quest."""
		return self.action

	def get_room_desc(self):
		"""Returns a description for the room that the quest is currently in. Note that this is different depending on whether or not the quest has been completed."""
		if self.complete == False:
			return self.before
		else:
			return self.after
		

	def attempt(self, player):
		"""Allows the player to attempt this quest. Checks the cumulative skill or will power of the player and all their items. 
		If this value is larger than the required skill or will threshold for this quest's completion, they succeed and are rewarded with the reward item. 
		The description of the room also changes depending on whether the quest is completed. Otherwise, nothing happens."""
		character_skill = player.get_skill()
		character_will = player.get_will()

		if self.char_req == "SKILL":
			if character_skill >= self.char_lvl:
				print(self.pass_msg)
				player.take(self.reward)
				self.complete = True
			else:
				print(self.fail_msg)

		elif self.char_req == "WILL":
			if character_will >= self.char_lvl:
				print(self.pass_msg)
				player.take(self.reward)
				self.complete = True
			else:
				print(self.fail_msg)