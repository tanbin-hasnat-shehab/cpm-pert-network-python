





# cpm-pert-network-python
#HOW TO USE THE MODULE

------------GO TO DIRECTORY 'MODULE AND HOW TO USE WITH EXAMPLE' -----------------------------

A demo is shown below :


import matplotlib.pyplot as plt
import cpm                      #importing module 




tasks=['a','b','c','d','e']     #all the activities in a list 
durations=[2,3,1,5,3]           #list of durations of each task
                    
precedors=[
			['-'],
			['-'],
			['a'],
			['b'],
			['c','d']	
		]                           #precedors lists in a list
                            
img=cpm.graph(tasks,durations,precedors,10)     #returns the path of generated image and show critical path and entire project completion time in the console

plt.show()                                      #showing image








py : https://drive.google.com/drive/folders/1-4JKC1mBGtWVnwFPlIX5Fa3sMaDiYcR7
