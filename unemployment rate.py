import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('ggplot')
%matplotlib inline
Labour = pd.read_csv('Labour force status by Sex.csv')
Labour.set_index('Unnamed: 0', inplace=True)
Labour=Labour.loc[:,['Unemployment rate ;  > Males ;.1', 'Unemployment rate ;  > Females ;.1', 'Participation rate ;  > Females ;.1', 'Participation rate ;  > Males ;.1']]
date_time = []
for date in Labour.index[513:]:
    date_time.append(date)
male = []
for num in Labour['Unemployment rate ;  > Males ;.1'][513:]:
    male.append(float(num))
female = []
for num in Labour['Unemployment rate ;  > Females ;.1'][513:]:
    female.append(float(num))
x = [datetime.strptime(d,'%b-%Y').date() for d in date_time]
plt.plot(x,male,linewidth = '1', label = "Male", color='#9ACD32', linestyle='-', marker='s',markersize=6, markeredgecolor='black',markerfacecolor='#87CEFA')
for a, b in zip(x, male):
    plt.text(a, b-0.22, b, ha='center', va='bottom', fontsize=10)
plt.plot(x,female,linewidth = '1', label = "Female", color='red', linestyle='-', marker='o',markersize=6, markeredgecolor='black',markerfacecolor='#7FFFD4')
for a, b in zip(x, female):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.legend()
plt.title('Unemployment Rate During COVID-19(Male vs. Female)',fontsize=12)
plt.ylabel('Unemployment Rate(%)', fontsize=10)
plt.yticks(fontweight='bold')
plt.xticks(fontweight='bold')
plt.savefig('unemployment rate.png', format='png')
plt.show()


date_time1 = []
for date in Labour.index[405:]:
    date_time1.append(date)
male1 = []
for num in Labour['Participation rate ;  > Males ;.1'][405:]:
    male1.append(float(num))
female1 = []
for num in Labour['Participation rate ;  > Females ;.1'][405:]:
    female1.append(float(num))
x1 = [datetime.strptime(d,'%b-%Y').date() for d in date_time1]
plt.plot(x1,male1,linewidth = '1', label = "Male", color='b', linestyle='-')

plt.plot(x1,female1,linewidth = '1', label = "Female", color='green', linestyle='-')

plt.legend()
plt.title('Participation Rate During COVID-19(Male vs. Female)',fontsize=12)
plt.ylabel('Participation Rate(%)', fontsize=10)
plt.yticks(fontweight='bold')
plt.xticks(fontweight='bold')
plt.savefig('participation rate.png', format='png')
plt.show()

