#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import statistics


# In[3]:


ELdata = pd.read_csv("Employees_who_have_left.csv")
EEdata = pd.read_csv("Existing_employees.csv")


# In[33]:


EEdata.head()


# In[34]:


ELdata.head()


# DATA PREPROCESSING
# 
# This step entails preparation of the data for analysis
# 
# SALARY COUNT FOR BOTH EMPLOYEES WHO LEFT AND EXISTING EMPLOYEES

# In[36]:


EEdata.salary.value_counts()


# In[37]:


ELdata.salary.value_counts()


# WORK ACCIDENT COUNT FOR BOTH EMPLOYEES WHO LEFT AND EXISTING

# In[38]:


EEdata['Work_accident'] = EEdata.Work_accident.replace(to_replace =1, 
                 value ="Yes") 
EEdata['Work_accident'] = EEdata.Work_accident.replace(to_replace =0, 
                 value ="No")
EEdata.Work_accident.value_counts()


# In[45]:


ELdata['Working_accident'] = ELdata.Work_accident.replace(to_replace =1,
                                  value ='Yes')
ELdata['Working_accident'] = ELdata.Work_accident.replace(to_replace =0,
                                   value ='No')
ELdata.Work_accident.value_counts()


# PROMOTION COUNT FOR THE LAST 5YEARS FOR BOTH EMPLOYEES WHO LEFT AND EXISTING

# In[42]:


EEdata['promotion_last_5years'] = EEdata.promotion_last_5years.replace(to_replace =1, 
                 value ="Yes") 
EEdata['promotion_last_5years'] = EEdata.promotion_last_5years.replace(to_replace =0, 
                 value ="No")
EEdata.promotion_last_5years.value_counts()


# In[44]:


ELdata['promotion_last_5years'] = ELdata.promotion_last_5years.replace(to_replace =1,
                                  value = 'Yes')
ELdata['promotion_last_5years'] = ELdata.promotion_last_5years.replace(to_replace =0,
                                   value = 'No')
ELdata.promotion_last_5years.value_counts()


# UNIVARIATE ANALYSIS FOR BOTH EMPLOYEES WHO LEFT AND EXISTING EMPLOYEES

# # SALARY PLOT

# In[56]:


plt.figure(figsize=(9,5))
sns.set(style='darkgrid')
sns.countplot(EEdata['salary'])
plt.title('Distribution of salaries of Employees who exist in the company')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.tight_layout()


# In[51]:


plt.figure(figsize=(9,5))
sns.set(style='darkgrid')
sns.countplot(ELdata['salary'])
plt.title('Distribution of salaries of Employees who left the company')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.tight_layout()


# # DEPARTMENT BAR PLOT

# In[57]:


plt.figure(figsize=(9,5))
sns.set(style='darkgrid')
sns.countplot(EEdata['dept'])
plt.title('Departments of Employees who exist in the Company')
plt.tight_layout()


# In[58]:


plt.figure(figsize=(9,5))
sns.set(style='darkgrid')
sns.countplot(ELdata['dept'])
plt.title('Departments of Employees who left the Company')
plt.tight_layout()


# # SATISFACTION LEVEL

# In[65]:


plt.figure(figsize=(9,5))
sns.set(style='darkgrid')
sns.boxplot(x='dept', y='satisfaction_level', data=EEdata)
plt.ylim([0,1])
plt.yticks(np.arange(0, 1, step=0.1)) #This step was added to make it have difference of 0.1 each on y axis
plt.title('Distribution of satisfaction level of Employees that exist by Department')
plt.xlabel('Department')
plt.ylabel('Satisfaction Level')
plt.tight_layout()


# In[61]:


plt.figure(figsize=(9,5))
sns.set(style='darkgrid')
sns.boxplot(x='dept', y='satisfaction_level', data=ELdata)
plt.ylim([0,1])
plt.title('Distribution of satisfaction level of Employees that left by Department')
plt.xlabel('Department')
plt.ylabel('Satisfaction Level')
plt.tight_layout()


# From the box plot of both Existing employees and employees who left the company, the following insights have been discovered
# 
# The mean satisfaction level of employees who left the company ranges bewteen 40-50%.
# 
# The mean satisfaction level of existing employees in the company ranges between 60-70%.
# 
# Performing further analysis on the satisfaction level of both employees who left and existing employees in the company for better insights

# In[69]:


plt.figure(figsize=(9,5))
sns.set(style='darkgrid')
sns.barplot(x='dept', y='satisfaction_level', hue='salary', data = EEdata)
plt.ylim([0,1])
plt.yticks(np.arange(0, 1, step=0.05))
plt.title('Satisfaction level by Dept based on the Salary of Employees who exist')
plt.tight_layout()
plt.legend(loc=2)


