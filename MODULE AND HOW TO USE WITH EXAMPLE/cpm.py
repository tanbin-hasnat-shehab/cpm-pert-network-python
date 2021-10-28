import networkx as nx   
import matplotlib.pyplot as plt
import matplotlib
import random
import string

def graph(mytask,days,precedors,fontSize):
	print(f'the type of xx is {type(fontSize)}')
	names=[]
	for i in range(len(mytask)):
		names.append(mytask[i])


	dep_in_numbers=[]
	for i in range(len(mytask)):
		xx=[]
		for j in range(len(precedors[i])):
			if precedors[i][0]=='-':
	   			xx.append('-')
	   			#dep_in_numbers.append(xx)
			else:
				xx.append(str(names.index(precedors[i][j])))
		dep_in_numbers.append(xx)
	
	print(f'thw dep in numb is {dep_in_numbers}')

	try:
		f = open("/cpm.txt", "w")
		path="/cpm.txt"
	except:
		f = open("cpm.txt", "w")
		path="cpm.txt"
	for i in range(len(mytask)):
	   	a=f'{i}'
	   	b=mytask[i]
	   	c=days[i]
	   	dep_str=''
	   	for j in range(len(dep_in_numbers[i])):
	   		if dep_in_numbers[i][0]=='-':
	   			dep_str=''
	   		else:
	   			if j==len(dep_in_numbers[i])-1:
	   				dep_str=dep_str+dep_in_numbers[i][j]
	   			else:
	   				dep_str=dep_str+dep_in_numbers[i][j]+';'
	   	f.write(f'{a},{b},{c},{dep_str}\n')
	        
	f.close()
	global show_results
	def show_results(a):
	    line = list() #contains a single line
	    singleElement = list()
	    tasks = dict() #contains all the tasks
	    number = -1
	    fhand = open(a)

	    for line in fhand:
	        singleElement=(line.split(',')) 
	        number += 1
	        for i in range(len(singleElement)): #creating the single task element
	            tasks['task'+ str(singleElement[0])]= dict()
	            tasks['task'+ str(singleElement[0])]['id'] = singleElement[0]
	            tasks['task'+ str(singleElement[0])]['name'] = singleElement[1]
	            tasks['task'+ str(singleElement[0])]['duration'] = singleElement[2]
	            if(singleElement[3] != "\n"):
	                tasks['task'+ str(singleElement[0])]['dependencies'] = singleElement[3].strip().split(';')
	            else:
	                tasks['task'+ str(singleElement[0])]['dependencies'] = ['-1']
	            tasks['task'+ str(singleElement[0])]['ES'] = 0
	            tasks['task'+ str(singleElement[0])]['EF'] = 0
	            tasks['task'+ str(singleElement[0])]['LS'] = 0
	            tasks['task'+ str(singleElement[0])]['LF'] = 0
	            tasks['task'+ str(singleElement[0])]['float'] = 0
	            tasks['task'+ str(singleElement[0])]['isCritical'] = False

	    # =============================================================================
	    # FORWARD PASS
	    # =============================================================================
	    for taskFW in tasks: #slides all the tasks
	        if('-1' in tasks[taskFW]['dependencies']): #checks if it's the first task
	            tasks[taskFW]['ES'] = 1
	            tasks[taskFW]['EF'] = (tasks[taskFW]['duration'])
	        else: #not the first task
	            for k in tasks.keys():
	                for dipendenza in tasks[k]['dependencies']: #slides all the dependency in a single task
	                    #print('task ' + taskFW + ' k '+ k + ' dipendenza ' +dipendenza)
	                    if(dipendenza != '-1' and len(tasks[k]['dependencies']) == 1): #if the task k has only one dependency
	                        tasks[k]['ES'] = int(tasks['task'+ dipendenza]['EF']) +1
	                        tasks[k]['EF'] = int(tasks[k]['ES']) + int(tasks[k]['duration']) -1
	                    elif(dipendenza !='-1'): #if the task k has more dependency
	                        if(int(tasks['task'+dipendenza]['EF']) > int(tasks[k]['ES'])):
	                            tasks[k]['ES'] = int(tasks['task'+ dipendenza]['EF']) +1
	                            tasks[k]['EF'] = int(tasks[k]['ES']) + int(tasks[k]['duration']) -1

	    aList = list() #list of task keys
	    for element in tasks.keys():
	        aList.append(element)

	    bList = list() #reversed list of task keys
	    while len(aList) > 0:
	        bList.append(aList.pop())
	        
	    # =============================================================================
	    # BACKWARD PASS
	    # =============================================================================
	    for taskBW in bList:
	        if(bList.index(taskBW) == 0): #check if it's the last task (so no more task)
	            tasks[taskBW]['LF']=tasks[taskBW]['EF']
	            tasks[taskBW]['LS']=tasks[taskBW]['ES']
	            
	        for dipendenza in tasks[taskBW]['dependencies']: #slides all the dependency in a single task
	            if(dipendenza != '-1'): #check if it's NOT the last task
	                if(tasks['task'+ dipendenza]['LF'] == 0): #check if the the dependency is already analyzed
	                    #print('ID dipendenza: '+str(tasks['task'+dipendenza]['id']) + ' taskBW: '+str(tasks[taskBW]['id']))
	                    tasks['task'+ dipendenza]['LF'] = int(tasks[taskBW]['LS']) -1
	                    tasks['task'+ dipendenza]['LS'] = int(tasks['task'+ dipendenza]['LF']) - int(tasks['task'+ dipendenza]['duration']) +1
	                    tasks['task'+ dipendenza]['float'] = int(tasks['task'+ dipendenza]['LF']) - int(tasks['task'+ dipendenza]['EF'])
	                    #print('IF1 dip LS: '+str(tasks['task'+dipendenza]['LS']) +' dip LF: '+str(tasks['task'+dipendenza]['LF']) + ' taskBW: '+str(tasks[taskBW]['id'])+' taskBW ES '+ str(tasks[taskBW]['ES']))
	                if(int(tasks['task'+ dipendenza]['LF']) >int(tasks[taskBW]['LS']) ): #put the minimun value of LF for the dependencies of a task
	                    tasks['task'+ dipendenza]['LF'] = int(tasks[taskBW]['LS']) -1
	                    tasks['task'+ dipendenza]['LS'] = int(tasks['task'+ dipendenza]['LF']) - int(tasks['task'+ dipendenza]['duration']) +1
	                    tasks['task'+ dipendenza]['float'] = int(tasks['task'+ dipendenza]['LF']) - int(tasks['task'+ dipendenza]['EF'])
	                    #print('IF2 dip LS: '+str(tasks['task'+dipendenza]['LS']) +' dip LF: '+str(tasks['task'+dipendenza]['LF']) + ' taskBW: '+str(tasks[taskBW]['id']))
	    # =============================================================================
	    # PRINTING  
	    # =============================================================================
	    #print('task id, task name, duration, ES, EF, LS, LF, float, isCritical')
	    c=0
	    for task in tasks:
	        tasks[task]['ES']=int(tasks[task]['ES'])
	        tasks[task]['EF']=int(tasks[task]['EF'])
	        tasks[task]['LS']=int(tasks[task]['LS'])
	        tasks[task]['LF']=int(tasks[task]['LF'])
	        #print(str(tasks[task]['id']) +', '+str(tasks[task]['name']) +', '+str(tasks[task]['duration']) +', '+str(tasks[task]['ES']) +', '+str(tasks[task]['EF']) +', '+str(tasks[task]['LS']) +', '+str(tasks[task]['LF']) +', '+str(tasks[task]['float']) +', '+str(tasks[task]['isCritical']))
	    i=0
	    for task in tasks:
	        ax=tasks[task]['ES']
	        bx=tasks[task]['EF']
	        cx=tasks[task]['LS']
	        dx=tasks[task]['LF']
	        if ax==cx and bx==dx:
	            tasks[task]['isCritical']=True
	            print(f'1st  and {tasks[task]["isCritical"]}')
	        else:
	            tasks[task]['isCritical']=False
	            print(f'2nd  and {tasks[task]["isCritical"]}')
	        i+=1

	    
	    return tasks

	result_tasks=show_results(path)


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
	#G = nx.cycle_graph(800)
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
	nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,font_size=fontSize)
	#font_size=xx)


	try:
		img=plt.savefig('/a.png')
	
		z=('/tmp/a.png')
	except:
		img=plt.savefig('a.png')
		
		z=('tmp/a.png')

	proj_com=0
	critical_path=''
	for task in result_tasks:
		if result_tasks[task]['ES']==result_tasks[task]['LS'] and result_tasks[task]['EF']==result_tasks[task]['LF']:
			proj_com=proj_com+int(result_tasks[task]['duration'])
			critical_path=critical_path+' -----> '+result_tasks[task]['name']
	
	print(result_tasks)

	print(f'\n\n critical path is {critical_path}')
	print(f'project completion time  is {proj_com}')

	return z
