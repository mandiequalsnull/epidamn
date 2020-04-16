from PySimpleGUI import Slider, Window, Image, Button, Text, Column
import os
from untitled2 import foo
import random
from decimal import Decimal


img = Image('foo.png')
img2 = Image('foo2.png')

drop_speed_text = Text(text="drop speed")
drop_speed = 		Slider(range=(1,200), resolution=0.01, orientation='horizontal', enable_events=True, default_value=54, size=(100,20))

starting_spread_rate_text = Text(text="initial spread rate")
starting_spread_rate = 		Slider(range=(1,5), resolution=0.01, orientation='horizontal', enable_events=True, default_value=1.49, size=(100,20))

S2_text = Text(text="S2")
S2 = 		Slider(range=(0,1.4), resolution=0.01, orientation='horizontal', enable_events=True, default_value=0.5, size=(100,20))

h_shift_text = Text(text="h_shift")
h_shift = 		Slider(range=(1,10), resolution=0.01, orientation='horizontal', enable_events=True, default_value=2.65, size=(100,20))


ds_text = Text(text="shift")
ds = 		Slider(range=(-100,100), resolution=0.01, orientation='horizontal', enable_events=True, default_value=-5.67, size=(100,20))


divisor_text = Text(text="divisor")
d = 		Slider(range=(0.1,10), resolution=0.01, orientation='horizontal', enable_events=True, default_value=3, size=(100,20))

evolve_button = Button("Evolve")

layout = [[img, img2],[Column([[drop_speed_text, drop_speed],
						[starting_spread_rate_text, starting_spread_rate],
						[S2_text, S2],
						[h_shift_text, h_shift],
						[ds_text, ds],
						[divisor_text, d],
						[evolve_button]])]]
window = Window("Tweak Stereo Image", layout)





def mutate(creature):
	s1, h1, s2, hs, ds, d = creature
	s1 = max(1, min(200, random.uniform(-10, 10) + s1))
	h1 = max(1, min(5, random.uniform(-1, 1) + h1))
	s2 = max(0, min(1.4, random.uniform(-0.3, 0.3) + s2))
	hs = max(1, min(10, random.uniform(-3, 3) + hs))
	ds = max(-100, min(100, random.uniform(-10, 10) + ds))
	d = max(0.1, min(10, random.uniform(-1, 1) + d))

	return [s1, h1, s2, hs, ds, d]

def get_best_from_pop(population):
	scores = [foo(creature[0], creature[1], creature[2], creature[3], creature[4], creature[5], display=False) for creature in population]
	return (population[scores.index(min(scores))], scores[scores.index(min(scores))])

def evolve(population, iterations):
	for i in range(iterations):
		best_creature, best_score = get_best_from_pop(population)
		# print(best_creature, best_score)
		population = [mutate(best_creature) for i in range(9)] + [best_creature]


	foo(best_creature[0], best_creature[1], best_creature[2], best_creature[3], best_creature[4], best_creature[5])
	print('%.2E' % Decimal(str(best_score)))




while True:
	event, values = window.read()
	d.value = 8
	if event == "Evolve":
		# genetic algo part

		current_creatures = [[values[2], values[3], values[4], values[5], values[6], values[7]]] * 20
		evolve(current_creatures, 1000)
	else:
		# os.system("cd ~/Desktop;python3 untitled2.py 20")
		print('%.2E' % Decimal(str(foo(values[2], values[3], values[4], values[5], values[6], values[7]))))
	img.update('foo.png')
	img2.update('foo2.png')
	if event in (None, 'Close'):
		break