# In[70]:


plt.figure(figsize=(9,5))
sns.set(style='darkgrid')
sns.barplot(x='dept', y='satisfaction_level', hue='salary', data = ELdata)
plt.ylim([0,1])
plt.yticks(np.arange(0, 1, step=0.05))
plt.title('Satisfaction level by Dept based on the Salary of Employees who left')
plt.tight_layout()
plt.legend(loc=2)


# In[4]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import statistics


# In[6]:


ELdata = pd.read_csv("Employees_who_have_left.csv")
EEdata = pd.read_csv("Existing_employees.csv")


# In[9]:


plt.figure(figsize=(9,5))
sns.set(style='darkgrid')
plt.hist(EEdata['satisfaction_level'])
plt.title('Distribution of satisfaction_level of Existing Employees')
plt.xlabel('satisfaction_level')
plt.ylabel('Frequency')
plt.tight_layout()


# In[10]:


plt.figure(figsize=(9,5))
sns.set(style='darkgrid')
plt.hist(ELdata['satisfaction_level'])
plt.title('Distribution of satisfaction_level of Existing Employees')
plt.xlabel('satisfaction_level')
plt.ylabel('Frequency')
plt.tight_layout()


# From the satisfaction level chart plots of employees who left the company, it is observed that the satisfaction level is below average, therefore it is vital to show the percentage of employees who left that are in this category 

# DETERMINING THE PERCENTAGE OF EMPLOYEES WHO LEFT THE COMPANY HAD A SATISFACTION LEVEL BELOW AVERAGE OF 45

# In[12]:


(len(ELdata[ELdata['satisfaction_level']<0.45])/len(ELdata)) * 100


# From the output generated it can be observed that an estimate of 65% of employees who left had a satisfaction level below average of 45%. This needs to be looked into as it's a determining factor as to why employees left the company. Futher insights needs to be carried out as to why the satisfaction level is low. Promotion status, salary where two factors that was considered by intuition which prompted further analysis to determine the percenatge of employees who left having a satisfaction level of 45%, their promotion status and salary range

# In[13]:


(ELdata[ELdata['satisfaction_level']<0.45] ['salary'].value_counts(normalize=True))*100


# From the output displayed, it can be seen that an estimate of 61% of employees who left where low income earners, 37% where medium income earners and 2% where high income earners.

# In[15]:


(ELdata[ELdata['satisfaction_level']<0.45] ['promotion_last_5years'].value_counts(normalize=True))*100


# From the output displayed, it can be seen that 99.6% of employees who left had a satisfaction level less than 45% and where not promoted in the last five years

# Through the insights gained from the employees who left, it is vital to validate the position of the existing employees in the company.

# DETERMINING THE MEAN SATISFACTION LEVEL OF EXISTING EMPLOYEES

# In[16]:


statistics.mean(EEdata['satisfaction_level'])*100


# From the output it is seen that the average satisfaction level of existing employees is estimated around 67%. Hence using the metrics/determing factor of employees who left as an insight to crosscheck existing employees who are prone to leave the company considering their promotion status

# In[20]:


(len(EEdata[EEdata['satisfaction_level']<0.45])/len(ELdata)) * 100


# In[22]:


(EEdata[EEdata['satisfaction_level']<0.45] ['promotion_last_5years'].value_counts(normalize=True))*100


# From the result displayed it shows 44% of existing employees have a satisfaction level below 45% and from this it is seen that an estimate of 98% have not been promoted in the last 5 years

# Type Markdown and LaTeX:  𝛼2

# BI/MULTIVARIATE ANALYSIS

# In[23]:


plt.figure(figsize=(9,5))
sns.set(style='darkgrid')
sns.barplot(x='dept', y='satisfaction_level', hue='salary', data = ELdata)
plt.ylim([0,1])
plt.yticks(np.arange(0, 1, step=0.05))
plt.title('Satisfaction level by Dept based on the Salary of Employees who left')
plt.tight_layout()
plt.legend(loc=2)


# In[24]:


plt.figure(figsize=(9,5))
sns.set(style='darkgrid')
sns.barplot(x='dept', y='satisfaction_level', hue='salary', data = EEdata)
plt.ylim([0,1])
plt.yticks(np.arange(0, 1, step=0.05))
plt.title('Satisfaction level by Dept based on the Salary of  Existing Employees')
plt.tight_layout()
plt.legend(loc=2)


# In[27]:


EL_PRO =ELdata.pivot_table(index='salary',columns='promotion_last_5years',values='satisfaction_level')
EL_PRO.plot.bar()
plt.title("Satisfaction Level of Employees who left based on Salary and Promotion Status")
plt.xlabel("Salary Range")
plt.ylabel("Satisfaction Level")


