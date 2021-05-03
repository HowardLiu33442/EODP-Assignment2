import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange
plt.style.use('ggplot')
childcare = pd.read_csv('Childcaretime.csv')
childcare = childcare.loc[(childcare['Who'] == 'Employment related')|(childcare['Who']=='Main job')|(childcare['Who']=='Child care'), ['Who', 'Males', 'Females']]
male_time = []
female_time = []
for time in childcare['Males']:  
    male_time.append(60*int(time[0])+10*int(time[2])+int(time[3]))
for time in childcare['Females']:
    female_time.append(60*int(time[0])+10*int(time[2])+int(time[3]))

male = plt.bar(arange(len(male_time))-0.3, male_time, width=0.3, label='Male', color='blue', alpha=0.4)
female = plt.bar(arange(len(female_time)),female_time, width=0.3,color='r', label='Female', alpha=0.4)
for rect in male + female:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')
plt.xticks(arange(len(childcare['Who'].tolist())), childcare['Who'].tolist(), fontweight='bold')
plt.yticks(fontweight='bold')
plt.legend()
plt.title('Time spent on doing activities on weekdays(Female vs. Male)', fontsize=12)
plt.xlabel('Activity',fontsize=10)
plt.ylabel('Time(minutes)', fontsize=10)
plt.savefig('childcare.png', format='png') 
plt.show()