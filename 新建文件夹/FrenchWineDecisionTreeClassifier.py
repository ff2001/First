#coding:gbk
"""
利用决策树算法进行分类
作者：植物生产类4班方芳
日期：2020.5.14
"""
import pandas as pd           # 调入需要用的库
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sb
#%matplotlib inline
# 调入数据
df = pd.read_csv('frenchwine.csv')
df.columns = ['species','alcohol', 'malic_acid', 'ash', 'alcalinity ash','magnesium']
# # 查看前6条数据

# 查看数据描述性统计信息
df.describe()
print(df.describe())


plt.figure(figsize=(20, 10)) #利用seaborn库绘制3个葡萄品种不同参数图
for column_index, column in enumerate(df.columns):
    if column == 'species':
        continue
    plt.subplot(3, 3, column_index + 1)
    sb.violinplot(x='species', y=column, data=df)
plt.show()

# 首先对数据进行切分，即划分出训练集和测试集
from sklearn.model_selection import train_test_split #调入sklearn库中交叉检验，划分训练集和测试集
all_inputs = df[['alcohol', 'malic_acid','ash',
                             'alcalinity ash','magnesium']].values
all_species = df['species'].values

(X_train,
 X_test,
 Y_train,
 Y_test) = train_test_split(all_inputs, all_species, train_size=0.85, random_state=1)#85%的数据选为训练集

# 使用决策树算法进行训练
from sklearn.tree import DecisionTreeClassifier #调入sklearn库中的DecisionTreeClassifier来构建决策树
# 定义一个决策树对象
decision_tree_classifier = DecisionTreeClassifier()
# 训练模型
model = decision_tree_classifier.fit(X_train, Y_train)
# 输出模型的准确度
print(decision_tree_classifier.score(X_test, Y_test)) 


# 使用训练的模型进行预测,导入题中数据
X_test=[[13.52,3.17,2.72,23.5,97],[12.42,2.55,2.27,22,90],[13.76,1.53,2.7,19.5,132]]
print(X_test[0:3])#利用3个数据进行测试，即取3个数据作为模型的输入端
model.predict(X_test[0:3])
dict1={"Zinfandel":"仙粉黛","Sauvignon":"赤霞珠","Syrah":"西拉"}#对应品种具体的中文名
a=model.predict(X_test[0:3])#输出测试的结果，即输出模型预测的结果
for i in range(3):
	a[i]=dict1[a[i]]
print(a) 
