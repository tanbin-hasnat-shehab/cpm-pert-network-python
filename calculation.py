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
            tasks[task]['isCritical']==1
            #print(f'1st  and {tasks[task]["isCritical"]}')
        else:
            tasks[task]['isCritical']==0
            #print(f'2nd  and {tasks[task]["isCritical"]}')
        i+=1

        
    #print(tasks)
    #print(tasks[f'task{0}']['LF'])
    #print('\n\n\n')
    #print(tasks)
    return tasks
             
            
        
                
            
    
        
        
        
    



    














