
import networkx as nx   
import matplotlib.pyplot as plt
import matplotlib
import random
import string

def trial_graphs(mytask,days,precedors,fontSize,f_size,l_width,show_my_results):
    
    
    
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
                
            else:
                tasks[task]['isCritical']=False
                
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

    
    new_nodes=[]
    new_nodes.append(task[0].left_node)
    for i in range(len(task)):
        if task[i].left_node not in new_nodes:
            new_nodes.append(task[i].left_node)
        if task[i].right_node not in new_nodes:
            new_nodes.append(task[i].right_node)
    
    n_nodes=[]
    for i in range(len(new_nodes)):
        n_nodes.append(i)

    for i in range(len(task)):
        for j in range(len(new_nodes)):
            if task[i].left_node==new_nodes[j]:
                task[i].left_node=n_nodes[j]
            if task[i].right_node==new_nodes[j]:
                task[i].right_node=n_nodes[j]





    for i in range(len(task)):
        ax=int(result_tasks[f'task{i}']['ES'])
        bx=int(result_tasks[f'task{i}']['EF'])
        cx=int(result_tasks[f'task{i}']['LS'])
        dx=int(result_tasks[f'task{i}']['LF'])
        
        if (ax==cx) and (bx==dx):
            dec=True
            
            G.add_edge(aa*task[i].left_node,aa*task[i].right_node,color='r',weight=l_width)     
        else:
            dec=False
        
            G.add_edge(aa*task[i].left_node,aa*task[i].right_node,weight=1)
        labels[(aa*task[i].left_node,aa*task[i].right_node)]=f'{ax},{bx}\n{task[i].name}\n{cx},{dx}'
    weights = nx.get_edge_attributes(G,'weight').values()
    colors = nx.get_edge_attributes(G,'color').values()
    plt.figure(figsize=(f_size,f_size))
    pos=nx.spring_layout(G,k=1)
    nx.draw_networkx_edges(G, pos,width=list(weights),edge_color=colors,arrowstyle='->',arrowsize=f_size+10)



    
    #, arrowstyle='->', arrowsize=10
    
    nx.draw(G, pos,node_size =20*f_size,with_labels = True)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,font_size=fontSize)
    
    
    '''
    try:
        
        plt.savefig('/a.png')
        z=('/a.png')
    except:
        
        plt.savefig('a.png')
        z=('a.png')
    '''

    def show_result_fn():
        f = open("results.txt", "w")
        f.write('Name\tduration\tES\tEF\tLS\tLF\tFloat\tisCritical ?\n')
        print('Name\tduration\tES\tEF\tLS\tLF\tFloat\tisCritical ?\n')
        for i in range(len(result_tasks)):
            
            print(f"{result_tasks[f'task{i}']['name']}\t{result_tasks[f'task{i}']['duration']}\t\t{result_tasks[f'task{i}']['ES']}\t{result_tasks[f'task{i}']['EF']}\t{result_tasks[f'task{i}']['LS']}\t{result_tasks[f'task{i}']['LF']}\t{result_tasks[f'task{i}']['float']}\t{result_tasks[f'task{i}']['isCritical']}")
            strs=f"{result_tasks[f'task{i}']['name']}\t{result_tasks[f'task{i}']['duration']}\t\t{result_tasks[f'task{i}']['ES']}\t{result_tasks[f'task{i}']['EF']}\t{result_tasks[f'task{i}']['LS']}\t{result_tasks[f'task{i}']['LF']}\t{result_tasks[f'task{i}']['float']}\t{result_tasks[f'task{i}']['isCritical']}"
            f.write(strs+'\n')
        f.close()
    if show_my_results==True:
        show_result_fn()







    multipiller=100
    edge_space=1
    #matched=True
    def check_crossings():
        #print(f'task 8 left={task[8].left_node} r8={task[8].right_node}')
        #print(len(task))
        for i in range(len(task)):
            
            task[i].x1=round(pos[task[i].left_node][0]*multipiller)
            task[i].y1=round(pos[task[i].left_node][1]*multipiller)
            task[i].x2=round(pos[task[i].right_node][0]*multipiller)
            task[i].y2=round(pos[task[i].right_node][1]*multipiller)
            if task[i].x1>task[i].x2:
                maxx1=task[i].x1
                task[i].x1=task[i].x2
                task[i].x2=maxx1

                maxy1=task[i].y1
                task[i].y1=task[i].y2
                task[i].y2=maxy1
            #print(f'task {i} x1={task[i].x1}  y1={task[i].y1}  x2={task[i].x2}  y2={task[i].y2}')

        for i in range(len(task)):
            #print(f'task {i} = x1 : {task[i].x1} y1:{task[i].y1} x2:{task[i].x2} y2:{task[i].y2}')
            if task[i].x1==task[i].x2:
                mmm=1
                ccc=task[i].x1
            else:
                mmm=(task[i].y1-task[i].y2)/(task[i].x1-task[i].x2)
                ccc=-mmm*task[i].x1+task[i].y1
            task[i].c=ccc
            task[i].m=mmm
        m_c=0
        

        def checke_match(a,b,m_c):
        
            if a.m!=b.m:
                sol_x=round((b.c-a.c)/(a.m-b.m))
                spacer=1
                #print(f'this is {a.name} {(a.x1+spacer,a.x2-spacer)} and  {b.name} {(b.x1+spacer,b.x2-spacer)} solution is {sol_x}')

                if (sol_x<=a.x2-spacer and sol_x>=a.x1+spacer) and (sol_x<=b.x2-spacer and sol_x>=b.x1+spacer):
                    m_c+=1
                    #print(f'this is m_c ============================================================================= = {m_c}')
            else:
                pass
            return m_c

        for i in range(len(task)):
            mm_c=0
            for j in range(len(task)):
                if i==j:
                    pass
                else:
                    mm_c=checke_match(task[i], task[j],m_c)
                if mm_c==1:
                    break
            if mm_c==1:
                break
       
        if mm_c==1:
            matched=True
        else:
            matched=False
        return matched

    matched=check_crossings()
    return matched

def graph(activities,durations,predecessors,*args,**kwargs):
    mytask=activities
    days=durations
    precedors=predecessors
    fontSize=kwargs.get('text_size',10)
    f_size=kwargs.get('fig_size',8)
    l_width=kwargs.get('line_width',3)
    show_my_results=kwargs.get('show_results',True)

    while True:
        #print("trying")
        plt.clf()
        matched=trial_graphs(mytask,days,precedors,fontSize,f_size,l_width,show_my_results)
        if matched==False:
            #print(f'this is matched  {matched}')
            plt.savefig('a.png')
            z=('a.png')
            break
    return z
