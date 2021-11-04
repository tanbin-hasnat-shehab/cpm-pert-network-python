import cpm

import matplotlib.pyplot as plt



activities=['a','b','c','d','e']
durations=[2,3,1,5,3]
predecessors=[
			['-'],
			['-'],
			['a'],
			['b'],
			['c','d']	
		]


img=cpm.graph(activities,durations,predecessors,show_results=True,fig_size=20,text_size=10,line_width=3)
#show_results,fig_size,text_size,line_width  ----are optional parameters,more the number of activities ,greater the fig_size is...


#showing figure
plt.show()
