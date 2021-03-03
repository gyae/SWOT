# -*- coding: utf-8 -*-
"""SWOT-анализ

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X2A4s05PJjQQV7DDAARYEjl9reHOde24

#Задание 1

#Информация об исполнителе
"""

print('Исполнитель:')
print('ФИО: Гуменюк Яна Евгеньевна')
print('Группа: 20БИ-3')
!ln -fs /usr/share/zoneinfo/Europe/Moscow /etc/localtime
!date

"""#Связь и обмен данными с Google-диском и другие манипуляции, обеспечивающие связь с необходимыми ресурсами на удаленном сервере"""

# Commented out IPython magic to ensure Python compatibility.
from google.colab import auth
auth.authenticate_user()
!pip install --upgrade gspread
import gspread
from google.colab import drive
drive.mount('/content/drive')
import os
print(os.getcwd())
print(os.listdir('./'))
print(os.listdir('/content/drive'))
print(os.listdir('/content/drive/MyDrive/Colab Notebooks/Task1'))
# %ll -lF /content/drive/MyDrive/"Colab Notebooks"/"Task1"
from oauth2client.client import GoogleCredentials
gs = gspread.authorize(GoogleCredentials.get_application_default())

"""# Таблица"""

import gspread
from oauth2client.client import GoogleCredentials
gc = gspread.authorize(GoogleCredentials.get_application_default())
table = gs.open_by_key('1EmUdIEw8O1xec-5P77ZLF5BY9-Kw34Guyg38vyQSRRE')
print(table.worksheets())
print (dir(table))

"""#Strengths"""

print(table.worksheets())
try:
  worksheet = table.worksheet('Strengths')
except Exception as mistake:
    print('\n',mistake)
    print("Необходимо создать лист\n")
    worksheet = table.add_worksheet("Strengths",100,100)

print(dir(worksheet))
rows = worksheet.get_all_values()
power_strengths = list()
i=0
for row in rows:
  if(i>0):
    print (i, row)
    power_strengths.append(int(row[2])*float(row[3]))
  i+=1
cell_list = worksheet.range('E2:E5')
cell_values = power_strengths
for i, val in enumerate(cell_values):  
    cell_list[i].value = val   
worksheet.update_cells(cell_list)

import matplotlib
import matplotlib.pyplot as plt

x_float = [1,2,3,4]
y = power_strengths
y_float = power_strengths                                                                                                                                 

x_pos=list()
for i in range(x_float.__len__()):
    x_pos.append(i)

fig=plt.figure(figsize=(8,6), dpi=72)
plt.bar(x_pos, y_float, width=0.75, align='edge', alpha=0.4)
plt.xticks(x_pos,  x_float, fontsize=14)
plt.xlabel('Обозначения', fontsize=14)
plt.ylabel('Мощность воздействия', fontsize=14)
plt.title('Strengths', fontsize=14)
plt.grid(True, color='r', linestyle='-', linewidth=2)

plt.show()

"""#Weaknesses"""

print(table.worksheets())
try:
  worksheet = table.worksheet('Weaknesses')
except Exception as mistake:
    print('\n',mistake)
    print("Необходимо создать лист\n")
    worksheet = table.add_worksheet("Weaknesses",100,100)

print(dir(worksheet))
rows = worksheet.get_all_values()
power_weaknesses = list()
i=0
for row in rows:
  if(i>0):
    print (i, row)
    power_weaknesses.append(int(row[2])*float(row[3]))
  i+=1
cell_list = worksheet.range('E2:E5')
cell_values = power_weaknesses
for i, val in enumerate(cell_values):  
    cell_list[i].value = val   
worksheet.update_cells(cell_list)

import matplotlib
import matplotlib.pyplot as plt

x_float = [1,2,3,4]
y = power_weaknesses
y_float = power_weaknesses                                                                                                                                 

x_pos=list()
for i in range(x_float.__len__()):
    x_pos.append(i)

fig=plt.figure(figsize=(8,6), dpi=72)
plt.bar(x_pos, y_float, width=0.75, align='edge', alpha=0.4)
plt.xticks(x_pos,  x_float, fontsize=14)
plt.xlabel('Обозначения', fontsize=14)
plt.ylabel('Мощность воздействия', fontsize=14)
plt.title('Weaknesses', fontsize=14)
plt.grid(True, color='r', linestyle='-', linewidth=2)

plt.show()

"""#Opportunities"""

print(table.worksheets())
try:
  worksheet = table.worksheet('Opportunities')
