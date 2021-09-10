import numpy as np #导入数值计算拓展模块
import pandas as pd #导入数据分析模块
from sklearn import preprocessing
data=pd.read_csv(r"C:/Users/cheng/Desktop/pyTest/Q1_influence.csv",index_col="ID") #读取数据
zdata=preprocessing.MinMaxScaler().fit_transform(data) #极大极小标准化
def entropy(data): #定义熵函数,返回综合得分
    m,n=np.shape(data) #数据维度
    data[np.where(data==0)]=0.0001 #替换0值
    data=pd.DataFrame(data).values #数据框化后矩阵化
    col_sum=data.sum(axis=0) #求列和
    pij=data/col_sum #占比
    entrop=-np.sum(pij*np.log(pij),axis=0) #信息熵
    w=(1-entrop)/np.sum(1-entrop,axis=0) #权重
    print(w) #观察权重是否合理
    score=np.dot(data,w) #得分
    return score
if __name__=="__main__":
    score=pd.DataFrame(entropy(zdata),index=data.index) #得分
    score.columns=["综合得分"] #给出列名
    result=pd.concat([data,score],axis=1) #沿着列的方向水平延伸合并
    print(result) #测试
    result.to_csv("output.csv") #保存为excel
