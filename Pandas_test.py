# Importing pandas package 
import pandas as pd 
# Creating two dictionaries 
d1 = { 'Name':['Ram','Raj','Sita','Gita'], 'Age':[[20,32,16],23,36,29] } 
# Creating DataFrame 
df = pd.DataFrame(d1) 
# Display the DataFrame 
print("Original DataFrame:\n",df,"\n\n") 
# Exploding the column age # where we encounter the list 
df = df.explode('Age') 
# Display modified DataFrame 
print("Modified DataFrame:\n",df,"\n")