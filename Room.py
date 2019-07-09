class Room:
	def __init__(self, name):
		"""Constructor for the Room class. It is passed a single argument name that is assigned as an attribute self.name.
		self.exits and self.directions are dictionaries where one maps given directions to destinations (room objects) and the other maps directions given
		by user input into lower case directions (e.g. North:north) respectively."""
		self.name = name
		self.exits = {}
		self.directions = {} 
		self.quest = None

	def get_exits(self):
		"""Returns a dictionary called self.exits"""
		return self.exits
		
	def get_name(self):
		"""Returns the room's name."""
		return self.name

	def get_short_desc(self):
		"""Returns a short description of the room. The description of this room will depend upon the quest attribute assigned to the room instance. This
		changes depending on whether the quest is none, complete or incomplete."""
		if self.quest == None:
			 return "There is nothing in this room."
		else:
			return self.quest.get_room_desc()

	def get_quest_action(self):
		"""If a quest can be completed in this room, returns a command that the user can input to attempt the quest."""
		return self.quest.get_action()

	def get_quest(self):
		"""Returns a Quest object that can be completed in this room."""
		return self.quest
		
	def set_path(self, dir, dest):
		"""Received argument dir (direction) as a string and dest (destination) as an adjoining room object. This method adds these values to the dictionaries
		created within the constructor"""
		dir = dir.lower()
		self.exits[dir] = dest
		self.exits[dir[0]] = dest
		self.directions[dir[0]] = dir
		self.directions[dir] = dir
	
	def draw(self):
		"""Creates a drawing depicting the exits in each room."""
		directions = ["north", "south", "east", "west"]

		#Creates a list for top, bottom and side walls
		top_wall = ["+"] + (["-"] * 20) + ["+\n"]
		bottom_wall = ["+"] + (["-"] * 20) + ["+"]
		walls = (["|"] + ([" "] * 20) + ["|\n"]) * 9

		#If there are exits for the current room, recreate walls appropriately
		for exit in range(len(directions)):
			if directions[exit] in self.exits and directions[exit] == "north":
				top_wall = top_wall[:10] + ["NN"] + top_wall[12:]

			elif directions[exit] in self.exits and directions[exit] == "south":
				bottom_wall = bottom_wall[:10] + ["SS"] + bottom_wall[12:]

			elif directions[exit] in self.exits and directions[exit] == "east":
				walls = walls[:109] + ["E\n"] + walls[110:]

			elif directions[exit] in self.exits and directions[exit] == "west":
				walls = walls[:88] + ["W"] + walls[89:]

		#Join the lists together as strings and out the room and its description.
		walls = "".join(walls)
		top_wall = "".join(top_wall)
		bottom_wall = "".join(bottom_wall)
		print("\n{}{}{}".format(top_wall, walls, bottom_wall))
		print("You are standing at the {}.".format(self.get_name()))
		print("{}".format(self.get_short_desc()))
		return

	def move(self, dir):
		"""Returns an adjoining Room object based on a direction given. (i.e. if dir == "NORTH", returns a Room object in the north)."""
		return self.directions[dir].lower(), self.exits[dir]
