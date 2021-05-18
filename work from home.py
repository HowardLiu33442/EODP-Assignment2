import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange

plt.style.use('ggplot')

work_from_home = pd.read_csv('Work from home arrangement.csv')
work_from_home = work_from_home.loc[(work_from_home['Unnamed: 0'] == 'Childcare, Family considerations')|(work_from_home['Unnamed: 0']=='Flexible working arrangements')|(work_from_home['Unnamed: 0']=='Prefer to increase the amount of work done from home'), ['Unnamed: 0','Sex', 'Unnamed: 2']]
male = []
female = []
for num in work_from_home['Sex']:  
    male.append(float(num))
for num in work_from_home['Unnamed: 2']:
    female.append(float(num))
data = {'Male': male, 'Female': female}
df = pd.DataFrame(data,columns=['Male','Female'], index = work_from_home['Unnamed: 0'].tolist())
plt.style.use('ggplot')
df.plot.barh(alpha=0.7)
plt.title('Proportion of Work from Home Arrangement(Male vs. Female)', fontsize=12)
plt.savefig('work from home arragement.png', format='png',dpi=200,bbox_inches='tight')
plt.show()
