# Main
# YOUR NAME
# The start of your overall agent program.
# Demonstrate the use of your SimpleReflexVacuum and your ModelReflexVacuum.
# The code for using a SimpleReflexVacuum is provided for you.


# Part 1
print("Part 1")
from simple_reflex_vacuum import SimpleReflexVacuum

simple_reflex_vacuum = SimpleReflexVacuum()
action = simple_reflex_vacuum.action('A', 'Dirt')
action()

action = simple_reflex_vacuum.action('A', None)
action()

action = simple_reflex_vacuum.action('B', None)
action()

action = simple_reflex_vacuum.action('B', 'Dirt')
action()

# Part 2
print("\nPart 2")
from model_reflex_vacuum import ModelReflexVacuum

from location import Location
from state import State
from movement_model import MovementModel
from transition_model import TransitionModel
from sensor_model import SensorModel
from model_reflex_vacuum import ModelReflexVacuum

vacuum_world = State({'A': Location('A', True), 'B': Location('B', True)}, 'A')
print(vacuum_world.current_location())

movements = {'A': MovementModel('A', 'B'),
             'B': MovementModel('A', 'B')}

transition_model = TransitionModel(vacuum_world, movements)

sensor_model = SensorModel(vacuum_world)

vacuum = ModelReflexVacuum(vacuum_world, transition_model, sensor_model)
print(vacuum.action()) # suck
print(vacuum.action()) # move right
print(vacuum.action()) # suck
print(vacuum.action()) # move left
print(vacuum.action()) # move right