except Exception as mistake:
    print('\n',mistake)
    print("Необходимо создать лист\n")
    worksheet = table.add_worksheet("Opportunities",100,100)

print(dir(worksheet))
rows = worksheet.get_all_values()
power_opportunities = list()
i=0
for row in rows:
  if(i>0):
    print (i, row)
    power_opportunities.append(int(row[2])*float(row[3]))
  i+=1
cell_list = worksheet.range('E2:E5')
cell_values = power_opportunities
for i, val in enumerate(cell_values):  
    cell_list[i].value = val   
worksheet.update_cells(cell_list)

import matplotlib
import matplotlib.pyplot as plt

x_float = [1,2,3,4]
y = power_opportunities
y_float = power_opportunities                                                                                                                               

x_pos=list()
for i in range(x_float.__len__()):
    x_pos.append(i)

fig=plt.figure(figsize=(8,6), dpi=72)
plt.bar(x_pos, y_float, width=0.75, align='edge', alpha=0.4)
plt.xticks(x_pos,  x_float, fontsize=14)
plt.xlabel('Обозначения', fontsize=14)
plt.ylabel('Мощность воздействия', fontsize=14)
plt.title('Opportunities', fontsize=14)
plt.grid(True, color='r', linestyle='-', linewidth=2)

plt.show()

"""#Threats"""

print(table.worksheets())
try:
  worksheet = table.worksheet('Threats')
except Exception as mistake:
    print('\n',mistake)
    print("Необходимо создать лист\n")
    worksheet = table.add_worksheet("Threats",100,100)

print(dir(worksheet))
rows = worksheet.get_all_values()
power_threats = list()
i=0
for row in rows:
  if(i>0):
    print (i, row)
    power_threats.append(int(row[2])*float(row[3]))
  i+=1
cell_list = worksheet.range('E2:E5')
cell_values = power_threats
for i, val in enumerate(cell_values):  
    cell_list[i].value = val   
worksheet.update_cells(cell_list)

import matplotlib
import matplotlib.pyplot as plt

x_float = [1,2,3,4]
y = power_threats
y_float = power_threats                                                                                                                                

x_pos=list()
for i in range(x_float.__len__()):
    x_pos.append(i)

fig=plt.figure(figsize=(8,6), dpi=72)
plt.bar(x_pos, y_float, width=0.75, align='edge', alpha=0.4)
plt.xticks(x_pos,  x_float, fontsize=14)
plt.xlabel('Обозначения', fontsize=14)
plt.ylabel('Мощность воздействия', fontsize=14)
plt.title('Threats', fontsize=14)
plt.grid(True, color='r', linestyle='-', linewidth=2)

plt.show()

"""# Итоговая таблица SWOT-анализа"""

print(table.worksheets())
try:
  worksheet = table.worksheet('Results')
except Exception as mistake:
    print('\n',mistake)
    print("Необходимо создать лист\n")
    worksheet = table.add_worksheet("Results",100,100)

print(dir(worksheet))
rows = worksheet.get_all_values()
value = list()
power = [sum(power_strengths),sum(power_weaknesses),sum(power_opportunities),sum(power_threats)]
print (power)
i=0
for row in rows:
  if(i>=0):
    print (i, row)
  i+=1
cell_list = worksheet.range('B1:B5')
cell_values = power
for i, val in enumerate(cell_values):  
    cell_list[i].value = val   
worksheet.update_cells(cell_list)
results = sum(power_strengths)-sum(power_weaknesses)+sum(power_opportunities)-sum(power_threats)
worksheet.update_cell(5,2,results)

import matplotlib
import matplotlib.pyplot as plt

title = [ "strengths", "weaknesses", "opportunities", "threats", "result"]
x=title
x_float = [1, 2, 3, 4, 5]
y = power
y_float = [sum(power_strengths),-sum(power_weaknesses),sum(power_opportunities),-sum(power_threats),results]                                                                                                                              

x_pos=list()
for i in range(x_float.__len__()):
    x_pos.append(i)

fig=plt.figure(figsize=(8,6), dpi=72)
plt.bar(x_pos, y_float, width=0.75, align='edge', alpha=0.4)
plt.xticks(x_pos,  x_float, fontsize=14)
plt.xlabel('Обозначения', fontsize=14)
plt.ylabel('Мощность воздействия', fontsize=14)
plt.title('SWOT', fontsize=14)
plt.grid(True, color='r', linestyle='-', linewidth=2)

plt.show()