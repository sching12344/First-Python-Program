class Item:
	def __init__(self, name, short, skill_bonus, will_bonus):
		"""Assigns the given arguments to create the item's name, short name, skill bonus and will bonus. skill_bonus and will_bonus are arguments passed as integers
		from the main file."""
		self.name = name
		self.short = short
		self.skill_bonus = skill_bonus
		self.will_bonus = will_bonus

	def get_name(self):
		"""Returns an item's name."""
		return self.name

	def get_short(self):
		"""Returns an item's short name."""
		return self.short

	def get_info(self):
		"""Prints information about the item."""
		print(self.name)
		print("Grants a bonus of {} to SKILL.\nGrants a bonus of {} to WILL.\n".format(self.skill_bonus, self.will_bonus))
		return

	def get_skill(self):
		"""Returns the item's skill bonus."""
		return self.skill_bonus

	def get_will(self):
		"""Returns the item's will bonus."""
		return self.will_bonus
