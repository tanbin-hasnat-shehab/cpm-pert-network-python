import calculation
import cpm 
import cpm2
import matplotlib.pyplot as plt
import streamlit as st
st.set_page_config(layout="wide")
n=st.slider('number of tasks', min_value=1, max_value=100, value=5, step=1)
text_on_graph=st.slider('text_on_graph', min_value=1, max_value=50, value=9, step=1)
myweight=st.slider('critical path line weight', min_value=1, max_value=5, value=3, step=1)
f_size=st.slider('size of the model', min_value=3, max_value=50, value=7, step=1)
c1, c2,c3 = st.columns((1,1,5))
if n:
    with c1:
        st.subheader('Tasks')
        task_names={}
        for i in range(n):
            task_names[f'task_no{i}']=''
        for k, v in task_names.items():
            task_names[k] = st.text_input(k, v)
            #st.write(task_names[k])
        #print(task_names)
    with c2:
        st.subheader('durations')
        durations={}
        duration_one_d=[]
        for i in range(n):
            durations[f'durations{i}']=''
        for k, v in durations.items():
            durations[k] = st.text_input(k, v)
            #st.write(durations[k])
        for i in range(n):
            duration_one_d.append(durations[f'durations{i}'])
        #print(duration_one_d)
    with c3:
        

        st.subheader('predecsors')
        if task_names[f'task_no{n-1}']:
            dep=[]
            dependency={}
            for i in range(n):
                dependency[f'precedors{i}']=''
            for k, v in dependency.items():
                dependency[k] = st.text_input(k, v)
                dep.append(dependency[k].split(','))
            #print(dep)
            names=[]
            for i in range(n):
                names.append(task_names[f'task_no{i}'])
                #st.write(dependency[k])
            #print(names)
            dep_in_numbers=[]
            for i in range(n):
                xx=[]
                for j in range(len(dep[i])):
                    if dep[i][0]=='-':
                        xx.append('-')
                    else:
                        xx.append(str(names.index(dep[i][j])))
                dep_in_numbers.append(xx)
            #print(dep_in_numbers)




if st.button('ok'):
    
    try: 
        f = open("/tmp/cpm.txt", "w")
    except:
        f = open("tmp/cpm.txt", "w")
    for i in range(n):
        a=f'{i}'
        b=task_names[f'task_no{i}']
        c=durations[f'durations{i}']
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
    try:
        mydic=calculation.show_results('/tmp/cpm.txt')
    except:
        mydic=calculation.show_results('tmp/cpm.txt')
    tasks=mydic
    #print(mydic)
    #img=cpm2.graph(names, duration_one_d, dep, mydic, text_on_graph,myweight,f_size)
    #print(f_size)
    img=cpm2.graph(names, duration_one_d, dep,text_size=text_on_graph, fig_size=f_size,line_width=myweight,show_results=False)




    
    st.image(img)

    cl1,cl2,cl3,cl4,cl5,cl6,cl7,cl8=st.columns(8)
    with cl1:
        st.subheader('task name')
        for task in tasks:    
            st.write((str(tasks[task]['name'])))
    with cl2:
        st.subheader('duration')
    
        for task in tasks:    
            st.write((str(tasks[task]['duration'])))
    with cl3:
        st.subheader('ES')
    
        for task in tasks:    
            st.write((str(tasks[task]['ES'])))
    with cl4:
        st.subheader('EF')
    
        for task in tasks:    
            st.write((str(tasks[task]['EF'])))
    with cl5:
        st.subheader('LS')
    
        for task in tasks:    
            st.write((str(tasks[task]['LS'])))
    with cl6:
        st.subheader('LF')
    
        for task in tasks:    
            st.write((str(tasks[task]['LF'])))
    with cl7:
        st.subheader('float')
    
        for task in tasks:    
            st.write((str(tasks[task]['float'])))
    with cl8:
        st.subheader('isCritical ?')
        proj_com=0
        critical_path=''
        for task in tasks:
            if tasks[task]['ES']==tasks[task]['LS'] and tasks[task]['EF']==tasks[task]['LF']:
                proj_com=proj_com+int(tasks[task]['duration'])
                critical_path=critical_path+' -----> '+tasks[task]['name']

                st.write(True)
            else:
                st.write(False)
    st.write(f'CRITICAL PATH : {critical_path}')
    st.write(f'PRJECT COMPLETION TIME = {proj_com}')




































    
