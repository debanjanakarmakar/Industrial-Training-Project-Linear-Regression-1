import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)

empsal_df=pd.read_csv('empsalupdated.csv',index_col='empno')
mean=empsal_df.groupby(['state'])['salary','hra','conv','total'].mean()
print(mean)

mean.plot(kind='bar')
plt.title('State Wise Mean Of Salary,hra,conv & total')
plt.xlabel('States')
plt.ylabel('Mean Figures')
plt.tight_layout()
plt.legend(loc='best')
plt.show()

x=input('Press Enter to Continue')