# 0=NO while 1=YES

# Insight: Most employees who left with a high salary range weren't promoted,regardless of other employee who were promoted that had their salary range from low to medium, it futher can be seen that the satisfaction level was below average of 45% and the employees who left where not promoted irrespective of their salary income. Hence Satisfaction level and promotion status are determining factors as to why employees are leaving the company.

# In[28]:


EE_PRO =EEdata.pivot_table(index='salary',columns='promotion_last_5years',values='satisfaction_level')
EE_PRO.plot.bar()
plt.title(" Satisfaction Level of Existing Employee based on Salary and Promotion Status")
plt.xlabel("Salary Range")
plt.ylabel("Satisfaction Level")
plt.legend(loc=2)


# 0=NO while 1=YES

# The insight obtained from this ouput for employees still existing in the company is such that salary is not a determining factor as to why the existing employees should leave the company due to the fact that the employees satisfaction level is above an average of 50% irrespective of their promotion status.

# In[29]:


EL_PRO =ELdata.pivot_table(index='time_spend_company',columns='promotion_last_5years',values='satisfaction_level')
EL_PRO.plot.bar()
plt.title("Satisfaction Level of Employee who left based on Time Spent in the company and promotion Status")
plt.xlabel("Time Spent")
plt.ylabel("Satisfaction Level")


# 0=NO while 1=YES

# From output above the insight: Time Spent and promotion status are great factors that determine if an employee should leave or not, some employee who left that spent 6 years in the company weren't promoted, even though their satisfaction level was quite moderate. It can also be seen that An avaerge employee who left spent about 4 years with 0.45 satisfaction level and wasn't promoted.
# 
# Recommedation:

# In[30]:


Existing_Employee_PRO =EEdata.pivot_table(index='time_spend_company',columns='promotion_last_5years',values='satisfaction_level')
Existing_Employee_PRO.plot.bar()
plt.title("Satisfaction Level of Existing Employee based on Time Spent in the company and promotion Status")
plt.xlabel("Time Spent")
plt.ylabel("Satisfaction Level")
plt.legend(loc=2)


# 0=NO while 1=YES

# From the output the insight obtained is such that the existing employees in company irrespective of the time spent have a moderate satisfaction level and positive promotion status above 0.5 exculding employeees that spent between 5 years in the company. Hence satisfaction level of employees that spent 5 years should is considered as a determining factor and why such employees are prone to leave.

# In[31]:


EL_PRO =ELdata.pivot_table(index='salary',columns='Work_accident',values='satisfaction_level')
EL_PRO.plot.bar()
plt.title("Satisfaction Level of Employees who left based on Salary and work accident")
plt.xlabel("Salary")
plt.ylabel("Satisfaction Level")


# 0=NO while 1=YES

# From the output the insight obtained is such that employees who left that earn between low and medium salaries where affected by work accidents and their satisfaction level was below avaerage of 0.45 as compared to those with a high salary. Hence work accident and satisfaction level are reasons as to why employees are leaving the company.

# In[32]:


Existing_Employee_PRO =EEdata.pivot_table(index='salary',columns='Work_accident',values='satisfaction_level')
Existing_Employee_PRO.plot.bar()
plt.title("Satisfaction Level of Existing Employee based on Salary in the company and work accident")
plt.xlabel("salary")
plt.ylabel("Satisfaction Level")


# In[33]:


EL_PRO =ELdata.pivot_table(index='number_project',columns='promotion_last_5years',values='satisfaction_level')
EL_PRO.plot.bar()
plt.title("Satisfaction Level of Employees who left based on Number of Projects and Promotion Status")
plt.xlabel("Number Project")
plt.ylabel("Satisfaction Level")


# From the output displayed, the insight gotten it can be seen that as the number of projects embarked on by employees who left exceeded 4, the satisfaction level began to decline and they where not promoted in the last five years. Hence an increase in the number of projects resulting in a decline in satisfaction level and employee promotion status can be seen as reasons as to why employees are leaving the company.

# In[34]:


Existing_Employee_PRO =EEdata.pivot_table(index='number_project',columns='promotion_last_5years',values='satisfaction_level')
Existing_Employee_PRO.plot.bar()
plt.title("Satisfaction Level of Existing Employee based on Number of Projects and Promotion Status")
plt.xlabel("Number Project")
plt.ylabel("Satisfaction Level")


# From the output displayed, the insight gotten it can be seen that as the number of projects embarked on by employees still in the company exceeded 4, the satisfaction level began to decline and they where not promoted in the last five years, this can also be seen as a trend for employees who left. Hence an increase in the number of projects resulting in a decline in satisfaction level and employee promotion status can be seen as reasons as to which exsiting employees are prone to leave the company.

# In[ ]:




