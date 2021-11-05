import networkx as nx   
import matplotlib.pyplot as plt
import matplotlib
import random
import string


def graph(mytask,days,precedors,result_tasks,xx,myweight,f_size):
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
	G = nx.cycle_graph(800)
	all_nodes=[]
	for i in range(2000):
		all_nodes.append((i))
	c=1
	aa=1
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
			G.add_edge(aa*task[i].left_node,aa*task[i].right_node,color='r',weight=myweight)		
		else:
			dec=False
			print(dec)
			G.add_edge(aa*task[i].left_node,aa*task[i].right_node,weight=1)
		labels[(aa*task[i].left_node,aa*task[i].right_node)]=f'{ax},{bx}\n{task[i].name}\n{cx},{dx}'
	weights = nx.get_edge_attributes(G,'weight').values()
	colors = nx.get_edge_attributes(G,'color').values()
	plt.figure(1,figsize=(f_size,f_size))
	pos=nx.spring_layout(G)
	nx.draw_networkx_edges(G, pos,width=list(weights),edge_color=colors,arrowstyle='->',arrowsize=f_size+10)



	
	#, arrowstyle='->', arrowsize=10
	
	nx.draw(G, pos,with_labels = True)
	nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,font_size=xx)
	print(f'thisssssssssssssssssss isssssssssssssssss {G.size()}')


	#plt.style.use('default')  node_size =20*f_size
	#plt.figure(1,figsize=(5,5))
	try:
		
		plt.savefig('/tmp/a.png')
		z=('/tmp/a.png')
	except:
		
		plt.savefig('tmp/a.png')
		z=('tmp/a.png')

	#plt.show()
	
	
	return z

