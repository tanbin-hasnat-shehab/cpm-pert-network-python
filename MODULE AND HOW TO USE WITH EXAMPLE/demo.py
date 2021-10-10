import cpm

import matplotlib.pyplot as plt



tasks=['a','b','c','d','e']
durations=[2,3,1,5,3]
precedors=[
			['-'],
			['-'],
			['a'],
			['b'],
			['c','d']	
		]

img=cpm.graph(tasks,durations,precedors,10)

plt.show()