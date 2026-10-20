#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as Plt

df = pd.read_csv("../data/employees.csv")

print(df.head())


# In[3]:


print ("Total Employees:",len(df))

print("\nSalary Details: ")
print (df["salary"].describe())
print("\nEmployees earning above 50000: ")
print(df[df["salary"]>50000][["name","salary"]])


# In[4]:


chennai_employees=df[df["city"]=="Chennai"]
print(chennai_employees[["name","department","salary"]])


# In[6]:


import matplotlib.pyplot as plt
df.groupby("department")["salary"].mean().plot(kind="bar")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average salary")
plt.tight_layout()
plt.savefig("../reports/average_salary.png")
plt.show()


# In[ ]:




