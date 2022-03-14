> Welcome to the better than PSE-Hamstergame hamstergame.
> Below you will find infos on how to initalize/setup a game, the game is then simulated 
> and rendern after, so the actual game is not calculated in realtime. This category includes 
> a list of all commands the hamster/game provide.
# Information on how to play the game
### Initialization
For building our own little hamstergame move in the src folder of the hamsterproject.
In there open a new python file(e.g called app.py) and use the following code to setup a game
```python
#! /usr/bin/python3

# Import the app handler class, AppBase will be used
# as parent for our App
import app_base

# AppBase suggest we call our class App, but you can name your class
# freely according to the python class naming conventions.
# App will be a child class of app_base.AppBase
# The hamster is inherited by the parent class and called *self._paule*
class App(app_base.AppBase):
	
	# The constructor will initialze the parent class, which requires the 
	# path to a territory file.
	# > for further information about territory files see structure informations
	def __init__(self):
		super().__init__(TERRITORY_PATH)
	
	#
	# Space for custom methods
	# e.g
	# 
	# def turnLeft() -> None:
	# 	for _ in range(3):
	# 		self._paule.turnRight()
	#
	
	# method that contains all moves the hamster should do	
	def _excecute_hamstergame(self):
		# to mimic the PSE convention for hamster names add the following line
		paule = self._paule
		
		# Here comes the whole hamster interaction...
		# e.g. 
		# while self._paule.frontIsClear():
		#		self._paule.move()
		#
		# Which moves the hamster in looking direction until it hits a wall.
		# When self._paule can replaced by just paule when the pse convention
		# from above is used, which results in the following code:
		# 
		# while paule.frontIsClear():
		#		paule.move()
		
		
# Init a new app, the constructor will then handle the calculation
# as well as the rendering
App()
```
To execute the game execute the follwoing command when still inside the src folder
when gameFile is called app.py
```console
./app.py
```
or else
```console
python3 app.py
```

### Hamster commands
- turnRight()
- - returns None
- - Changes the looking direction of the hamster by 90 degrees clockwise
- 
- move()
- - returns None
- - moves the hamster one tile in looking direction
- - raises FrontIsBlockedException() when the tile in front of the hamster is a wall
- 
- pickGrain()
- - returns None
- - picks a grain from the tile, the hamster is currently standing on
- - raises NoGrainAvailableException() when the tile contains no grains
- 
- putGrain()
- - returns None
- - puts a grain on the tile, the hamster is currently standing on
- - raises NoGrainAvailableException() when the hamster has no grains
- - raises GrainPileFullException() when the tile already contains 9 grains
- 
- teleport()
- - returns None
- - moves the hamster from the portal, the hamster is currently standing on
- - to the other portal available
- - raises PortalClosedException() when hamster is not on tile containing a portal
- 
- frontIsClear()
- - returns bool
- - True when the tile in front f the hamster is NOT a wall
- 
- hasGrain()
- - returns bool
- - True when the hamster has 1 or more grains
- 
- grainAvailable()
- - returns bool
- - True when the tile, the hamster is currently standing on contains 1 or more grains
-  
- grainPileIsFull()
- - returns bool
- - True when the tile, the hamster is currently standing on contains 9 grains
-  
- portalIsOpen()
- - returns bool
- - True when the tile, the hamster is currently standing on is a portal
-  
- write(message: str)
- - returns None
- - prints "[Hamster] - *message*" to the console

# Information all about the game itself

# Information all about the code and structure


