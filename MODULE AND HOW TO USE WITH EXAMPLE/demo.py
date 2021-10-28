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

text_size_in_model=10
img=cpm.graph(tasks,durations,precedors,text_size_in_model)

plt.show()
