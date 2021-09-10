import numpy as np
import pandas as pd

supply=pd.read_csv('D:/TONGJI/MathematicalModeling/C/supply.csv')
order=pd.read_csv('D:/TONGJI/MathematicalModeling/C/order.csv')

data_frame = pd.DataFrame(columns=supply.columns,index=[])
bad_Week_num = pd.DataFrame(columns=['1'],index=[])
differ_Result = pd.DataFrame(columns=['1'],index=[])
for i in range(402):
    difference = supply.iloc[i]-order.iloc[i]
    tempNum=0
    differResult=0
    for j in range(240):
        differResult=differResult+difference[j]/240
        if difference[j]<0:
            tempNum =tempNum+1
    #dpp=pd.DataFrame(tempNum)
    
    #df=pd.DataFrame(difference)
    
    df_row=data_frame.shape[0]
    week_row=bad_Week_num.shape[0]
    differ_row=differ_Result.shape[0]
    
    data_frame.loc[df_row]=difference
    bad_Week_num.loc[week_row]=tempNum
    differ_Result.loc[differ_row]=differResult
    differ_Result.to_csv('differ_Result.csv',index=False)
    bad_Week_num.to_csv('bad_week_num.csv',index=False)
    data_frame.to_csv('difference.csv',index=False)
    #print(df)
    #df.columns=['W'+str(j) for j in range(240)]
    #df.to_csv('difference.csv',index=False)
