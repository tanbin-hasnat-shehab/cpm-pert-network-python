import streamlit as st
import networkx as nx   
# Sample graph
import matplotlib.pyplot as plt
import random
import string

mytask=['a','b','c','d','e','f','g','h','i','j']
days=[2,4,5,1,2,3,7,5,3,1]
precedors=[
								['-'],
								['-'],
								['-']
								,['a']
								,['c']
								,['a']
			
								,['c']
								,['j','f']
								,['h','g']
								,['b','d','e']]

class points:
	def __init__(self,name,duration,dependency,already):
		self.name=name
		self.duration=duration
		self.dependency=dependency
		self.already=already


task=[]
for i in range(len(mytask)):

	frame=points(mytask[i], days[i], precedors[i],False)
	task.append(frame)


#print(string.ascii_uppercase)


#print(hasattr(task[i], 'right'))

letters = string.ascii_lowercase
'''
random_ids=[]

for i in range(len(task)):
	letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(10))
	random_ids.append(result_str)  random. randint(0,1000)
'''
G = nx.DiGraph()

all_nodes=[]
for i in range(200):
	all_nodes.append((i))
c=1
####################################
aa=random.randint(0,1000)


def common_data(list1, list2):
    result = False
  
    # traverse in the 1st list
    for x in list1:
  
        # traverse in the 2nd list
        for y in list2:
    
            # if one common
            if x == y:
                result = True
                return result 
                  
    return result
for i in range(len(task)):
	if task[i].dependency[0]=='-':
		task[i].left_node=all_nodes[0]
	else:
		for j in range(len(task)):
			if i==j:
				pass
			else:
				if common_data(task[i].dependency, task[j].dependency):
					task[i].left_node=all_nodes[c]
					task[j].left_node=all_nodes[c]
	c+=1

for i in range(len(task)):
	if hasattr(task[i], 'left_node'):
		pass
	else:
		task[i].left_node=all_nodes[c]

	c+=1

for i in range(len(task)):
	
	for j in range(len(task[i].dependency)):
		for k in range(len(task)):
			if  task[i].dependency[j]==task[k].name:
				if hasattr(task[k], 'right_node'):
					pass
				else:
					task[k].right_node=task[i].left_node


for i in range(len(task)):
	if hasattr(task[i], 'right_node'):
		pass
	else:
		task[i].right_node=all_nodes[c]

	


'''
for i in range(len(task)):
	
	print(f'name = {task[i].name} and left ={task[i].left_node} and right = {task[i].right_node}')

'''

		
	#print(f'name = {task[i].name} and left ={task[i].left_node} ')














G = nx.DiGraph()





for i in range(len(task)):
	G.add_edge(task[i].left_node,task[i].right_node)



#labels = {(0,1):f'{1}', (2,3):'bar'}

pos=nx.spring_layout(G)
#edge_labels=labels
nx.draw(G, pos)
#nx.draw_networkx_edge_labels(G,pos)
#plt.show()
plt.savefig('a.png')
if st.button('run'):
	st.image('a.png')
