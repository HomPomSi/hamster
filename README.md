 Welcome to the better than PSE-Hamstergame hamstergame.
 Below you will find informations on how to initalize/setup a game, the game is 
 then simulated and rendered after, so the actual game is not calculated in realtime. 
 This README includes a list of all commands the hamster/game provide.
 As well as how the format .ter files for wasy territory distribution. Territorys should be 
 parsed from a .ter file and not be built manually, still possible tho...
# Information on how to play the game
## Initialization
For building our own little hamstergame move in the src folder of the hamsterproject.
In there open a new python file(e.g called app.py) and use the following code to setup a game
```python
#! /usr/bin/python3

# Import the app handler class, AppBase will be used
# as parent for our App
import app_base

# For building our own territories import the following, you can alternativly 
# use a .ter file, which results in cleaner code and easy distribution, easy 
# changes as well as super readable territories.
# custom territories allow for the usage of more than one portal
import territory.territory

# When its neccessary to overwrite the default hamster also omport the following
import hamster.hamster
import datatypes.location

# AppBase suggest we call our class App, but you can name your class
# freely according to the python class naming conventions.
# App will be a child class of app_base.AppBase
# The hamster is inherited by the parent class and called *self._paule*
# Paule is by default initialized at 1|1. When using a custom territory 
# make sure to leave this tile free or overwrite self._paule by creating
# your own hamster.
class App(app_base.AppBase):
	
	# The constructor will initialze the parent class, which requires the 
	# path to a territory file or a territory object
	# > for further information about territory files see structure informations
	def __init__(self):
		#
		# When you want to build your own territory do 
		# that here(but please do not do that)
		#
		super().__init__(TERRITORY_PATH or TERRITORY_OBJECT)
		
		# When neccesarry overwrite the inherited hamster by doing the following
		location = datatypes.location.Location(NEW_ROW, NEW_COLUMN)
		self._paule = hamster.hamster.Hamster(self._game, location)
		
	#
	# Space for custom methods
	# e.g
	# 
	# def turnLeft() -> None:
	# 	for _ in range(3):
	# 		self._paule.turnRight()
	#
	
	# method that contains all moves the hamster should do	
	# raises NotImplementedError() when kept empty
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
To execute the game execute the following command when still inside the src folder
when gameFile is called app.py
```console
./app.py
```
or else
```console
python3 app.py
```
<br> 

### Building a territory from scratch
```python
# Import the territory class 
import territory.territory

# Start by initializing a new territory object, the constructor takes
# two arguments, the size and an OPTIONAL description
# The Size constructor takes a width and a hight.
size = Size(5, 7)
description = "I am a territory made from scratch"
ter = territory.territory.Territory(size, description)

# Now that we have an empty territory of a custom size we  can start
# adding stuff...
# To place a wall use wallAt() which takes a location as argument
# The Location constructor takes a row_index and a column_index
location = Location(0, 0)
ter.wallAt(location)

# To add grains use putGrain() which will put a single grain at
# a specific location
location = (1, 0)
ter.putGrain(location)

# To remove grains use pickGrain() which will remove a single grain
# at a specific location
location = Location(1, 0)
ter.pickGrain(location)

# A territory can contain gateways, made of a source_portal and
# a destination_portal
# To add a new gateway use setPortal which takes a location for 
# the source_portal and a location for the destination_portal
source = Location(2, 0)
destination = Location(1, 3)
ter.setPortal(source, destination)
```
## Hamster commands	
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

### Some example methods 
```python 
def turnLeft():
	for _ in range(3):
		self._paule.turnRight()

def moveNSteps(n: int):
	for n in range(n):
		self._paule.move()

def moveTillBlocked():
	while self._paule.frontIsClear():
		self._paule.move()

def pickAllGrains():
	while self._paule.grainAvailable():
		self._paule.pickGrain()
```

# Information all about the game itself

# Information all about the code and structure
### Project structure
```
| Hamster
+ - +
|   | README.md
|   | src
|   + - +
|   |   | app_example.py
|   |   | app_base.py
|   |   | __init__.py
|   |   | datatypes
|   |   + - +
|   |   |   | direction.py
|   |   |   | location.py
|   |   |   | size.py
|   |   |   | tile_types.py
|   |   |   | __init__.py
|   |   |
|   |   | exceptions
|   |   + - +
|   |   |   | blocked_exception.py
|   |   |   | max_steps_exception.py
|   |   |   | parser_exception.py
|   |   |   | territory_exception.py
|   |   |   | __init__.py
|   |   |
|   |   | hamster
|   |   + - +
|   |   |   | hamster.py
|   |   |   | __init__.py
|   |   |
|   |   | hamstergame
|   |   + - +
|   |   |   | hamstergame.py
|   |   |   | render_map.py
|   |   |   | __init__.py
|   |   |
|   |   | territory
|   |   + - +
|   |   |   | grain_pile.py
|   |   |   | parser.py
|   |   |   | portal.py
|   |   |   | territory.py
|   |   |   | tile.py
|   |   |   | wall.py
|   |   |   | __init__.py
|   |   |
|   |   | test
|   |   + - +
|   |   |   | verify_territories.py
|   |   |   | __init__.py
|   |
|   | resources
|   + - +
|   |   | territories
|   |   + - +
|   |   |   | blank-8x8.ter
|   |   |   | broke-1x1.ter
|   |   |   | circle-12x12.ter
|   |   |   | max-grain-8x8.ter
|   |   |   | portal-5x5.ter
|   |   |   
|   |   | images
|   |   + - +
|   |   |   | grain0.png
|   |   |   | grain1.png
|   |   |   | grain2.png
|   |   |   | grain3.png
|   |   |   | grain4.png
|   |   |   | grain5.png
|   |   |   | grain6.png
|   |   |   | grain7.png
|   |   |   | grain8.png
|   |   |   | grain9.png
|   |   |   | hamster.png
|   |   |   | portal.png
|   |   |   | tile_base.png
|   |   |   | wall.png
|   |   |   | xfc
|   |   |   + - +
|   |   |   |   | grain1.xfc
|   |   |   |   | grain2.xfc
|   |   |   |   | grain3.xfc
|   |   |   |   | grain4.xfc
|   |   |   |   | grain5.xfc
|   |   |   |   | grain6.xfc
|   |   |   |   | grain7.xfc
|   |   |   |   | grain8.xfc
|   |   |   |   | grain9.xfc
|   |   |   |   | hamster_backup.xfc
|   |   |   |   | hamster.xfc
|   |   |   |   | portal.xfc
|   |   |   |   | tile_base.xfc
|   |   |   |   | wall.xfc
```

