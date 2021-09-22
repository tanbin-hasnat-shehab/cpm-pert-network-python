from openpyxl import load_workbook
import streamlit as st


wb=load_workbook('data.xlsx')
sheet=wb.active

input_t=st.text_input('here')
if st.button('add'):
	
	a=len(sheet['A'])
	sheet.cell(row=a+1, column=1).value=input_t
	
if st.button('ok show'):
	
	for i in range(len(sheet['A'])):
		st.write(sheet.cell(row=i+1,column=1).value)
