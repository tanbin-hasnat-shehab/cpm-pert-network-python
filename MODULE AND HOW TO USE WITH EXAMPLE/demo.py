import cpm

import matplotlib.pyplot as plt



activities=['a','b','c','d','e','f','g','h','i','j']
durations=[2,3,1,5,3,5,3,2,1,3]
predecessors=[
			['-'],
			['-'],
			['b'],
			['a','c'],
			['b'],
			['b'],
			['d','e'],
			['d','e'],
			['h'],
			['f','g','i']

		]



#show_results(boolean),fig_size(int),text_size(int),line_width(int)  ----are optional parameters,more the number of activities ,greater the fig_size is...


#showing figure

img=cpm.graph(activities,durations,predecessors,show_results=False,fig_size=25,text_size=10,line_width=3)

plt.show()


#set show_results = True   to save the results into a text file
