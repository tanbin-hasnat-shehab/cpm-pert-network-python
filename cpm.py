import networkx as nx   
import matplotlib.pyplot as plt
import matplotlib
import random
import string


def graph(mytask,days,precedors,result_tasks,xx):
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
	letters = string.ascii_lowercase
	G = nx.cycle_graph()
	all_nodes=[]
	for i in range(200000):
		all_nodes.append((i))
	c=1
	aa=50
	def common_data(list1, list2):
	    result = False
	    for x in list1:
	        for y in list2:
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
	#########################################################################################
	G = nx.DiGraph()
	ss=10
	labels={}
	for i in range(len(task)):
		ax=int(result_tasks[f'task{i}']['ES'])
		bx=int(result_tasks[f'task{i}']['EF'])
		cx=int(result_tasks[f'task{i}']['LS'])
		dx=int(result_tasks[f'task{i}']['LF'])
		
		if (ax==cx) and (bx==dx):
			dec=True
			print(dec)
			G.add_edge(aa*task[i].left_node,aa*task[i].right_node)		
		else:
			dec=False
			print(dec)
			G.add_edge(aa*task[i].left_node,aa*task[i].right_node)
		labels[(aa*task[i].left_node,aa*task[i].right_node)]=f'{ax},{bx}\n{task[i].name}\n{cx},{dx}'

	#edge_colors = ['r' if dec==True else 'b' for e in G.edges]
	#edge_color=edge_colors
	pos=nx.spring_layout(G)
	nx.draw_networkx_edges(G, pos,arrowsize=8)



	
	#, arrowstyle='->', arrowsize=10
	nx.draw(G, pos,node_size =200,with_labels = True)
	nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,font_size=xx)


	#plt.style.use('default')
	#plt.subplots(figsize=(20,20))
	plt.savefig('/tmp/a.png')
	#plt.show()
	z=('/tmp/a.png')
	
	return z

